# 00_09 Mapa de la Tesis: El Grafo de Dependencias

Esta tesis no es lineal, es un **grafo dirigido** donde cada nodo alimenta al siguiente.

```mermaid
graph TD
    A[00 Marco Conceptual] -->|Define Axiomas| B[01 Metodología]
    B -->|Define Protocolos| C[02 Modelado]
    C -->|Genera Datos| D[03 Validación]
    D -->|Valida Hipótesis| E[04 Casos de Estudio]
    E -->|Refina Axiomas| A
```

*   **Capas 00/01:** El Kernel del sistema (Back-end).
*   **Capas 02/03:** La lógica de negocio y procesamiento.
*   **Capa 04:** La interfaz con la realidad (Front-end/UI).
