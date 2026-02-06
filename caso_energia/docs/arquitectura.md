# Arquitectura de Modelos (Capas)

## Conceptual
- Hiperobjeto: demanda electrica agregada persistente con shocks externos.
- Mecanismo: difusion local + forcing externo (clima, actividad economica).
- Delimitacion: serie nacional de demanda como proxy del sistema.

## Formal
- Estado micro por celda: demanda local `D`.
- Dinamica micro: difusion local + forcing + ruido.
- Estado macro: demanda agregada `E`.
- Dinamica macro: ODE de balance agregado.
- Variable puente: `E` acopla al micro y el micro alimenta `E`.

## Computacional
- Modelo micro: lattice 2D de agentes.
- Modelo macro: ODE discreta de balance agregado.
- Simulacion: pasos mensuales con semillas controladas.

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
