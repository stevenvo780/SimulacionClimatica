import os
from datetime import datetime

import pandas as pd
import requests


def fetch_pm25_worldbank(start_date, end_date, cache_path=None):
    start_year = int(start_date[:4])
    end_year = int(end_date[:4])

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    url = (
        "https://api.worldbank.org/v2/country/WLD/indicator/"
        "EN.ATM.PM25.MC.M3?format=json&per_page=2000"
    )
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    payload = resp.json()
    if not isinstance(payload, list) or len(payload) < 2:
        raise RuntimeError("Unexpected World Bank response")

    rows = []
    for entry in payload[1]:
        year = entry.get("date")
        value = entry.get("value")
        if year is None or value is None:
            continue
        y = int(year)
        if y < start_year or y > end_year:
            continue
        rows.append({"date": f"{y}-01-01", "pm25": float(value)})

    df = pd.DataFrame(rows)
    if df.empty:
        raise RuntimeError("No PM2.5 data available for selected period")
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "pm25"]).sort_values("date")

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df
