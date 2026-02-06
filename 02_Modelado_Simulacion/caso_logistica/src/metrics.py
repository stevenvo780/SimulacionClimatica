import numpy as np

def compute_rmse(obs, sim):
    obs = np.array(obs)
    sim = np.array(sim)
    min_len = min(len(obs), len(sim))
    
    if min_len == 0:
        return 9999.0
        
    obs_slice = obs[:min_len]
    sim_slice = sim[:min_len]
    
    # Manejo de NaNs
    if np.isnan(obs_slice).any() or np.isnan(sim_slice).any():
        return 9999.0
        
    # Evitar división por cero en normalización
    obs_range = np.max(obs_slice) - np.min(obs_slice)
    sim_range = np.max(sim_slice) - np.min(sim_slice)
    
    if obs_range == 0: obs_range = 1e-6
    if sim_range == 0: sim_range = 1e-6
    
    obs_norm = (obs_slice - np.min(obs_slice)) / obs_range
    sim_norm = (sim_slice - np.min(sim_slice)) / sim_range
    
    return np.sqrt(np.mean((obs_norm - sim_norm)**2))

def compute_bullwhip_ratio(demand_signal, order_signal):
    var_demand = np.var(demand_signal)
    var_orders = np.var(order_signal)
    if var_demand == 0: return 0
    return var_orders / var_demand