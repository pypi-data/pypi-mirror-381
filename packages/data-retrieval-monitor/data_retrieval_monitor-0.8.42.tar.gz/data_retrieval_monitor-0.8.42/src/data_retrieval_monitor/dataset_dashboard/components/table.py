# dataset_dashboard/components/table.py
from typing import List, Optional, Tuple, Dict, Union
from dash import html, dcc
import dash_bootstrap_components as dbc

from dataset_dashboard.components.compute import best_status
from dataset_dashboard.constants import DATA_STAGES, rgb_for_tab


RowT = Tuple[int, str, str, str, dict]  # (rank, owner, mode, dataset_name, detail_map)


class TableComponent:
    """
    - Data tab: Dataset + ONLY the visible_stages columns (defaults to all DATA_STAGES).
    - All tab: Separate tables for Data, Features, Alphas, Strategies.
      Each section can receive its own entry list and its own caption.
    - Other tabs (features/alphas/strategies): Name + single Status column
    """

    def __init__(self, log_linker, clipboard_fallback_open: bool):
        self.linker = log_linker
        self.fallback_open = bool(clipboard_fallback_open)

    @staticmethod
    def _shade(tab: str, status: Optional[str], alpha=0.18):
        if not status:
            return {"backgroundColor": "#FFFFFF"}
        r, g, b = rgb_for_tab(tab).get(status, (230, 230, 230))
        return {"backgroundColor": f"rgba({r},{g},{b},{alpha})"}

    def _clipboard_button(self, text: str):
        icon = html.Span(
            "📄",
            title=f"Copy: {text}",
            style={"display": "inline-block", "fontSize": "12px", "opacity": 0.9, "marginLeft": "6px", "cursor": "pointer"},
        )
        overlay = dcc.Clipboard(
            content=text,
            title="Copy",
            style={
                "position": "absolute",
                "left": 0,
                "top": 0,
                "width": "1.6em",
                "height": "1.6em",
                "opacity": 0.01,
                "zIndex": 5,
                "cursor": "pointer",
                "border": 0,
                "background": "transparent",
            },
        )
        return html.Span([icon, overlay], style={"position": "relative", "display": "inline-block", "marginRight": "10px"})

    def _chunk_badge_and_links(self, tab: str, ch: dict, idx: int, prefix: str):
        label = f"{prefix}{idx}"
        st = (ch.get("status") or "other")
        proc = ch.get("proc")
        raw = ch.get("log")
        href = self.linker.href_for(raw)

        badge = html.Span(
            label,
            title=str(label),
            style={
                "display": "inline-block",
                "padding": "2px 6px",
                "borderRadius": "8px",
                "fontSize": "12px",
                "marginRight": "6px",
                **self._shade(tab, st, 0.35),
            },
        )
        bits = [badge]

        if proc:
            bits.append(
                html.A(
                    "p",
                    href=proc,
                    target="_blank",
                    title="proc",
                    style={"marginRight": "6px", "textDecoration": "underline"},
                )
            )
        if href:
            bits.append(
                html.A(
                    "l",
                    href=href,
                    target="_blank",
                    title="open log",
                    style={"marginRight": "0", "textDecoration": "underline", "fontSize": "12px"},
                )
            )
            bits.append(self._clipboard_button(str(raw or href)))
        elif raw:
            bits.append(self._clipboard_button(str(raw)))
        return bits

    def _chunk_block(self, tab: str, chunks: List[dict], chunks_per_line: int, prefix: str):
        if not chunks:
            return html.I("—", className="text-muted")
        cpl = max(1, int(chunks_per_line or 6))
        lines = []
        for i in range(0, len(chunks), cpl):
            seg = chunks[i : i + cpl]
            seg_nodes = []
            for j, ch in enumerate(seg):
                seg_nodes.extend(self._chunk_badge_and_links(tab, ch, idx=i + j, prefix=prefix))
            lines.append(html.Div(seg_nodes, style={"whiteSpace": "nowrap"}))
        return html.Div(lines, style={"display": "grid", "rowGap": "2px"})

    # ---------- helpers ----------
    @staticmethod
    def _safe(map_like: Optional[dict]) -> dict:
        return map_like or {}

    def _tabs_root(self, tree: dict) -> Optional[dict]:
        if isinstance(tree, dict) and "tabs" in tree and isinstance(tree["tabs"], dict):
            return tree
        return None

    def _lookup_name_and_leaf(self, tabs_root: dict, tab_name: str, owner: str, mode: str, dataset: str):
        jobs = self._safe(self._safe(self._safe(tabs_root.get("tabs")).get(tab_name)).get("jobs"))
        # try exact owner/mode first
        name_map = self._safe(jobs.get(owner, {}).get(mode) or jobs.get(owner, {}).get("live", {}))
        if isinstance(name_map, dict) and dataset in name_map:
            leaf = self._safe(self._safe(name_map.get(dataset)).get("status"))
            return dataset, {"counts": self._safe(leaf.get("counts")), "chunks": list(self._safe(leaf.get("chunks")))}
        # fallback: search other owners/modes for same dataset key
        for o_map in jobs.values():
            for m_map in self._safe(o_map).values():
                if dataset in self._safe(m_map):
                    node = self._safe(m_map.get(dataset))
                    leaf = self._safe(node.get("status"))
                    return dataset, {"counts": self._safe(leaf.get("counts")), "chunks": list(self._safe(leaf.get("chunks")))}
        return None, {"counts": {}, "chunks": []}

    def _noun_for_tab(self, section_tab: str) -> str:
        t = (section_tab or "").lower()
        return {
            "data": "datasets",
            "features": "features",
            "alphas": "alphas",
            "strategies": "strategies",
        }.get(t, "items")


    def _build_section_table(
        self,
        section_tab: str,
        entries_sorted: List[Tuple[int, str, str, str, dict]],
        gpr: int,
        chunks_per_line: int,
        state: dict,
        vis_stages: List[str],
        is_data: bool = False,
        *,
        heading: Optional[str] = None,
        total_count: Optional[int] = None,
        current_page: Optional[int] = None,   # 0-indexed
        rows_per_page: Optional[int] = None,
        total_pages: Optional[int] = None,
    ):
        # ----- header row -----
        head_cells = []
        if is_data:
            per_group = [html.Th("Name", style={"whiteSpace": "nowrap"})] + [
                html.Th(s.title(), style={"whiteSpace": "nowrap"}) for s in vis_stages
            ]
        else:
            per_group = [
                html.Th("Name", style={"whiteSpace": "nowrap"}),
                html.Th("Status", style={"whiteSpace": "nowrap"}),
            ]
        for _ in range(gpr):
            head_cells.extend(per_group)
        head = html.Thead(html.Tr(head_cells))

        # ----- body rows -----
        def _chunked(lst: List, n: int) -> List[List]:
            return [lst[i:i + n] for i in range(0, len(lst), n)]

        body_rows: List[html.Tr] = []
        for row_groups in _chunked(entries_sorted, gpr):
            tds: List[html.Td] = []
            for _, own, md, dn, d_map in row_groups:
                if is_data:
                    stage_stat = {stg: best_status(self._safe(self._safe(d_map.get(stg)).get("counts")), "data") for stg in vis_stages}
                    cells = [html.Td(dn, style={"fontWeight": "600", "whiteSpace": "nowrap"})]
                    for stg in vis_stages:
                        leaf = self._safe(d_map.get(stg))
                        cells.append(
                            html.Td(
                                self._chunk_block("data", list(self._safe(leaf.get("chunks"))), chunks_per_line, prefix="c"),
                                style={
                                    "verticalAlign": "top",
                                    "padding": "6px 10px",
                                    "whiteSpace": "nowrap",
                                    **self._shade("data", stage_stat.get(stg), 0.18),
                                },
                            )
                        )
                    tds.extend(cells)
                else:
                    nm, leaf = self._lookup_name_and_leaf(self._tabs_root(state), section_tab, own, md, dn)
                    bs = best_status(self._safe(leaf.get("counts")), section_tab)
                    cells = [html.Td(nm or "—", style={"fontWeight": "600", "whiteSpace": "nowrap"})]
                    cells.append(
                        html.Td(
                            self._chunk_block(section_tab, list(self._safe(leaf.get("chunks"))), chunks_per_line, prefix=self._prefix_for_tab(section_tab)),
                            style={
                                "verticalAlign": "top",
                                "padding": "6px 10px",
                                "whiteSpace": "nowrap",
                                **self._shade(section_tab, bs, 0.18),
                            },
                        )
                    )
                    tds.extend(cells)
            body_rows.append(html.Tr(tds))

        if not body_rows:
            return None  # Don't render empty tables

        # ----- per-table caption (title) -----
        noun = self._noun_for_tab(section_tab)
        title_txt: Optional[str] = None
        if total_count is not None and current_page is not None and rows_per_page is not None and total_pages is not None:
            if total_count == 0:
                title_txt = f"{heading or section_tab.title()}: 0 {noun}"
            else:
                start_idx = current_page * max(1, rows_per_page)
                shown = len(entries_sorted)
                start_disp = start_idx + 1
                end_disp = min(start_idx + shown, total_count)
                title_txt = f"{heading or section_tab.title()}: Showing {start_disp}-{end_disp} of {total_count} {noun} • Page {current_page + 1} / {max(1, total_pages)}"
        else:
            # Fallback if meta not provided
            title_txt = f"{heading or section_tab.title()}"

        title_el = html.Div(
            title_txt,
            className="fw-bold",
            style={"fontSize": "1.1rem", "marginBottom": "6px"},
        )

        # ----- actual table -----
        table = dbc.Table(
            [head, html.Tbody(body_rows)],
            bordered=True,
            hover=False,
            size="sm",
            className="mb-1",
            style={
                "tableLayout": "auto",
                "width": "auto",
                "display": "inline-table",
                "marginRight": "10ch",
                "overflow": "visible",
            },
        )

        # Wrap so the caption sits just above, and ensure no inner scroll clipping
        return html.Div(
            [title_el, table],
            style={"display": "inline-block", "marginRight": "10ch", "overflow": "visible"},
        )


    def render(
        self,
        tab: str,
        entries_sorted: List[Tuple[int, str, str, str, dict]],
        groups_per_row: int,
        chunks_per_line: int,
        state: dict,
        vis_stages: List[str] = DATA_STAGES,
        entries_by_section: Optional[dict] = None,  # used by "all"
        page_meta: Optional[dict] = None,           # counts/page info for captions
    ):
        gpr = max(1, int(groups_per_row or 2))

        if tab == "all":
            # Expect page_meta = {mode:"all", current_page, rows_per_page, total_pages, totals:{...}}
            pm = page_meta or {}
            cur = int(pm.get("current_page", 0))
            rpp = int(pm.get("rows_per_page", 20))
            tpages = int(pm.get("total_pages", 1))
            totals = pm.get("totals", {}) or {}

            data_entries       = (entries_by_section or {}).get("data",       entries_sorted)
            features_entries   = (entries_by_section or {}).get("features",   entries_sorted)
            alphas_entries     = (entries_by_section or {}).get("alphas",     entries_sorted)
            strategies_entries = (entries_by_section or {}).get("strategies", entries_sorted)

            tables = []

            dt = self._build_section_table(
                "data", data_entries, gpr, chunks_per_line, state, vis_stages, True,
                heading="Data",
                total_count=int(totals.get("data", 0)),
                current_page=cur,
                rows_per_page=rpp,
                total_pages=tpages,
            )
            if dt: tables.append(dt)

            ft = self._build_section_table(
                "features", features_entries, gpr, chunks_per_line, state, [], False,
                heading="Features",
                total_count=int(totals.get("features", 0)),
                current_page=cur,
                rows_per_page=rpp,
                total_pages=tpages,
            )
            if ft: tables.append(ft)

            at = self._build_section_table(
                "alphas", alphas_entries, gpr, chunks_per_line, state, [], False,
                heading="Alphas",
                total_count=int(totals.get("alphas", 0)),
                current_page=cur,
                rows_per_page=rpp,
                total_pages=tpages,
            )
            if at: tables.append(at)

            st = self._build_section_table(
                "strategies", strategies_entries, gpr, chunks_per_line, state, [], False,
                heading="Strategies",
                total_count=int(totals.get("strategies", 0)),
                current_page=cur,
                rows_per_page=rpp,
                total_pages=tpages,
            )
            if st: tables.append(st)

            # Single horizontal strip; no inner scroll container — page can extend infinitely to the right
            return html.Div(
                tables,
                style={
                    "display": "flex",
                    "flexDirection": "row",
                    "gap": "10ch",
                    "flexWrap": "nowrap",        # single long line
                    "alignItems": "flex-start",
                    "width": "max-content",      # grow beyond viewport; prevents inner scrolling
                    "overflow": "visible",
                },
            )

        else:
            # Single-tab table with caption
            pm = page_meta or {}
            return self._build_section_table(
                tab, entries_sorted, gpr, chunks_per_line, state, vis_stages, (tab == "data"),
                heading=tab.title(),
                total_count=int(pm.get("total_count", len(entries_sorted))),
                current_page=int(pm.get("current_page", 0)),
                rows_per_page=int(pm.get("rows_per_page", max(1, len(entries_sorted)))),
                total_pages=int(pm.get("total_pages", 1)),
            )

    def _prefix_for_tab(self, tab: str) -> str:
        return {"data": "c", "features": "f", "alphas": "a", "strategies": "s"}.get((tab or "").lower(), "c")