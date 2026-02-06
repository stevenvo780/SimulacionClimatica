# 04_10 Plan de Caso: Energia Electrica

## Objetivo
- Ejecutar un caso de demanda electrica con dos fases: sintetica (verificacion interna) y real (evaluacion final).

## Fuente de datos reales
- Open Power System Data (OPSD) time series.
- Serie mensual agregada de demanda GB.

## Metodologia
- Dos modelos no isomorfos: ABM (micro) + ODE (macro).
- Variable puente: demanda agregada.
- Indicadores: symploke, no-localidad, persistencia, emergencia.
- Criterios C1–C5 obligatorios.

## Fases y splits
- Fase sintetica: 2000-2019, split 2010.
- Fase real: 2015-2020, split 2019.

## Entregables
- Reporte reproducible (`report.md`) y metricas (`metrics.json`).
- Validacion en 03 y caso ejecutado en 04.
- Actualizar indices y matriz 00–01.
