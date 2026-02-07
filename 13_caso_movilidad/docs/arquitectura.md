# Arquitectura de Modelos (Capas)

## Conceptual
- Hiperobjeto: movilidad urbana persistente con acoplamientos internos y shocks externos.
- Mecanismo: contagio de flujo local + forcing externo (eventos, restricciones).
- Delimitacion: movilidad metropolitana como sistema agregado.

## Formal
- Estado micro por celda: intensidad de flujo `F`.
- Dinamica micro: difusion local + forcing + ruido.
- Estado macro: flujo agregado `M`.
- Dinamica macro: ODE de balance de demanda/retorno.
- Variable puente: `M` acopla al micro y el micro alimenta `M`.

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
