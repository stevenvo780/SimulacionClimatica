# Reproducibilidad y Versionado

## Versionado
- El codigo vive en el repo y se reporta el commit en `outputs/report.md`.
- Los parametros base y semillas quedan registrados en `outputs/metrics.json`.

## Entorno replicable
- Dependencias en `requirements.txt`.
- Ejecucion unica con `python3 src/validate.py`.

## Sensibilidad
- Se reporta rango de sensibilidad en `outputs/metrics.json`.
- La fase sintetica sirve como verificacion en escenario controlado.
