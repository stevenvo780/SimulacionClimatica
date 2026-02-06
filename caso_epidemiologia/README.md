# Caso Epidemiologia (SIR/SEIR)

Este caso implementa dos modelos no isomorfos para dinamica epidemiologica:
- Modelo micro (ABM de presion de infeccion continua) con difusion local y estocasticidad.
- Modelo macro (SEIR ODE agregado) con exposicion explicita.

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
- Fase real: evaluacion final con datos reales (OWID COVID, World).
El script cachea los datos reales en `data/owid_world_weekly_cases.csv`.

## Validacion
- Split entrenamiento/validacion sintetica: 2010-2016 / 2017-2020.
- Split entrenamiento/validacion real: 2020-2021 / 2022-2023.
- Nudging con observacion del mismo periodo (t) para evaluacion de corto plazo.
