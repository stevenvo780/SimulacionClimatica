# 02_03 Glosario Matemático: Fórmulas del Motor

Este documento detalla la implementación algebraica de los conceptos definidos en el Capítulo 00.

## 1. Dinámica Micro (ABM)
### Ecuación de Actualización de Agente
$$ S_{t+1} = S_t + \alpha ( \langle S \rangle_{vecinos} - S_t ) + \beta ( M_t - S_t ) + \epsilon $$
*   $\alpha$: Coeficiente de Difusión (interacción horizontal).
*   $\beta$: Coeficiente de Nudging (interacción vertical/macro).
*   $\epsilon$: Ruido estocástico (Wiener process).

## 2. Dinámica Macro (ODE)
### Ecuación de Balance Agregado
$$ \frac{dM}{dt} = F(t) - \gamma M + \sigma \xi_t $$
*   $F(t)$: Forzamiento externo (ej. radiación solar).
*   $\gamma$: Tasa de disipación/inercia.
*   $\sigma$: Volatilidad sistémica.

## 3. Métricas de Validación
### RMSE (Root Mean Square Error)
$$ RMSE = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2 } $$

### EDI (Emergence Degradation Index)
$$ EDI = \frac{RMSE_{reducido} - RMSE_{hibrido}}{RMSE_{reducido}} $$
*   Si $EDI > 0.30$, se confirma la eficacia causal de $M_t$ sobre $S_t$.
