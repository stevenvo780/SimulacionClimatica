import os
from datetime import datetime

import pandas as pd
from meteostat import Stations, Monthly


def _conus_bounds():
    # Continental US approximate bounds
    return (24.0, -125.0, 49.5, -66.5)


def _select_stations(start, end, max_stations):
    lat_min, lon_min, lat_max, lon_max = _conus_bounds()
    top_left = (lat_max, lon_min)
    bottom_right = (lat_min, lon_max)
    stations = Stations().bounds(top_left, bottom_right)
    stations = stations.fetch(500)

    # Prefer stations with monthly coverage across the period
    def coverage_score(row):
        m_start = row.get("monthly_start")
        m_end = row.get("monthly_end")
        if pd.isna(m_start) or pd.isna(m_end):
            return 0
        overlap_start = max(m_start, start)
        overlap_end = min(m_end, end)
        if overlap_end < overlap_start:
            return 0
        months = (overlap_end.year - overlap_start.year) * 12 + (overlap_end.month - overlap_start.month) + 1
        total = (end.year - start.year) * 12 + (end.month - start.month) + 1
        return months / total

    stations = stations.copy()
    stations["coverage"] = stations.apply(coverage_score, axis=1)
    stations = stations.sort_values("coverage", ascending=False)
    stations = stations[stations["coverage"] > 0.85]
    return stations.head(max_stations)


def fetch_regional_monthly(start_date, end_date, max_stations=10, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    stations = _select_stations(start, end, max_stations)
    if stations.empty:
        raise RuntimeError("No stations with sufficient coverage found in CONUS bounds")

    series_list = []
    for station_id in stations.index.tolist():
        data = Monthly(station_id, start, end).fetch()
        if data is None or data.empty:
            continue
        if "tavg" not in data.columns:
            continue
        s = data["tavg"].dropna()
        s = s.rename(station_id)
        series_list.append(s)

    if not series_list:
        raise RuntimeError("No station data available for selected period")

    combined = pd.concat(series_list, axis=1)
    coverage = combined.notna().mean()
    top = coverage.sort_values(ascending=False).head(max_stations).index.tolist()
    combined = combined[top]

    regional = combined.mean(axis=1).dropna()
    df = regional.reset_index().rename(columns={"time": "date", 0: "tavg", "tavg": "tavg"})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df
