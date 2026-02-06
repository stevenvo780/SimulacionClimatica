# GEMINI.md - Resumen del Proyecto: SimulacionClimatica

Este documento proporciona una visión general del proyecto `SimulacionClimatica`, sirviendo como contexto instructivo para futuras interacciones.

## Resumen del Proyecto General

El proyecto `SimulacionClimatica` es una iniciativa integral de modelado y simulación que abarca múltiples **casos de estudio** o dominios. El objetivo principal es la implementación de **modelos alternativos no isomorfos** para la dinámica de sistemas complejos, adheriéndose a un marco de desarrollo riguroso (marco 00/01/02) que incluye capas completas (conceptual, formal, computacional, validación) y una validación exhaustiva (C1-C5).

Cada caso de estudio dentro del proyecto generalmente implementa:
*   Un **Modelo Basado en Agentes (ABM) a microescala**, a menudo utilizando una estructura de celosía con interacción local y acoplamiento macro.
*   Un **modelo de Ecuación Diferencial Ordinaria (ODE) a macroescala**, basado en balances agregados con forzamiento externo.

El proyecto está desarrollado en **Python** y aprovecha bibliotecas comunes como `numpy` y `pandas` para operaciones numéricas y manipulación de datos, complementadas con librerías específicas para cada dominio (ej. `meteostat` para clima, `yfinance` para finanzas). Procesa tanto datos sintéticos como datos reales específicos de cada dominio.

## Principios y Reglas de Modelado y Simulación

El capítulo "02 Modelado y Simulación" establece los siguientes principios operativos y reglas que rigen la construcción y validación de todos los modelos dentro de este proyecto:

### Principios
*   **Trazabilidad conceptual completa:** Asegurar que los modelos puedan ser rastreados hasta sus axiomas conceptuales.
*   **Modelos multinivel con variables puente:** Integrar modelos de diferentes escalas (micro y macro) mediante variables que acoplan su dinámica.
*   **Validación con C1-C5:** Utilizar un marco de validación riguroso para asegurar la robustez y validez de los modelos.

### Arquitectura
*   Los modelos deben pasar por capas sucesivas: **conceptual -> formal -> computacional -> validación**.
*   **Cierre:** Ninguna de estas capas puede omitirse o ser incompleta para que un modelo sea considerado válido.

### Reglas de Construcción
*   Todo modelo debe tener un **modelo alternativo no isomorfo** para comparación y robustez.
*   Todo resultado de simulación debe estar asociado a una **métrica clara y una regla de aceptación** definida.

### Verificación y Reproducibilidad
*   **Versionado** de código y parámetros para asegurar la replicabilidad.
*   **Entornos replicables** para garantizar que las simulaciones puedan ser reproducidas por otros.
*   **Reportes de sensibilidad** para entender cómo las variaciones en los parámetros afectan los resultados.

## Casos de Estudio Incluidos

### 1. Caso Clima Regional (`02_Modelado_Simulacion/caso_clima/`)

Este caso se enfoca en la dinámica climática regional, implementando modelos micro (ABM/lattice) y macro (ODE/balance energético agregado). Utiliza datos meteorológicos (Meteostat, CONUS).

**Configuración y Ejecución:**
1.  **Instalar Dependencias:**
    ```bash
    pip install -r 02_Modelado_Simulacion/caso_clima/requirements.txt
    ```
2.  **Ejecutar la Simulación:**
    ```bash
    python3 02_Modelado_Simulacion/caso_clima/src/validate.py
    ```
Genera `outputs/metrics.json` y `outputs/report.md`.

### 2. Caso Finanzas Globales (`02_Modelado_Simulacion/caso_finanzas/`)

Este caso modela la dinámica de precios en un índice bursátil, con modelos micro (ABM/agentes de tendencia y fundamentalistas) y macro (ODE agregado). Utiliza datos de mercado reales (ej. SPY a través de `yfinance`).

**Configuración y Ejecución:**
1.  **Instalar Dependencias:**
    ```bash
    pip install -r 02_Modelado_Simulacion/caso_finanzas/requirements.txt
    ```
2.  **Ejecutar la Simulación:**
    ```bash
    python3 02_Modelado_Simulacion/caso_finanzas/src/validate.py
    ```
Genera `outputs/metrics.json` y `outputs/report.md`.

## Estructura de Directorios Relevante

*   `02_Modelado_Simulacion/`: Contiene la base conceptual y los diversos casos de estudio de simulación.
    *   `02_Modelado_Simulacion/*.md`: Documentos que detallan principios generales, arquitectura, protocolos de simulación, etc.
    *   `caso_clima/`: Proyecto específico para la simulación climática.
        *   `src/`: Código fuente principal (programas Python).
        *   `data/`: Datos utilizados por el modelo.
        *   `docs/`: Documentación específica del caso (arquitectura, indicadores, validación).
        *   `outputs/`: Resultados de las simulaciones.
    *   `caso_finanzas/`: Proyecto específico para la simulación financiera, con una estructura idéntica a `caso_clima/`.
        *   `src/`: Código fuente principal (programas Python).
        *   `data/`: Datos utilizados por el modelo.
        *   `docs/`: Documentación específica del caso.
        *   `outputs/`: Resultados de las simulaciones.
