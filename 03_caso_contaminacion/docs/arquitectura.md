# Arquitectura de Modelos (Capas)

## Conceptual
- Hiperobjeto: contaminacion del aire persistente con acoplamientos internos y shocks externos.
- Mecanismo: difusion local + forcing externo (regulacion, actividad economica).
- Delimitacion: serie global promedio como proxy del sistema.

## Formal
- Estado micro por celda: nivel de contaminacion `C`.
- Dinamica micro: difusion local + forcing + ruido.
- Estado macro: concentracion agregada `P`.
- Dinamica macro: ODE de balance de emisiones/atenuacion.
- Variable puente: `P` acopla al micro y el micro alimenta `P`.

## Computacional
- Modelo micro: lattice 2D de agentes.
- Modelo macro: ODE discreta de balance agregado.
- Simulacion: pasos anuales con semillas controladas.

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
