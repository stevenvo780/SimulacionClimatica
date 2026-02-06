# 00_07 Edge Cases y Decisiones: El Log de Arquitectura

Aquí registramos las decisiones de diseño tomadas durante el desarrollo de la tesis (Architecture Decision Records - ADR).

## ADR #1: Uso de Modelos Híbridos
*   **Contexto:** Los modelos simples (sólo ODE) no capturan el caos. Los modelos sólo micro (ABM) son computacionalmente caros y divergen.
*   **Decisión:** Usar un patrón de **Acoplamiento Bidireccional**.
*   **Consecuencia:** Mayor precisión pero requiere una calibración cuidadosa del "Nudging".

## ADR #2: Criterio C1-C5 como Estándar
*   **Contexto:** Necesitábamos un "Linter" para validar si un caso de estudio es válido o no.
*   **Decisión:** Crear la pentalogía C1-C5.
