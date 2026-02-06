import os
import pandas as pd
import requests

OWID_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"


def fetch_owid_world_weekly(start_date, end_date, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    resp = requests.get(OWID_URL, timeout=60)
    resp.raise_for_status()

    tmp_path = os.path.join(os.path.dirname(cache_path or "./"), "owid_covid.csv")
    with open(tmp_path, "wb") as f:
        f.write(resp.content)

    df = pd.read_csv(tmp_path, parse_dates=["date"])
    df = df[df["location"] == "World"]
    df = df[["date", "new_cases_smoothed"]].dropna()
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    if df.empty:
        raise RuntimeError("No OWID data for selected period")

    df["week"] = df["date"].dt.to_period("W").dt.start_time
    weekly = df.groupby("week", as_index=False)["new_cases_smoothed"].mean()
    weekly = weekly.rename(columns={"week": "date", "new_cases_smoothed": "cases"})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        weekly.to_csv(cache_path, index=False)

    return weekly
