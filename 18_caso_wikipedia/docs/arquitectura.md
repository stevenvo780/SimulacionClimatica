# Arquitectura de Modelos (Capas)

## Conceptual
- Hiperobjeto: atencion colectiva persistente con acoplamientos internos y shocks externos.
- Mecanismo: contagio local de interes + forcing externo (eventos mediaticos).
- Delimitacion: cluster de articulos de Wikipedia como proxy del sistema.

## Formal
- Estado micro por celda: intensidad de atencion `A`.
- Dinamica micro: difusion local + forcing + ruido.
- Estado macro: atencion agregada `W`.
- Dinamica macro: ODE de balance agregado.
- Variable puente: `W` acopla al micro y el micro alimenta `W`.

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
- Determinismo vs estocasticidad: se usa ruido para reproducir volatilidad de atencion.
- Escalabilidad vs interpretabilidad: se prioriza interpretabilidad del modelo base.
