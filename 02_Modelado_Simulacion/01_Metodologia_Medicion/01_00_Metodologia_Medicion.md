# 01_00 Metodología de Medición: El Plan de QA

Este capítulo es el manual de **Quality Assurance (QA)** de la tesis. Si el capítulo 00 era el "Qué", este es el "Cómo" lo probamos.

## 1. El Objetivo
Garantizar que los datos que salen de nuestras simulaciones no son basura (`Garbage In, Garbage Out`).

## 2. Los 3 Niveles de Testing
1.  **Unit Tests (Fase Sintética):** Probamos el algoritmo con datos conocidos.
2.  **Integration Tests (Fase Real):** Conectamos el modelo a APIs de datos reales.
3.  **Stress Tests (Criterio C2):** Forzamos los parámetros para ver cuándo se rompe el modelo.
