import os
from datetime import datetime

import numpy as np
import pandas as pd


def fetch_mta_subway_monthly(start_date, end_date, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    url = (
        "https://data.ny.gov/resource/vxuj-8kew.csv"
        "?$select=date,subways_total_estimated_ridership"
        "&$order=date"
        "&$limit=50000"
    )
    df = pd.read_csv(url)
    if df.empty:
        raise RuntimeError("No MTA ridership data returned")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.dropna(subset=["date", "subways_total_estimated_ridership"])
    df = df[(df["date"] >= start) & (df["date"] <= end)]

    df["ridership"] = df["subways_total_estimated_ridership"].astype(float)
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()
    monthly = df.groupby("month", as_index=False)["ridership"].sum()

    monthly["log_ridership"] = monthly["ridership"].apply(lambda x: float(np.log(max(x, 1.0))))
    out = monthly[["month", "log_ridership"]].rename(columns={"month": "date", "log_ridership": "mobility"})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        out.to_csv(cache_path, index=False)

    return out
