# 01_03 Estándares de Validación: El Linter de Certeza

Este documento actúa como el "Juez" final de la tesis.

## Estándar de Oro (Pass/Fail)
1.  **C1 (Convergencia):** `RMSE < 0.6 * StdDev`. (Puntería mínima).
2.  **C2 (Robustez):** Variación de resultados < 10% ante cambios del 10% en inputs.
3.  **C3 (Determinismo):** `Hash(Result_Seed_A) == Hash(Result_Seed_A_Replay)`.
4.  **C4 (Arquitectura):** El modelo debe ser híbrido. Los modelos "Caja Negra" (IA pura) se aceptan solo como contraste, no como explicación.
5.  **C5 (Honestidad):** El margen de error debe estar declarado y ser estable.

**Nota:** Si un caso de estudio falla UN SOLO estándar, el estatus del Hiperobjeto pasa a ser "Herramienta Provisional" (Ontología Degradada).
