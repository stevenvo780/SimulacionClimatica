import os
from datetime import datetime

import numpy as np
import pandas as pd
import yfinance as yf


def fetch_spy_monthly(start_date, end_date, cache_path=None):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    data = yf.download(
        "SPY",
        start=start.strftime("%Y-%m-%d"),
        end=end.strftime("%Y-%m-%d"),
        interval="1mo",
        auto_adjust=True,
        progress=False,
    )
    if data is None or data.empty:
        raise RuntimeError("No SPY data available for selected period")

    data = data.reset_index()
    data = data.rename(columns={"Date": "date"})
    if "Close" not in data.columns:
        raise RuntimeError("SPY data missing Close column")

    close = data["Close"]
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    data = data[["date"]].copy()
    data["Close"] = close.values
    data = data.dropna()
    data["log_price"] = data["Close"].apply(lambda x: float(np.log(x)))
    df = data[["date", "log_price"]].rename(columns={"log_price": "price"})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df
