# Caso Movilidad Urbana (Modelo y Simulacion)

Este caso implementa dos modelos no isomorfos para dinamica de movilidad urbana:
- Modelo micro (ABM/lattice) con agentes de flujo local y acople macro.
- Modelo macro (ODE agregado) con forzamiento externo.

El objetivo es cumplir criterios del marco 00/01/02:
- Capas completas (conceptual, formal, computacional, validacion).
- Modelos alternativos no isomorfos.
- Reglas de aceptacion y C1-C5.

## Estructura
- `docs/arquitectura.md`: capas y supuestos.
- `docs/protocolo_simulacion.md`: protocolo y criterio de paro.
- `docs/indicadores_metricas.md`: indicadores, metricas y reglas.
- `docs/validacion_c1_c5.md`: validacion operativa.
- `docs/reproducibilidad.md`: versionado, entorno y sensibilidad.
- `src/`: implementacion.
- `outputs/`: reportes de corrida.

## Como correr

```bash
pip install -r requirements.txt
python3 src/validate.py
```

Genera:
- `outputs/metrics.json`
- `outputs/report.md`

## Datos sinteticos y reales
- Fase sintetica: calibracion y verificacion interna con serie sintetica.
- Fase real: evaluacion final con datos reales (MTA Subway Daily Ridership, 2020-2024).
El script cachea los datos reales en `data/mta_subway_monthly.csv`.

## Validacion
- Split entrenamiento/validacion sintetica: 2000-2009 / 2010-2019.
- Split entrenamiento/validacion real: 2020-2022 / 2023-2024.
- Nudging con observacion rezagada (t-1) para evaluacion de corto plazo.
