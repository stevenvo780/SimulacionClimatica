import os
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

def fetch_logistics_data(cache_path=None):
    """
    Descarga datos de ZIM (naviera) como proxy del estrés en la cadena de suministro.
    El precio de la acción correlaciona con el costo de los fletes (Freight Rates).
    """
    if cache_path and os.path.exists(cache_path):
        try:
            return pd.read_csv(cache_path, parse_dates=['date'])
        except:
            pass

    start_date = "2020-01-01"
    end_date = "2024-01-01"
    
    print(f"Descargando datos logísticos (ZIM) de {start_date} a {end_date}...")
    
    ticker = "ZIM"
    try:
        data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    except Exception as e:
        print(f"Error descargando yfinance: {e}")
        data = pd.DataFrame()
    
    if data.empty:
        print("ZIM data empty. Generando datos sintéticos de crisis logística (Curva S).")
        # Generar curva sintética de crisis: Estabilidad -> Pico -> Caída
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        steps = len(dates)
        x = np.linspace(-5, 5, steps)
        # Sigmoide doble (subida y bajada)
        price = 10 + 50 * (1 / (1 + np.exp(-(x + 2)*2))) * (1 / (1 + np.exp((x - 2)*2)))
        # Añadir ruido
        price += np.random.normal(0, 2, steps)
        
        df = pd.DataFrame({'date': dates, 'price': price})
    else:
        df = data.reset_index()
        # Handle MultiIndex columns if present (yfinance update)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
            
        df = df.rename(columns={"Date": "date", "Close": "price"})
        
        if "price" not in df.columns and "Adj Close" in df.columns:
             df = df.rename(columns={"Adj Close": "price"})
             
        df = df[["date", "price"]]
    
    # Normalizar precio (Stress Index 0-100 aprox)
    min_p = df["price"].min()
    max_p = df["price"].max()
    if max_p == min_p: max_p += 1e-6
    
    df["stress_index"] = (df["price"] - min_p) / (max_p - min_p) * 100
    
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
        
    return df