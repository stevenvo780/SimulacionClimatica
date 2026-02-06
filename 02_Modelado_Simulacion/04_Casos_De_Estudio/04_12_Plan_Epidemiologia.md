# 04_12 Plan de Caso: Epidemiologia

## Objetivo
- Ejecutar un caso epidemiologico con dos fases: sintetica (verificacion interna) y real (evaluacion final).

## Fuente de datos reales
- Our World in Data (OWID) COVID.
- Serie semanal de casos para el agregado Mundial.

## Metodologia
- Dos modelos no isomorfos: ABM (micro) + SEIR ODE (macro).
- Variable puente: incidencia semanal.
- Indicadores: symploke, no-localidad, persistencia, emergencia.
- Criterios C1–C5 obligatorios.

## Fases y splits
- Fase sintetica: 2010-2020, split 2017.
- Fase real: 2020-2023, split 2022.

## Entregables
- Reporte reproducible (`report.md`) y metricas (`metrics.json`).
- Validacion en 03 y caso ejecutado en 04.
- Actualizar indices y matriz 00–01.
