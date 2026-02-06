# Arquitectura de Modelos (Capas)

## Conceptual
- Hiperobjeto: clima regional persistente con no-localidad funcional.
- Mecanismo: acoples internos (transporte local de energia y humedad) + forcing externo (CO2).
- Delimitacion: frontera funcional basada en cohesion interna vs externa.

## Formal
- Estado micro por celda: temperatura `T`, humedad `H`.
- Dinamica micro: difusion local + forzamiento externo + ruido.
- Estado macro: temperatura regional media `T_bar`.
- Dinamica macro: balance energetico agregado con forcing `F`.
- Variable puente: `T_bar` acopla al micro y el micro alimenta `T_bar`.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta tipo energy-balance.
- Simulacion: pasos discretos con semillas controladas.

## Validacion
- Convergencia ABM vs ODE sobre datos sinteticos.
- Robustez ante perturbaciones de parametros.
- Replicacion en condiciones iniciales alternativas.
- Validez interna/constructiva y reporte de incertidumbre.

Regla: si una capa falta, el modelo se invalida.

## Dialectica de modelado
- Representacion vs realidad: el modelo solo se acepta si valida externamente.
- Simplificacion vs complejidad: complejidad solo si mejora ajuste o explicacion.
- Determinismo vs estocasticidad: se usa ruido para mejorar ajuste empirico.
- Escalabilidad vs interpretabilidad: se prioriza interpretabilidad del modelo base.
