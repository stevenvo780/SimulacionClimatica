# Arquitectura de Modelos - Cascadas DeFi

## 1. Capa Conceptual
El modelo simula la estabilidad sistémica de un protocolo de préstamos descentralizado. Los agentes (billeteras) mantienen posiciones de deuda garantizadas por colateral volátil. El riesgo emerge cuando la caída del precio macro dispara liquidaciones micro, las cuales alimentan una mayor caída del precio (retroalimentación negativa).

## 2. Capa Formal
- **Micro (Agentes):** Cada agente $i$ tiene colateral $C_i$ y deuda $D_i$. Factor de salud $H_i = (C_i \cdot P) / D_i$.
- **Macro (Mercado):** El precio $P$ sigue una dinámica ODE influenciada por ventas forzosas $S$: $dP/dt = \alpha(F(t) - \beta P) - \lambda S$.
- **Variable Puente:** Presión de venta agregada $S = \sum 	ext{liquidaciones}_i$.

## 3. Capa Computacional
- **Grafo de Contagio:** Los agentes están conectados por "re-hipotecación" o exposición común.
- **Algoritmo:** Iteración discreta donde las liquidaciones de un bloque afectan el precio del siguiente.

## 4. Capa de Validación (C1-C5)
- **C1 (Convergencia):** El sistema debe estabilizarse en ausencia de choques externos.
- **C4 (Predictiva):** Comparación con datos históricos de eventos de liquidación masiva (ej. Black Thursday 2020).
