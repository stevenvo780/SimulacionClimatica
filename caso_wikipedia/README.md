# Caso Wikipedia (Atencion y Edicion)

Este caso implementa dos modelos no isomorfos para dinamica de atencion en Wikipedia:
- Modelo micro (ABM/lattice) con contagio local y acople macro.
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
- Fase real: evaluacion final con datos reales (Wikimedia pageviews).
El script cachea los datos reales en `data/wikipedia_pageviews_monthly.csv`.

## Validacion
- Split entrenamiento/validacion sintetica: 2000-2009 / 2010-2019.
- Split entrenamiento/validacion real: 2015-2019 / 2020-2024.
- Nudging con observacion del mismo periodo (t) para evaluacion de corto plazo.
