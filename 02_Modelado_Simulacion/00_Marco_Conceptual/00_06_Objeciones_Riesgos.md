# 00_06 Objeciones y Riesgos: Risk Management del Proyecto

Todo despliegue tiene riesgos. En esta tesis, los gestionamos como si fueran fallos de infraestructura.

| Riesgo | Impacto | Mitigación (Backup Plan) |
| :--- | :--- | :--- |
| **Reificación** | Alta | No decir que el hiperobjeto es "una cosa", sino una "dinámica organizada". |
| **Sobreajuste (Overfitting)** | Crítica | Usar el criterio **C2 (Robustez)**. El modelo debe funcionar en diferentes escenarios. |
| **Falta de Datos** | Media | Usar la **Fase Sintética** para validar la lógica antes de conectar datos reales. |
