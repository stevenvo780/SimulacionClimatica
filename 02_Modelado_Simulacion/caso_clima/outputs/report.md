# Reporte de Validacion - Caso Clima Regional

## Resultado general
- Overall pass: True

## Datos
- start: 1990-01-01
- end: 2024-12-31
- split: 2011-01-01
- steps: 420
- val_steps: 168
- obs_mean: 15.860

## Calibracion
- forcing_scale: 0.050
- macro_coupling: 0.400
- damping: 0.050
- assimilation_strength: 1.000
- ode_alpha: 0.0010
- ode_beta: 0.0010

## Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

## Indicadores
- symploke_pass: True
- non_locality_pass: True
- persistence_pass: True
- persistence_window_variance: 60.861
- obs_window_variance: 59.561
- emergence_pass: True

## Errores
- rmse_abm: 4.268
- rmse_ode: 4.526
- rmse_reduced: 7.872
- rmse_reduced_full: 8.098
- threshold: 4.717

## Notas
- Datos reales regionales (Meteostat, CONUS, 1990-2024).
- Umbrales estrictos definidos en el pipeline.
