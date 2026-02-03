# Caso Clima Regional (Modelo y Simulacion)

Este caso implementa dos modelos no isomorfos para dinamica climatica regional:
- Modelo micro (ABM/lattice) con interaccion local y acople macro.
- Modelo macro (ODE/energy-balance agregado) con forcing exogeno.

El objetivo es cumplir criterios del marco 00/01/02:
- Capas completas (conceptual, formal, computacional, validacion).
- Modelos alternativos no isomorfos.
- Reglas de aceptacion y C1-C5.

## Estructura
- `docs/arquitectura.md`: capas y supuestos.
- `docs/protocolo_simulacion.md`: protocolo y criterio de paro.
- `docs/indicadores_metricas.md`: indicadores, metricas y reglas.
- `docs/validacion_c1_c5.md`: validacion operativa.
- `src/`: implementacion.
- `outputs/`: reportes de corrida.

## Como correr

```bash
python3 src/validate.py
```

Genera:
- `outputs/metrics.json`
- `outputs/report.md`

## Datos reales
Este caso usa datos reales regionales (Meteostat, CONUS) en el periodo 1990-2024.
El script cachea los datos en `data/regional_monthly_tavg.csv`.

## Validacion
- Split entrenamiento/validacion: 1990-2010 / 2011-2024.
- Nudging con observacion rezagada (t-1) para evaluacion de corto plazo.
