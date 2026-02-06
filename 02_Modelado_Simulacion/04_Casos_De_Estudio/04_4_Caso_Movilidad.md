# 04_4 Caso de Estudio: Movilidad Urbana (Ejecutado)

## Contexto
- Fenomeno: movilidad urbana persistente con shocks externos.
- Justificacion: evidencia distribuida y patrones recurrentes.

## Datos
- Fase sintetica: serie controlada 2000-2019 con forcing estacional + tendencia.
- Fase real: MTA Subway Daily Ridership (agregado mensual), 2020-2024.
- Archivos de resultados: `02_Modelado_Simulacion/caso_movilidad/report.md` y `02_Modelado_Simulacion/caso_movilidad/metrics.json`.

## Modelado
- Modelo micro: ABM lattice 2D con contagio local y acople macro.
- Modelo macro: ODE de balance agregado para flujo.
- Variable puente: `M` (flujo agregado) acopla micro y macro.

## Resultados
- Fase sintetica: `overall_pass = True`.
- Fase real: `overall_pass = True`.
- Convergencia en ambas fases bajo umbral con piso de sigma.
- Symploke interna > externa, no-localidad funcional y persistencia verificadas.
- Emergencia: el modelo reducido degrada el error por encima del umbral.

## Criterio de aceptacion
- Cumplimiento C1-C5 y reglas de indicadores en ambas fases.

## Limites y criterio de paro
- Limites: serie corta y shocks exogenos fuertes (pandemia).
- Criterio de paro: estabilidad de patrones y costo marginal > beneficio.
