# dataset_dashboard/inject.py
from __future__ import annotations
from typing import List, Optional, Dict, Tuple
from datetime import datetime
import pytz

import dash
from dash import Input, Output, State, html, dcc, no_update
from dash.exceptions import PreventUpdate

import dataset_dashboard.components.compute as compute
from dataset_dashboard.constants import DATA_STAGES, status_order_for_tab
from dataset_dashboard.utils import to_local_str

# -------------------------
# Lightweight coherent caches
# -------------------------
_AGG_CACHE: Dict[tuple, Dict[str, int]] = {}
_STAGE_CACHE: Dict[tuple, Dict[str, int]] = {}
_LIST_CACHE: Dict[tuple, list] = {}

def _tab_updated_at(state, tab):
    return ((state.get("tabs", {}) or {}).get(tab, {}) or {}).get("updated_at")

def cached_aggregate_counts(state, tab):
    key = (tab, _tab_updated_at(state, tab))
    if key in _AGG_CACHE:
        return _AGG_CACHE[key]
    val = compute.aggregate_counts(state, tab)
    _AGG_CACHE.clear()
    _AGG_CACHE[key] = val
    return val

def cached_filtered_stage_counts(state, owner_sel, stage, tab):
    key = (tab, stage, (owner_sel or "All").lower(), _tab_updated_at(state, tab))
    if key in _STAGE_CACHE:
        return _STAGE_CACHE[key]
    val = compute.filtered_stage_counts(state, owner_sel, stage, tab)
    _STAGE_CACHE[key] = val
    return val

def cached_filtered_sorted_entries(state, owner_sel, vis_stages, status_filter, tab, sort_by):
    tab_key = "data" if (tab or "all").lower() == "all" else (tab or "data").lower()
    upd = _tab_updated_at(state, tab_key)
    key = (
        tab_key, upd,
        (owner_sel or "All"),
        tuple(vis_stages or ()),
        tuple(status_filter or ()),
        sort_by or "",
    )
    if key in _LIST_CACHE:
        return _LIST_CACHE[key]
    val = compute.filtered_sorted_entries(state, owner_sel, vis_stages, status_filter, tab, sort_by)
    _LIST_CACHE[key] = val
    return val

def _subtree_for_tab(state: dict, tab: str) -> dict:
    tabs = state.get("tabs", {}) or {}
    return tabs.get(tab) or {}

# -------------------------
# Selection helpers
# -------------------------
def _list_datasets_for_tab(state: dict, tab: str) -> List[str]:
    tab = (tab or "data").lower()
    jobs = (state.get("tabs", {}).get(tab, {}) or {}).get("jobs", {}) or {}
    names = set()
    for o_map in jobs.values():
        for m_map in (o_map or {}).values():
            for ds in (m_map or {}).keys():
                names.add(str(ds))
    return sorted(names)

def _chunk_indices_for_dataset(state: dict, tab: str, dataset: Optional[str], stage: Optional[str] = None) -> List[int]:
    if not dataset:
        return []
    tab = (tab or "data").lower()
    jobs = (state.get("tabs", {}).get(tab, {}) or {}).get("jobs", {}) or {}
    for o_map in jobs.values():
        for m_map in (o_map or {}).values():
            node = (m_map or {}).get(dataset)
            if not node or not isinstance(node, dict):
                continue
            if tab == "data":
                if not stage:
                    return []  # stage required to know which chunk list
                st_node = (node or {}).get(stage) or {}
                chunks = (st_node.get("chunks") or [])
                return list(range(len(chunks)))
            else:
                st_node = (node or {}).get("status") or {}
                chunks = (st_node.get("chunks") or [])
                return list(range(len(chunks)))
    return []

def _resolve_raw_href_for_selection(state: dict, tab: str, dataset: Optional[str], idx: Optional[int], stage: Optional[str], linker) -> Tuple[Optional[str], Optional[str]]:
    if not dataset or idx is None or idx < 0:
        return None, None
    tab = (tab or "data").lower()
    jobs = (state.get("tabs", {}).get(tab, {}) or {}).get("jobs", {}) or {}
    for o_map in jobs.values():
        for m_map in (o_map or {}).values():
            node = (m_map or {}).get(dataset)
            if not node or not isinstance(node, dict):
                continue
            if tab == "data":
                if not stage:
                    return None, None
                st_node = (node or {}).get(stage) or {}
                chunks = (st_node.get("chunks") or [])
            else:
                st_node = (node or {}).get("status") or {}
                chunks = (st_node.get("chunks") or [])
            if 0 <= idx < len(chunks):
                raw = chunks[idx].get("log")
                href = None
                if linker:
                    try:
                        href = linker.href_for(raw)
                    except Exception:
                        href = None
                return raw, href
    return None, None

def _parse_hash(hash_str: Optional[str]):
    """Return (dataset, idx, tab_override, stage_override) parsed from #pick?..."""
    from urllib.parse import parse_qs, unquote_plus
    if not hash_str or not hash_str.startswith("#pick?"):
        return None, None, None, None
    qs = hash_str[6:]
    qs_map = parse_qs(qs, keep_blank_values=True)
    ds = unquote_plus(qs_map.get("dataset", [""])[0]) or None
    idx_s = qs_map.get("idx", [""])[0]
    tab_override = (qs_map.get("tab", [""])[0] or "").lower() or None
    stage_override = (qs_map.get("stage", [""])[0] or "").lower() or None
    try:
        idx = int(idx_s)
    except Exception:
        idx = None
    if tab_override not in ("data", "features", "alphas", "strategies"):
        tab_override = None
    if tab_override != "data":
        stage_override = None
    return ds, idx, tab_override, stage_override

def _effective_tab(main_tab: str, tab_override: Optional[str]) -> str:
    main_tab = (main_tab or "all").lower()
    if main_tab == "all" and tab_override in ("data", "features", "alphas", "strategies"):
        return tab_override
    return main_tab if main_tab in ("data", "features", "alphas", "strategies") else "data"

# -------------------------
# Register callbacks
# -------------------------
def register_callbacks(app, cfg, host):
    store = host.store
    pie = host.pies
    linker = getattr(getattr(host, "table", None), "linker", None)

    # ----------------- MAIN refresh -----------------
    @app.callback(
        # KPIs
        Output("kpi-container", "children"),

        # Filter options
        Output("owner-filter", "options"),
        Output("stage-filter", "options"),
        Output("status-filter", "options"),

        # External pies (hidden)
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

        # Inputs
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
                groups_per_row, chunks_per_line, sort_by, rows_per_page,
                pager_active, current_page, cur_interval):

        ctx = dash.callback_context
        triggered_id = ctx.triggered[0]['prop_id'].split('.')[0] if ctx.triggered else None

        tab = str(tab or "all").lower()
        state = store.state()
        tab_for_subtree = "data" if tab == "all" else tab
        tree = _subtree_for_tab(state, tab_for_subtree)

        # Filters
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

        # Hidden external pies (keep valid)
        if tab == "data":
            data_counts = cached_aggregate_counts(state, "data")
            fig_ext_overview = pie.figure("data", "Overview",  data_counts, labels_order=status_vocab)
            fig_ext_stage    = pie.figure("data", "Stage",     cached_filtered_stage_counts(state, owner_sel, "stage", "data"),      labels_order=status_vocab)
            fig_ext_archive  = pie.figure("data", "Archive",   cached_filtered_stage_counts(state, owner_sel, "archive", "data"),    labels_order=status_vocab)
            fig_ext_enrich   = pie.figure("data", "Enrich",    cached_filtered_stage_counts(state, owner_sel, "enrich", "data"),     labels_order=status_vocab)
            fig_ext_cons     = pie.figure("data", "Consolidate",cached_filtered_stage_counts(state, owner_sel, "consolidate", "data"),labels_order=status_vocab)
        elif tab == "all":
            tot_counts = {}
            for tname in ("data", "features", "alphas", "strategies"):
                part = cached_aggregate_counts(state, tname)
                for k, v in part.items():
                    tot_counts[k] = tot_counts.get(k, 0) + int(v or 0)
            fig_ext_overview = pie.figure("all", "Overview", tot_counts, labels_order=status_vocab)
            fig_ext_stage    = pie.figure("data", "Stage",     cached_filtered_stage_counts(state, owner_sel, "stage", "data"),      labels_order=status_order_for_tab("data"))
            fig_ext_archive  = pie.figure("data", "Archive",   cached_filtered_stage_counts(state, owner_sel, "archive", "data"),    labels_order=status_order_for_tab("data"))
            fig_ext_enrich   = pie.figure("data", "Enrich",    cached_filtered_stage_counts(state, owner_sel, "enrich", "data"),     labels_order=status_order_for_tab("data"))
            fig_ext_cons     = pie.figure("data", "Consolidate",cached_filtered_stage_counts(state, owner_sel, "consolidate", "data"),labels_order=status_order_for_tab("data"))
        else:
            tab_counts = cached_aggregate_counts(state, tab)
            fig_ext_overview = pie.figure(tab, "Overview", tab_counts, labels_order=status_vocab)
            fig_ext_stage = fig_ext_archive = fig_ext_enrich = fig_ext_cons = fig_ext_overview

        # KPI + vertical pies (first taller)
        if tab == "all":
            tot_counts = {}
            for tname in ("data", "features", "alphas", "strategies"):
                part = cached_aggregate_counts(state, tname)
                for k, v in part.items():
                    tot_counts[k] = tot_counts.get(k, 0) + int(v or 0)
            pies_for_kpi = [
                pie.figure("all", "Overview",  tot_counts,                           labels_order=status_vocab),
                pie.figure("data", "Data",     cached_aggregate_counts(state,"data"),      labels_order=status_order_for_tab("data")),
                pie.figure("features", "Features", cached_aggregate_counts(state,"features"), labels_order=status_order_for_tab("features")),
                pie.figure("alphas", "Alphas", cached_aggregate_counts(state,"alphas"),    labels_order=status_order_for_tab("alphas")),
                pie.figure("strategies", "Strategies", cached_aggregate_counts(state,"strategies"), labels_order=status_order_for_tab("strategies")),
            ]
            k_counts = tot_counts
        elif tab == "data":
            data_counts = cached_aggregate_counts(state, "data")
            pies_for_kpi = [
                pie.figure("data", "Overview",  data_counts, labels_order=status_vocab),
                pie.figure("data", "Archive",   cached_filtered_stage_counts(state, owner_sel, "archive", "data"),    labels_order=status_vocab),
                pie.figure("data", "Stage",     cached_filtered_stage_counts(state, owner_sel, "stage", "data"),      labels_order=status_vocab),
                pie.figure("data", "Enrich",    cached_filtered_stage_counts(state, owner_sel, "enrich", "data"),     labels_order=status_vocab),
                pie.figure("data", "Consolidate",cached_filtered_stage_counts(state, owner_sel, "consolidate", "data"),labels_order=status_vocab),
            ]
            k_counts = data_counts
        else:
            tab_counts = cached_aggregate_counts(state, tab)
            pies_for_kpi = [pie.figure(tab, "Overview", tab_counts, labels_order=status_vocab)]
            k_counts = tab_counts

        pie_graphs = [
            dcc.Graph(
                figure=f,
                style={"height": "260px" if i == 0 else "200px", "marginBottom": "8px" if i < len(pies_for_kpi)-1 else "0px", "width": "100%"},
                config={"displayModeBar": False},
            ) for i, f in enumerate(pies_for_kpi)
        ]

        # Selection tools
        selection_tools = html.Div(
            [
                dcc.Location(id="url", refresh=False),
                html.Div("Selection", className="fw-bold mb-1"),
                html.Div(
                    [
                        dcc.Dropdown(id="sel-dataset-dd", placeholder="Dataset", clearable=False, style={"minWidth": "14rem", "marginRight": "8px"}),
                        dcc.Dropdown(id="sel-chunk-dd", placeholder="Chunk index", clearable=False, style={"width": "10rem", "marginRight": "8px"}),
                        html.Button("Copy log path", id="copy-selected-btn", n_clicks=0, className="btn btn-outline-secondary btn-sm"),
                        dcc.Store(id="selected-chunk-raw"),
                        dcc.Store(id="selected-chunk-href"),
                        html.Span(id="copy-feedback", className="text-muted", style={"fontSize": "12px", "marginLeft": "8px"}),
                    ],
                    style={"display": "flex", "alignItems": "center", "gap": "6px", "flexWrap": "wrap", "marginBottom": "6px"},
                ),
            ],
            style={"marginBottom": "8px"},
        )

        kpi_children = html.Div(
            [
                selection_tools,
                html.Div(host.kpis.render("all" if tab == "all" else tab, status_vocab, k_counts, per_row=3),
                         className="w-100", style={"width": "100%"}),
                html.Div(pie_graphs, style={"display": "flex", "flexDirection": "column", "width": "100%"}),
            ],
            className="w-100",
            style={"width": "100%", "alignSelf": "stretch", "height": "100%"},
        )

        pie_styles = [{"display": "none"}] * 5
        adv_style = {"display": "block"} if tab in ("data", "all") else {"display": "none"}

        # Tables & pagination
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
                slices = {"data": data_all, "features": feats_all, "alphas": alphas_all, "strategies": strats_all}
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

            table = host.table.render(
                "all",
                slices["data"],  # signature compatibility
                groups_per_row,
                chunks_per_line,
                state,
                vis_stages=vis_stages,
                entries_by_section=slices,
                page_meta={
                    "mode": "all",
                    "current_page": current_page,
                    "rows_per_page": rows_per_page,
                    "total_pages": total_pages,
                    "totals": totals,
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
            entries_sorted = compute.filtered_sorted_entries(state, owner_sel, vis_stages, status_filter, tab, sort_by)
            total_entries = len(entries_sorted)

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

        table_children = html.Div([table], style={"width": "100%"})

        # Footer
        meta = tree.get("meta") or {}
        env = meta.get("env", "local")
        last_ingest = meta.get("last_ingest_at")
        now = to_local_str(datetime.now(pytz.utc))
        now_indicator = f"{env.upper()} | {now} | Last ingest: {last_ingest or '—'}"

        # Respect configured refresh_ms
        desired_interval = int(getattr(cfg, "refresh_ms", 30000) or 30000)
        next_interval = no_update if (cur_interval == desired_interval) else desired_interval

        return (
            kpi_children,
            owner_opts,
            stage_opts,
            status_opts,
            fig_ext_stage, fig_ext_archive, fig_ext_enrich, fig_ext_cons, fig_ext_overview,
            "",
            table_children,
            now_indicator,
            next_interval,
            adv_style,
            *([{"display": "none"}] * 5),
            current_page,
            pager_max_value,
            pager_active_page,
            pager_style,
        )

    # ----------------- Selection: set values from hash -----------------
    @app.callback(
        Output("sel-dataset-dd", "value"),
        Output("sel-chunk-dd", "value"),
        Input("url", "hash"),
        prevent_initial_call=True,
    )
    def on_hash_to_selection(hash_str):
        ds, idx, _tab_override, _stage = _parse_hash(hash_str)
        if ds is None:
            raise PreventUpdate
        return ds, (idx if isinstance(idx, int) else None)

    # ----------------- Selection: options for dataset/chunk -----------------
    @app.callback(
        Output("sel-dataset-dd", "options"),
        Output("sel-chunk-dd", "options"),
        Input("main-tabs", "value"),
        Input("sel-dataset-dd", "value"),
        Input("url", "hash"),
        prevent_initial_call=True,
    )
    def selection_options(tab, ds_value, hash_str):
        state = store.state()
        _ds, _idx, tab_override, stage_override = _parse_hash(hash_str)
        eff_tab = _effective_tab(tab, tab_override)
        ds_options = [{"label": n, "value": n} for n in _list_datasets_for_tab(state, eff_tab)]
        ch_options = [{"label": str(i), "value": i}
                      for i in _chunk_indices_for_dataset(state, eff_tab, ds_value, stage_override)] if ds_value else []
        return ds_options, ch_options

    # ----------------- Selection: resolve raw/href for copy button ---------
    @app.callback(
        Output("selected-chunk-raw", "data"),
        Output("selected-chunk-href", "data"),
        Input("main-tabs", "value"),
        Input("sel-dataset-dd", "value"),
        Input("sel-chunk-dd", "value"),
        State("url", "hash"),
        prevent_initial_call=True,
    )
    def selection_paths(tab, ds, idx, hash_str):
        state = store.state()
        _ds, _idx, tab_override, stage_override = _parse_hash(hash_str)
        eff_tab = _effective_tab(tab, tab_override)
        raw, href = _resolve_raw_href_for_selection(state, eff_tab, ds, idx, stage_override, linker)
        return raw, href

    # ----------------- Copy button (client-only copy to clipboard) --------
    app.clientside_callback(
        """
        function(n, raw) {
            if (!n) return "";
            try {
                if (raw && navigator && navigator.clipboard) {
                    navigator.clipboard.writeText(String(raw));
                    return "Copied log path.";
                }
                return "Nothing to copy.";
            } catch(e) {
                return "Copy failed.";
            }
        }
        """,
        Output("copy-feedback", "children"),
        Input("copy-selected-btn", "n_clicks"),
        State("selected-chunk-raw", "data"),
        prevent_initial_call=True,
    )


# -------------------------
# Ingest routes (unchanged core; cache clears)
# -------------------------
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
                    ch["log"] = ch[k]; break
        if "proc" not in ch or not ch.get("proc"):
            for k in ("proc_url", "process_url", "ui", "url", "link"):
                if ch.get(k):
                    ch["proc"] = ch[k]; break
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
        _AGG_CACHE.clear()
        _STAGE_CACHE.clear()
        _LIST_CACHE.clear()

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
        leaf = (tree.get("jobs", {})
                .get(owner, {}).get(mode, {}).get(dataset, {}))
        return _jsonify(leaf)