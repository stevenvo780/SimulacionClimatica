# Caso Paradigmas Cientificos

Este caso evalua el surgimiento de paradigmas cientificos con dos modelos no isomorfos:
- Modelo micro (ABM de difusion de ideas) con interaccion local y acople macro.
- Modelo macro (ODE agregado) con dinamica de adopcion y forcing externo.

Objetivo:
- Probar limites del marco 00/01 en transiciones de regimen intelectual.
- Validar C1-C5 con fase sintetica y fase real.

## Estructura
- `docs/arquitectura.md`
- `docs/protocolo_simulacion.md`
- `docs/indicadores_metricas.md`
- `docs/validacion_c1_c5.md`
- `docs/reproducibilidad.md`
- `src/` implementacion
- `outputs/` reportes de corrida

## Como correr

```bash
pip install -r requirements.txt
python3 src/validate.py
```

Genera:
- `outputs/metrics.json`
- `outputs/report.md`

## Datos reales
- Fuente: OpenAlex (conteos por anio de conceptos "quantum mechanics" y "classical mechanics").
- Serie: share anual de publicaciones quantum / (quantum + classical).
- Cache: `data/openalex_paradigms.csv`.

Para cambiar el user agent de OpenAlex:
- `export OPENALEX_USER_AGENT="SimulacionClimatica/0.1 (mailto:correo@ejemplo.com)"`

## Validacion
- Fase sintetica: 1950-2023, split 1990.
- Fase real: 1950-2023, split 1990.
- Nudging con observacion del mismo periodo (t) para evaluacion de corto plazo.
