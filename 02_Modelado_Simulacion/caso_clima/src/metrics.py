import math


def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def variance(xs):
    if not xs:
        return 0.0
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)


def rmse(a, b):
    if len(a) != len(b) or not a:
        return 0.0
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)) / len(a))


def correlation(a, b):
    if len(a) != len(b) or len(a) < 2:
        return 0.0
    ma = mean(a)
    mb = mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den_a = math.sqrt(sum((x - ma) ** 2 for x in a))
    den_b = math.sqrt(sum((y - mb) ** 2 for y in b))
    if den_a == 0.0 or den_b == 0.0:
        return 0.0
    return num / (den_a * den_b)


def window_variance(xs, window):
    if len(xs) < window:
        return variance(xs)
    tail = xs[-window:]
    return variance(tail)


def internal_vs_external_cohesion(grid_series, forcing_series):
    # Compute average correlation of each cell with neighbor mean (internal)
    # and with forcing (external).
    steps = len(grid_series)
    if steps == 0:
        return 0.0, 0.0
    n = len(grid_series[0])

    internal_corrs = []
    external_corrs = []
    for i in range(n):
        for j in range(n):
            cell_series = [grid_series[t][i][j] for t in range(steps)]
            neighbor_series = []
            for t in range(steps):
                neighbors = []
                if i > 0:
                    neighbors.append(grid_series[t][i - 1][j])
                if i < n - 1:
                    neighbors.append(grid_series[t][i + 1][j])
                if j > 0:
                    neighbors.append(grid_series[t][i][j - 1])
                if j < n - 1:
                    neighbors.append(grid_series[t][i][j + 1])
                neighbor_series.append(sum(neighbors) / len(neighbors))

            internal_corrs.append(correlation(cell_series, neighbor_series))
            external_corrs.append(correlation(cell_series, forcing_series))

    internal = mean(internal_corrs)
    external = mean(external_corrs)
    return internal, external


def dominance_share(grid_series):
    # Proxy for non-locality: max share of correlation with regional mean.
    steps = len(grid_series)
    if steps == 0:
        return 1.0
    n = len(grid_series[0])
    regional = []
    for t in range(steps):
        total = 0.0
        for i in range(n):
            total += sum(grid_series[t][i])
        regional.append(total / (n * n))

    scores = []
    for i in range(n):
        for j in range(n):
            cell_series = [grid_series[t][i][j] for t in range(steps)]
            scores.append(abs(correlation(cell_series, regional)))

    total = sum(scores) if scores else 1.0
    max_share = max(scores) / total if scores else 1.0
    return max_share


def effective_information(series_macro, series_micro_agg, bins=5):
    """
    Calcula la Información Efectiva (EI = Determinismo - Degeneración)
    basado en el marco de Erik Hoel.
    """
    import numpy as np

    def get_tpm(data, bins):
        # Discretizar la serie en 'bins' estados
        v_min, v_max = min(data), max(data)
        if v_min == v_max: return np.eye(bins)
        
        digits = np.digitize(data, np.linspace(v_min, v_max, bins)) - 1
        tpm = np.zeros((bins, bins))
        for t in range(len(digits) - 1):
            tpm[digits[t], digits[t+1]] += 1
        
        # Normalizar filas para obtener probabilidades de transición
        row_sums = tpm.sum(axis=1)
        for i in range(bins):
            if row_sums[i] > 0:
                tpm[i] /= row_sums[i]
            else:
                tpm[i] = np.ones(bins) / bins # Estado de máxima incertidumbre
        return tpm

    def calculate_ei(tpm):
        # Determinismo: cuán predecible es el futuro dado el presente (entropía de filas)
        # Degeneración: cuán solapados están los pasados dado el futuro (entropía de columnas)
        bins = tpm.shape[0]
        # H(W_out | do(W_in))
        row_entropies = []
        for i in range(bins):
            p = tpm[i]
            p = p[p > 0]
            row_entropies.append(-np.sum(p * np.log2(p)))
        
        determinism = 1 - (np.mean(row_entropies) / np.log2(bins))
        
        # Degeneración (basada en la especificidad de las columnas)
        avg_tpm = tpm.mean(axis=0)
        avg_tpm = avg_tpm[avg_tpm > 0]
        degeneracy = 1 - (-np.sum(avg_tpm * np.log2(avg_tpm)) / np.log2(bins))
        
        return max(0.0, determinism - (1 - degeneracy))

    ei_macro = calculate_ei(get_tpm(series_macro, bins))
    ei_micro = calculate_ei(get_tpm(series_micro_agg, bins))
    
    # La Causal Emergence ocurre si EI_macro > EI_micro
    return float(ei_macro - ei_micro)


def stationarity_index(series):
    if len(series) < 2:
        return 0.0
    return correlation(series[:-1], series[1:])
