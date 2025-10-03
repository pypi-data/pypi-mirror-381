# dataset_dashboard/inject.py
from __future__ import annotations
import dash_bootstrap_components as dbc
from datetime import datetime
from typing import List, Optional, Dict, Tuple
from .caching import cache
import pytz
from dash import Input, Output, State, html, dcc
from dash.exceptions import PreventUpdate
import dash
import dataset_dashboard.components.compute as compute
from dataset_dashboard.constants import DATA_STAGES, status_order_for_tab
from dataset_dashboard.utils import to_local_str


# -------------------------
# Lightweight coherent caches
# -------------------------
_AGG_CACHE: Dict[tuple, Dict[str, int]] = {}
_STAGE_CACHE: Dict[tuple, Dict[str, int]] = {}

def _tab_updated_at(state, tab):
    return ((state.get("tabs", {}) or {}).get(tab, {}) or {}).get("updated_at")

def cached_aggregate_counts(state, tab):
    key = (tab, _tab_updated_at(state, tab))
    if key in _AGG_CACHE:
        return _AGG_CACHE[key]
    val = compute.aggregate_counts(state, tab)
    _AGG_CACHE.clear()          # small & coherent
    _AGG_CACHE[key] = val
    return val

def cached_filtered_stage_counts(state, owner_sel, stage, tab):
    key = (tab, stage, (owner_sel or "All").lower(), _tab_updated_at(state, tab))
    if key in _STAGE_CACHE:
        return _STAGE_CACHE[key]
    val = compute.filtered_stage_counts(state, owner_sel, stage, tab)
    _STAGE_CACHE[key] = val
    return val


def _subtree_for_tab(state: dict, tab: str) -> dict:
    tabs = state.get("tabs", {}) or {}
    return tabs.get(tab) or {}


def register_callbacks(app, cfg, host):
    store = host.store
    pie = host.pies

    # --- Main refresh callback (stable inputs!) ---
    @app.callback(
    # KPIs
    Output("kpi-container", "children"),

    # Filter options
    Output("owner-filter", "options"),
    Output("stage-filter", "options"),
    Output("status-filter", "options"),

    # External pies (kept hidden but updated so nothing breaks)
    Output("pie-stage", "figure"),
    Output("pie-archive", "figure"),
    Output("pie-enrich", "figure"),
    Output("pie-consolidate", "figure"),
    Output("pie-overview", "figure"),

    # Table + footer + refresh
    Output("table-title", "children"),
    Output("table-container", "children"),
    Output("now-indicator", "children"),
    Output("interval", "interval"),

    # Visibilities
    Output("advanced-controls", "style"),
    Output("pie-stage", "style"),
    Output("pie-archive", "style"),
    Output("pie-enrich", "style"),
    Output("pie-consolidate", "style"),
    Output("pie-overview", "style"),

    Output("table-page", "data", allow_duplicate=True),

    # Pager outputs
    Output("table-pager", "max_value"),
    Output("table-pager", "active_page"),
    Output("table-pager", "style"),

    # Inputs (stable set)
    Input("interval", "n_intervals"),
    Input("main-tabs", "value"),
    Input("owner-filter", "value"),
    Input("stage-filter", "value"),
    Input("status-filter", "value"),
    Input("table-groups", "value"),
    Input("chunks-per-line", "value"),
    Input("sort-by", "value"),
    Input("rows-per-page", "value"),
    Input("table-pager", "active_page"),
    State("table-page", "data"),
    State("interval", "interval"),
    prevent_initial_call=True,
    )
    def refresh(_n, tab,
                owner_sel, stage_filter, status_filter,
                groups_per_row, chunks_per_line, sort_by, rows_per_page, pager_active, current_page, cur_interval):

        from dash import callback_context

        ctx = callback_context
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

        tab = str(tab or "all").lower()
        state = store.state()
        tab_for_subtree = "data" if tab == "all" else tab
        tree = _subtree_for_tab(state, tab_for_subtree)

        # --- Filter option lists ---
        owner_opts = store.list_filters_for_tab(tab_for_subtree)
        stage_opts = [{"label": s.title(), "value": s}] if False else []
        if tab in ("data", "all"):
            stage_opts = [{"label": s.title(), "value": s} for s in DATA_STAGES]

        if tab == "all":
            union_vocab = sorted(set(
                status_order_for_tab("data")
                + status_order_for_tab("features")
                + status_order_for_tab("alphas")
                + status_order_for_tab("strategies")
            ))
            status_vocab = union_vocab
        else:
            status_vocab = status_order_for_tab(tab_for_subtree)
        status_opts = [{"label": s, "value": s} for s in status_vocab]

        # --- External pies (hidden but valid) ---
        if tab == "data":
            data_counts = cached_aggregate_counts(state, "data")
            fig_ext_overview = pie.figure("data", "Overview", data_counts, labels_order=status_vocab)
            fig_ext_stage      = pie.figure("data", "Stage",      cached_filtered_stage_counts(state, owner_sel, "stage", "data"),      labels_order=status_vocab)
            fig_ext_archive    = pie.figure("data", "Archive",    cached_filtered_stage_counts(state, owner_sel, "archive", "data"),    labels_order=status_vocab)
            fig_ext_enrich     = pie.figure("data", "Enrich",     cached_filtered_stage_counts(state, owner_sel, "enrich", "data"),     labels_order=status_vocab)
            fig_ext_cons       = pie.figure("data", "Consolidate",cached_filtered_stage_counts(state, owner_sel, "consolidate", "data"),labels_order=status_vocab)
        elif tab == "all":
            tot_counts = {}
            for tname in ("data", "features", "alphas", "strategies"):
                part = cached_aggregate_counts(state, tname)
                for k, v in part.items():
                    tot_counts[k] = tot_counts.get(k, 0) + int(v or 0)
            fig_ext_overview = pie.figure("all", "Overview", tot_counts, labels_order=status_vocab)
            # keep data-stage pies filled for hidden slots
            fig_ext_stage      = pie.figure("data", "Stage",      cached_filtered_stage_counts(state, owner_sel, "stage", "data"),      labels_order=status_order_for_tab("data"))
            fig_ext_archive    = pie.figure("data", "Archive",    cached_filtered_stage_counts(state, owner_sel, "archive", "data"),    labels_order=status_order_for_tab("data"))
            fig_ext_enrich     = pie.figure("data", "Enrich",     cached_filtered_stage_counts(state, owner_sel, "enrich", "data"),     labels_order=status_order_for_tab("data"))
            fig_ext_cons       = pie.figure("data", "Consolidate",cached_filtered_stage_counts(state, owner_sel, "consolidate", "data"),labels_order=status_order_for_tab("data"))
        else:
            tab_counts = cached_aggregate_counts(state, tab)
            fig_ext_overview = pie.figure(tab, "Overview", tab_counts, labels_order=status_vocab)
            fig_ext_stage = fig_ext_archive = fig_ext_enrich = fig_ext_cons = fig_ext_overview

        # --- KPI block + pies (in correct order) ---
        if tab == "all":
            # Overview (ALL), then Data, Features, Alphas, Strategies
            tot_counts = {}
            for tname in ("data", "features", "alphas", "strategies"):
                part = cached_aggregate_counts(state, tname)
                for k, v in part.items():
                    tot_counts[k] = tot_counts.get(k, 0) + int(v or 0)

            f_all_overview   = pie.figure("all",       "Overview",  tot_counts,                         labels_order=status_vocab)
            f_data_overview  = pie.figure("data",      "Data",      cached_aggregate_counts(state,"data"),      labels_order=status_order_for_tab("data"))
            f_feat_overview  = pie.figure("features",  "Features",  cached_aggregate_counts(state,"features"),  labels_order=status_order_for_tab("features"))
            f_alpha_overview = pie.figure("alphas",    "Alphas",    cached_aggregate_counts(state,"alphas"),    labels_order=status_order_for_tab("alphas"))
            f_strat_overview = pie.figure("strategies","Strategies",cached_aggregate_counts(state,"strategies"),labels_order=status_order_for_tab("strategies"))

            pies_for_kpi = [f_all_overview, f_data_overview, f_feat_overview, f_alpha_overview, f_strat_overview]
            k_counts = tot_counts

        elif tab == "data":
            # Order: Overview, Archive, Stage, Enrich, Consolidate
            data_counts = cached_aggregate_counts(state, "data")
            f_overview  = pie.figure("data", "Overview",  data_counts, labels_order=status_vocab)
            f_archive   = pie.figure("data", "Archive",   cached_filtered_stage_counts(state, owner_sel, "archive", "data"),    labels_order=status_vocab)
            f_stage     = pie.figure("data", "Stage",     cached_filtered_stage_counts(state, owner_sel, "stage", "data"),      labels_order=status_vocab)
            f_enrich    = pie.figure("data", "Enrich",    cached_filtered_stage_counts(state, owner_sel, "enrich", "data"),     labels_order=status_vocab)
            f_cons      = pie.figure("data", "Consolidate",cached_filtered_stage_counts(state, owner_sel, "consolidate", "data"),labels_order=status_vocab)

            pies_for_kpi = [f_overview, f_archive, f_stage, f_enrich, f_cons]
            k_counts = data_counts

        else:
            tab_counts = cached_aggregate_counts(state, tab)
            pies_for_kpi = [pie.figure(tab, "Overview", tab_counts, labels_order=status_vocab)]
            k_counts = tab_counts

        # Vertical pies; first one ~30% taller; stretch KPI block to panel width/height
        pie_graphs = []
        for i, f in enumerate(pies_for_kpi):
            pie_graphs.append(
                dcc.Graph(
                    figure=f,
                    style={
                        "height": "260px" if i == 0 else "200px",
                        "marginBottom": "8px" if i < len(pies_for_kpi)-1 else "0px",
                        "width": "100%",
                    },
                    config={"displayModeBar": False},
                )
            )

        kpi_children = html.Div(
            [
                html.Div(host.kpis.render("all" if tab == "all" else tab, status_vocab, k_counts, per_row=3),
                        className="w-100", style={"width": "100%"}),
                html.Div(pie_graphs, style={"display": "flex", "flexDirection": "column", "width": "100%"}),
            ],
            className="w-100",
            style={"width": "100%", "alignSelf": "stretch", "height": "100%"},
        )

        # Always hide the external pie components
        pie_styles = [{"display": "none"}] * 5

        # --- Advanced controls visibility ---
        adv_style = {"display": "block"} if tab in ("data", "all") else {"display": "none"}

        # --- Tables & pagination ---
        vis_stages = list(stage_filter or DATA_STAGES) if tab in ("data", "all") else []
        rows_per_page = int(rows_per_page) if rows_per_page else 20

        if tab == "all":
            data_all   = compute.filtered_sorted_entries(state, owner_sel, vis_stages, status_filter, "data",       sort_by)
            feats_all  = compute.filtered_sorted_entries(state, owner_sel, [],          status_filter, "features",   sort_by)
            alphas_all = compute.filtered_sorted_entries(state, owner_sel, [],          status_filter, "alphas",     sort_by)
            strats_all = compute.filtered_sorted_entries(state, owner_sel, [],          status_filter, "strategies", sort_by)

            totals = {
                "data": len(data_all),
                "features": len(feats_all),
                "alphas": len(alphas_all),
                "strategies": len(strats_all),
            }

            if rows_per_page == 999999:
                total_pages = 1
                current_page = 0
                slices = {
                    "data": data_all,
                    "features": feats_all,
                    "alphas": alphas_all,
                    "strategies": strats_all,
                }
            else:
                total_pages = max(
                    1,
                    *[
                        (totals[k] + rows_per_page - 1) // max(1, rows_per_page)
                        for k in totals
                    ],
                )

                reset_triggers = ['main-tabs', 'owner-filter', 'stage-filter', 'status-filter', 'sort-by', 'rows-per-page']
                if triggered_id == "table-pager":
                    current_page = (pager_active - 1) if pager_active else int(current_page or 0)
                elif triggered_id in reset_triggers:
                    current_page = 0
                else:
                    current_page = int(current_page or 0)
                current_page = max(0, min(current_page, total_pages - 1))

                def _slice(lst):
                    start = current_page * rows_per_page
                    end = min(start + rows_per_page, len(lst))
                    return lst[start:end]

                slices = {
                    "data": _slice(data_all),
                    "features": _slice(feats_all),
                    "alphas": _slice(alphas_all),
                    "strategies": _slice(strats_all),
                }

            # Per-section titles (counts & page info handled inside TableComponent)
            table_title = ""

            table = host.table.render(
                "all",
                slices["data"],                # unused for 'all' logic; kept for signature
                groups_per_row,
                chunks_per_line,
                state,
                vis_stages=vis_stages,
                entries_by_section=slices,
                page_meta={
                    "mode": "all",
                    "current_page": current_page,      # 0-index
                    "rows_per_page": rows_per_page,
                    "total_pages": total_pages,
                    "totals": totals,                  # dict per section
                },
            )

            if total_pages > 1:
                pager_max_value = total_pages
                pager_active_page = current_page + 1
                pager_style = {
                    "display": "inline-flex",
                    "flexWrap": "wrap",
                    "gap": "6px",
                    "alignItems": "center",
                    "maxWidth": "100%",
                }
            else:
                pager_max_value = 1
                pager_active_page = 1
                pager_style = {"display": "none"}

        else:
            # Single tab
            entries_sorted = compute.filtered_sorted_entries(state, owner_sel, vis_stages, status_filter, tab, sort_by)
            total_entries = len(entries_sorted)
            table_title = ""  # per-table heading is rendered with the table itself

            if rows_per_page == 999999:
                rows_per_page = total_entries + 1

            total_pages = max(1, (total_entries + rows_per_page - 1) // rows_per_page)

            reset_triggers = ['main-tabs', 'owner-filter', 'stage-filter', 'status-filter', 'sort-by', 'rows-per-page']
            if triggered_id == "table-pager":
                current_page = (pager_active - 1) if pager_active else int(current_page or 0)
            elif triggered_id in reset_triggers:
                current_page = 0
            else:
                current_page = int(current_page or 0)
            current_page = max(0, min(current_page, total_pages - 1))

            start = current_page * rows_per_page
            end = min(start + rows_per_page, total_entries)
            sliced_entries = entries_sorted[start:end]

            table = host.table.render(
                tab,
                sliced_entries,
                groups_per_row,
                chunks_per_line,
                state,
                vis_stages=vis_stages,
                page_meta={
                    "mode": "single",
                    "current_page": current_page,
                    "rows_per_page": rows_per_page,
                    "total_pages": total_pages,
                    "total_count": total_entries,
                },
            )

            if total_pages > 1:
                pager_max_value = total_pages
                pager_active_page = current_page + 1
                pager_style = {
                    "display": "inline-flex",
                    "flexWrap": "wrap",
                    "gap": "6px",
                    "alignItems": "center",
                    "maxWidth": "100%",
                }
            else:
                pager_max_value = 1
                pager_active_page = 1
                pager_style = {"display": "none"}

        # Footer
        meta = tree.get("meta") or {}
        env = meta.get("env", "local")
        last_ingest = meta.get("last_ingest_at")
        now = to_local_str(datetime.now(pytz.utc))
        now_indicator = f"{env.upper()} | {now} | Last ingest: {last_ingest or '—'}"

        next_interval = cur_interval

        return (
            kpi_children,
            owner_opts,
            stage_opts,
            status_opts,
            # external pies (hidden)
            fig_ext_stage, fig_ext_archive, fig_ext_enrich, fig_ext_cons, fig_ext_overview,
            table_title,
            table,
            now_indicator,
            next_interval,
            adv_style,
            *pie_styles,
            current_page,
            pager_max_value,
            pager_active_page,
            pager_style,
        )

    # --- Reset table page on filter changes ---
    @app.callback(
        Output("table-page", "data"),
        Input("table-pager", "active_page"),
        Input("main-tabs", "value"),
        Input("owner-filter", "value"),
        Input("stage-filter", "value"),
        Input("status-filter", "value"),
        Input("sort-by", "value"),
        Input("rows-per-page", "value"),
        prevent_initial_call=True,
    )
    def update_table_page(pager_active, tab, owner, stage, status, sort, rpp):
        ctx = dash.callback_context
        if not ctx.triggered:
            raise PreventUpdate
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if triggered_id == "table-pager":
            if pager_active is None:
                raise PreventUpdate
            return pager_active - 1
        else:  # Any other input (filters, sort, etc.) triggers reset
            return 0


def register_ingest_routes(server, host):
    from flask import request, jsonify

    def _canon_status(tab: str, raw: Optional[str]) -> str:
        vocab = set(status_order_for_tab(tab))
        s = (raw or "other")
        s = s.lower() if tab == "data" else s
        return s if s in vocab else "other"

    def _canon_stage(tab: str, raw_stage: Optional[str]) -> Optional[str]:
        t = (tab or "data").lower()
        if t != "data":
            return "status"
        s = str(raw_stage or "").strip().lower()
        aliases = {
            "arch": "archive", "archives": "archive", "archive": "archive",
            "stage": "stage", "staging": "stage",
            "enrich": "enrich", "enrichment": "enrich", "enriched": "enrich",
            "consolidate": "consolidate", "consolidation": "consolidate", "cons": "consolidate",
        }
        s = aliases.get(s, s)
        return s if s in set(DATA_STAGES) else None

    def _canon_chunk_fields(tab: str, ch: dict) -> dict:
        ch = dict(ch or {})
        ch["status"] = _canon_status(tab, ch.get("status") or ch.get("state") or ch.get("result"))
        if "log" not in ch or not ch.get("log"):
            for k in ("log_path", "logfile", "logfile_path", "raw_log", "raw", "path"):
                if ch.get(k):
                    ch["log"] = ch[k]
                    break
        if "proc" not in ch or not ch.get("proc"):
            for k in ("proc_url", "process_url", "ui", "url", "link"):
                if ch.get(k):
                    ch["proc"] = ch[k]
                    break
        return ch

    def _canon_items(tab: str, items: List[dict]) -> List[dict]:
        out: List[dict] = []
        for it in items or []:
            it = dict(it or {})
            stg = _canon_stage(tab, it.get("stage"))
            if stg is None:
                continue
            chs = [_canon_chunk_fields(tab, ch) for ch in (it.get("chunks") or [])]
            it["stage"] = stg if (tab or "data").lower() == "data" else "status"
            it["chunks"] = chs
            if "data_name" not in it or not it.get("data_name"):
                for k in ("dataset", "name", "data", "id"):
                    if it.get(k):
                        it["data_name"] = it[k]
                        break
            out.append(it)
        return out

    def _apply(tab: str, items: List[dict], meta: Optional[dict]):
        host.store.apply_snapshot_with_meta_tab(tab, items, meta or {})
        # IMPORTANT: clear caches so UI reflects new data immediately
        _AGG_CACHE.clear()
        _STAGE_CACHE.clear()

    @server.route("/ingest_snapshot", methods=["POST"])
    def ingest_snapshot():
        try:
            body = request.get_json(force=True, silent=False)
            if isinstance(body, list):
                items = _canon_items("data", body)
                _apply("data", items, {})
                return jsonify({"ok": True})
            if not isinstance(body, dict):
                return jsonify({"ok": False, "error": "Unsupported payload"}), 400

            tabs_pack = body.get("tabs")
            if isinstance(tabs_pack, dict):
                for t, pack in tabs_pack.items():
                    if not isinstance(pack, dict):
                        continue
                    tab = str(t).lower()
                    if tab == "all":
                        continue
                    items = pack.get("snapshot") or pack.get("items") or []
                    meta = pack.get("meta") or {}
                    items = _canon_items(tab, list(items or []))
                    _apply(tab, items, dict(meta or {}))
                return jsonify({"ok": True})

            tab = str(body.get("tab") or "data").lower()
            if tab == "all":
                return jsonify({"ok": False, "error": "tab 'all' is synthetic"}), 400
            items = body.get("snapshot") or body.get("items") or []
            meta = body.get("meta") or {}
            if not isinstance(items, list):
                return jsonify({"ok": False, "error": "Send {snapshot:[...]} or a JSON array"}), 400
            items = _canon_items(tab, list(items or []))
            _apply(tab, items, dict(meta or {}))
            return jsonify({"ok": True})
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 400

    @server.route("/__debug__/store_summary", methods=["GET"])
    def store_summary():
        from flask import jsonify as _jsonify
        st = host.store.state()
        tabs = st.get("tabs", {})
        out: Dict[str, Dict] = {"tabs": {}}
        for t, tree in tabs.items():
            jobs = tree.get("jobs", {}) or {}
            n = 0
            for o_map in jobs.values():
                for m_map in o_map.values():
                    n += len(m_map)
            meta = tree.get("meta", {}) or {}
            owners = sorted(jobs.keys())
            modes = set()
            for o_map in jobs.values():
                modes.update(o_map.keys())
            out["tabs"][t] = {
                "datasets_total": n,
                "meta": {
                    "env": meta.get("env"),
                    "last_ingest_at": meta.get("last_ingest_at"),
                    "owner_labels": meta.get("owner_labels", {}),
                },
                "modes": sorted(modes),
                "owners": owners,
                "updated_at": tree.get("updated_at"),
            }
        return _jsonify(out)

    @server.route("/__debug__/leaf", methods=["GET"])
    def debug_leaf():
        from flask import request as _req, jsonify as _jsonify
        st = host.store.state()
        tab = _req.args.get("tab", "data")
        owner = _req.args.get("owner", "kimdg")
        mode = _req.args.get("mode", "live")
        dataset = _req.args.get("dataset")
        tree = st.get("tabs", {}).get(tab, {})
        leaf = (tree.get("jobs", {}).get(owner, {}).get(mode, {}).get(dataset, {}))
        return _jsonify(leaf)