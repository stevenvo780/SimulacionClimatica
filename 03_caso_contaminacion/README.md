# Caso Contaminacion del Aire (PM2.5)

Este caso implementa dos modelos no isomorfos para dinamica de contaminacion:
- Modelo micro (ABM/lattice) con difusion local y acople macro.
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
- Fase real: evaluacion final con datos reales (World Bank, WLD).
El script cachea los datos reales en `data/pm25_world.csv`.

## Validacion
- Split entrenamiento/validacion sintetica: 1980-1999 / 2000-2019.
- Split entrenamiento/validacion real: 1990-2005 / 2006-2022.
- Nudging con observacion rezagada (t-1) para evaluacion de corto plazo.
