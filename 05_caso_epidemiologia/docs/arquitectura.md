# Arquitectura de Modelos (Capas)

## Conceptual
- Hiperobjeto: dinamica epidemiologica persistente con shocks externos.
- Mecanismo: contagio local + transicion de estados (S, E, I, R).
- Delimitacion: serie global agregada como proxy del sistema.

## Formal
- Micro: presion de infeccion continua con difusion local y estocasticidad.
- Macro: SEIR con exposicion explicita y parametros agregados.
- Variable puente: incidencia agregada.

## Computacional
- Micro: lattice 2D con reglas SIR estocasticas.
- Macro: ODE SEIR discreta.
- Simulacion: pasos semanales con semillas controladas.

## Validacion
- Convergencia ABM vs ODE sobre datos sinteticos y reales.
- Robustez ante perturbaciones de parametros.
- Replicacion con semillas alternativas.
- Validez interna/constructiva y reporte de incertidumbre.

Regla: si una capa falta, el modelo se invalida.

## Dialectica de modelado
- Representacion vs realidad: el modelo solo se acepta si valida externamente.
- Simplificacion vs complejidad: complejidad solo si mejora ajuste o explicacion.
- Determinismo vs estocasticidad: se usa ruido para reproducir variabilidad.
- Escalabilidad vs interpretabilidad: se prioriza interpretabilidad del modelo base.
