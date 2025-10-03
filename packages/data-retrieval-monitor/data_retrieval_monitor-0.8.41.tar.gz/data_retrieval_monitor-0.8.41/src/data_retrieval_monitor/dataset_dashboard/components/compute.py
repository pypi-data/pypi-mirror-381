from __future__ import annotations
from typing import Dict, List, Tuple, Optional
from ..constants import status_scores_for_tab, status_order_for_tab, DATA_STAGES

def best_status(counts: Dict[str,int], tab: str) -> Optional[str]:
    scores = status_scores_for_tab(tab)
    best = None
    best_s = -10**9
    for k,v in counts.items():
        s = scores.get(k, -0.2)
        if v>0 and s>best_s: best_s, best = s, k
    return best

def chunk_avg_score_for_leaf(leaf: Dict, tab: str) -> float:
    scores = status_scores_for_tab(tab)
    chunks = list(leaf.get("chunks") or [])
    if not chunks: return 0.0
    tot = 0.0; n=0
    for ch in chunks:
        st = (ch.get("status") or "other")
        tot += float(scores.get(st, -0.2)); n += 1
    return (tot / max(1,n))

def make_sort_key(tab: str, d_map: Dict, dn: str, own: str, sel_stages: List[str], sort_by: str):
    t = (tab or "data").lower()
    if sort_by == "name_asc":
        return (dn.lower(),)
    elif sort_by in ("chunk_asc", "chunk_desc"):
        if t == "data":
            vals = [chunk_avg_score_for_leaf(d_map.get(stg,{}), "data") for stg in sel_stages]
            avg = sum(vals)/max(1,len(vals))
        else:
            avg = chunk_avg_score_for_leaf(d_map.get("status",{}), t)
        return ((avg if sort_by=="chunk_asc" else -avg), dn.lower())
    else:
        return (dn.lower(),)

def aggregate_counts(state: Dict, tab: str) -> Dict[str,int]:
    tabs = state.get("tabs", {})
    tree = tabs.get(tab, {})
    out: Dict[str,int] = {}
    jobs = tree.get("jobs", {}) or {}
    if tab == "data":
        for o_map in jobs.values():
            for m_map in o_map.values():
                for d_map in m_map.values():
                    for stg in DATA_STAGES:
                        leaf = d_map.get(stg, {})
                        for k,v in (leaf.get("counts") or {}).items():
                            out[k] = out.get(k, 0) + int(v or 0)
    else:
        for o_map in jobs.values():
            for m_map in o_map.values():
                for d_map in m_map.values():
                    leaf = d_map.get("status", {})
                    for k,v in (leaf.get("counts") or {}).items():
                        out[k] = out.get(k, 0) + int(v or 0)
    return out

def filtered_stage_counts(state: Dict, owner_sel: Optional[str], stage: str, tab: str = "data") -> Dict[str,int]:
    tabs = state.get("tabs", {})
    tree = tabs.get("data", {})
    out: Dict[str,int] = {}
    want_owner = None if str(owner_sel or "All").lower() in ("all","") else str(owner_sel).lower()
    for own, o_map in (tree.get("jobs") or {}).items():
        if want_owner and own != want_owner: continue
        for m_map in o_map.values():
            for d_map in m_map.values():
                leaf = d_map.get(stage, {})
                for k,v in (leaf.get("counts") or {}).items():
                    out[k] = out.get(k, 0) + int(v or 0)
    return out

def filtered_sorted_entries(
    state: Dict,
    owner_sel: Optional[str],
    sel_stages: List[str],
    status_filter: List[str],
    tab: str,
    sort_by: str
) -> List[Tuple[int, str, str, str, Dict]]:
    entries: List[Tuple[str, str, str, Dict]] = []
    want_owner = None if str(owner_sel or "All").lower() == "all" else str(owner_sel).lower()
    status_set = set(status_filter)
    use_filter = bool(status_set)
    tab_sub = "data" if tab == "all" else tab
    tree = state.get("tabs", {}).get(tab_sub, {})
    jobs = tree.get("jobs", {})
    
    for own in sorted(jobs.keys()):
        if want_owner and own != want_owner:
            continue
        o_map = jobs[own]
        for md in sorted(o_map.keys()):
            m_map = o_map[md]
            for dn in sorted(m_map.keys()):
                d_map = m_map[dn]
                if use_filter:
                    include = False
                    if tab_sub == "data":
                        check_stages = sel_stages if sel_stages else DATA_STAGES
                        if tab == "all":
                            check_stages = DATA_STAGES  # Ignore sel_stages for filtering in "all"
                        for stg in check_stages:
                            leaf = d_map.get(stg, {})
                            for ch in leaf.get("chunks", []):
                                st = ch.get("status") or "other"
                                if st in status_set:
                                    include = True
                                    break
                            if include:
                                break
                    else:
                        leaf = d_map.get("status", {})
                        for ch in leaf.get("chunks", []):
                            st = ch.get("status") or "other"
                            if st in status_set:
                                include = True
                                break
                    if not include:
                        continue
                entries.append((own, md, dn, d_map))
    
    def sk(e):
        stages_for_sort = sel_stages if sel_stages else DATA_STAGES
        return make_sort_key(tab, e[3], e[2], e[0], stages_for_sort, sort_by)
    
    entries_sorted = sorted(entries, key=sk)
    return [(i, own, md, dn, d_map) for i, (own, md, dn, d_map) in enumerate(entries_sorted)]