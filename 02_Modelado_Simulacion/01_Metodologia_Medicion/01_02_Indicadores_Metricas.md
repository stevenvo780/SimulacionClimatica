# 01_02 Indicadores y Métricas: El Dashboard Blindado

Para que la métrica C1-C5 sea incontestable, definimos las fórmulas exactas de validación.

## 1. Índice de Degradación de Emergencia (EDI)
Mide cuánto dependemos del "Cerebro Macro".
*   **Fórmula:** `EDI = (RMSE_reducido - RMSE_hibrido) / RMSE_reducido`
*   **Significado:** Si el EDI es 0.45 (como en nuestro Caso Clima), significa que el 45% de nuestra precisión viene de entender el sistema como un todo. **Si el EDI < 0.30, la Hipótesis H1 se marca como "No Probada".**

## 2. Ratio de Cohesión de Symploke (CR)
Define el límite del sistema.
*   **Fórmula:** `CR = Conectividad_Interna / Interferencia_Externa`
*   **Significado:** Si CR = 2.5, el sistema es una entidad sólida. Si CR < 1.0, el sistema es solo ruido de fondo y no existe como Hiperobjeto.

## 3. Protocolo Cross-Validation (Real vs Sintético)
Para evitar la "lógica circular", la **Fase Sintética** solo se usa para definir el `Basal Error`. La validación ontológica real solo ocurre en la **Fase Real** con datos `Out-of-sample` (datos que el modelo nunca vio durante la calibración).
