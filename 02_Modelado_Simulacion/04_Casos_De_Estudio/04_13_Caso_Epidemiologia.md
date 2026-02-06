# 04_13 Caso de Estudio: Epidemiologia (Ejecutado)

## Contexto
- Fenomeno: dinamica de contagio agregada con shocks externos.
- Justificacion: evidencia distribuida y patrones con olas y persistencia.

## Datos
- Fase sintetica: serie controlada 2010-2020 con ruido y forcing.
- Fase real: OWID COVID (World), casos semanales 2020-2023.
- Archivos de resultados: `02_Modelado_Simulacion/caso_epidemiologia/report.md` y `02_Modelado_Simulacion/caso_epidemiologia/metrics.json`.

## Modelado
- Modelo micro: ABM de presion de infeccion continua con difusion local.
- Modelo macro: SEIR ODE agregado con exposicion explicita.
- Variable puente: incidencia semanal.

## Resultados
- Fase sintetica: `overall_pass = True`.
- Fase real: `overall_pass = True`.
- Convergencia en ambas fases bajo umbral `0.6 * sigma`.
- Symploke interna > externa, no-localidad funcional y persistencia verificadas.
- Emergencia: el modelo reducido degrada el error por encima del umbral.

## Criterio de aceptacion
- Cumplimiento C1-C5 y reglas de indicadores en ambas fases.

## Limites y criterio de paro
- Limites: agregacion mundial y periodo 2020-2023.
- Criterio de paro: estabilidad de patrones y costo marginal > beneficio.
