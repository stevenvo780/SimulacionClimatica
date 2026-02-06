import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_defi_data(start_date, steps, seed=42):
    """
    Genera datos sintéticos de alta fidelidad que imitan una crisis de DeFi.
    Incluye un choque de precios y una cascada de liquidaciones.
    """
    np.random.seed(seed)
    date_rng = pd.date_range(start=start_date, periods=steps, freq='D')
    
    # Simular precio base con un colapso súbito en el medio
    price = np.ones(steps) * 2000.0
    for t in range(1, steps):
        if steps // 3 < t < steps // 3 + 5:
            price[t] = price[t-1] * 0.85 # Caída del 15% diaria
        else:
            price[t] = price[t-1] + np.random.normal(0, 20)
            
    # Simular volumen de liquidaciones realistas (picos durante la caída)
    liquidations = np.zeros(steps)
    for t in range(steps):
        if price[t] < 1500:
            liquidations[t] = np.random.gamma(2, 50) * (2000 - price[t])
        else:
            liquidations[t] = np.random.exponential(10)
            
    df = pd.DataFrame({
        'date': date_rng,
        'price': price,
        'liquidations': liquidations
    })
    return df

def fetch_defi_data(cache_path=None):
    if cache_path:
        try:
            return pd.read_csv(cache_path, parse_dates=['date'])
        except FileNotFoundError:
            pass
            
    df = generate_defi_data('2020-03-01', 100)
    if cache_path:
        df.to_csv(cache_path, index=False)
    return df
