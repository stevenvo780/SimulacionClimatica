import os
import time
from datetime import datetime

import pandas as pd
import requests

API_BASE = "https://api.openalex.org"
DEFAULT_UA = "SimulacionClimatica/0.1 (mailto:contacto@simulacion.local)"


def _user_agent():
    return os.getenv("OPENALEX_USER_AGENT", DEFAULT_UA)


def _request(url, params=None):
    headers = {"User-Agent": _user_agent()}
    resp = requests.get(url, params=params, headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json()


def _search_concept(term):
    data = _request(f"{API_BASE}/concepts", params={"search": term, "per_page": 1})
    results = data.get("results", [])
    if not results:
        return None, None
    concept = results[0]
    return concept.get("id"), concept.get("display_name")


def _find_concept(terms):
    for term in terms:
        cid, name = _search_concept(term)
        if cid:
            return cid, name, term
        time.sleep(0.2)
    return None, None, None


def _counts_by_year(concept_id):
    data = _request(
        f"{API_BASE}/works",
        params={
            "filter": f"concepts.id:{concept_id}",
            "group_by": "publication_year",
            "per_page": 200,
        },
    )
    groups = data.get("group_by", [])
    counts = {}
    for entry in groups:
        year = entry.get("key")
        count = entry.get("count")
        if year is None or count is None:
            continue
        counts[int(year)] = int(count)
    return counts


def fetch_openalex_paradigms(cache_path, start_year=1950, end_year=2023, refresh=False):
    cache_path = os.path.abspath(cache_path)
    if os.path.exists(cache_path) and not refresh:
        df = pd.read_csv(cache_path)
        df["date"] = pd.to_datetime(df["date"])
        meta = {
            "source": "OpenAlex",
            "concepts": {},
            "cached": True,
            "start_year": int(df["year"].min()),
            "end_year": int(df["year"].max()),
        }
        return df, meta

    quantum_terms = ["quantum mechanics", "quantum theory"]
    classical_terms = ["classical mechanics", "classical physics"]

    q_id, q_name, q_term = _find_concept(quantum_terms)
    c_id, c_name, c_term = _find_concept(classical_terms)
    if not q_id or not c_id:
        raise RuntimeError("No se pudieron resolver conceptos en OpenAlex")

    q_counts = _counts_by_year(q_id)
    time.sleep(0.2)
    c_counts = _counts_by_year(c_id)

    years = list(range(start_year, end_year + 1))
    rows = []
    for year in years:
        q = q_counts.get(year, 0)
        c = c_counts.get(year, 0)
        total = q + c
        share = q / total if total > 0 else 0.0
        rows.append(
            {
                "year": year,
                "date": datetime(year, 1, 1),
                "quantum": q,
                "classical": c,
                "share": share,
            }
        )

    df = pd.DataFrame(rows)
    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    df.to_csv(cache_path, index=False)

    meta = {
        "source": "OpenAlex",
        "concepts": {
            "quantum": {"id": q_id, "name": q_name, "term": q_term},
            "classical": {"id": c_id, "name": c_name, "term": c_term},
        },
        "cached": False,
        "start_year": start_year,
        "end_year": end_year,
    }
    return df, meta
