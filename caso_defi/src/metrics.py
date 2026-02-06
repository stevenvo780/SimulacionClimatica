import numpy as np

def compute_rmse(obs, sim):
    obs = np.array(obs)
    sim = np.array(sim)
    # Alinear longitudes si es necesario
    min_len = min(len(obs), len(sim))
    return np.sqrt(np.mean((obs[:min_len] - sim[:min_len])**2))

def compute_cascade_metrics(liquidation_series):
    """
    Calcula el tamaño máximo de la cascada y la duración.
    """
    series = np.array(liquidation_series)
    max_peak = np.max(series)
    total_volume = np.sum(series)
    return {
        "max_liquidation_peak": float(max_peak),
        "total_liquidation_volume": float(total_volume)
    }
