# GEMINI.md - Contexto del Proyecto: SimulacionClimatica (Versión Titanio)

Este documento sirve como contexto maestro para la IA. Describe la arquitectura consolidada de la tesis tras la "Reingeniería de Alta Densidad".

## 1. Objetivo de la Tesis
Validar la existencia de **Hiperobjetos** (entidades masivamente distribuidas) mediante pruebas de **Eficacia Causal**.
*   **Hipótesis (H1):** Un hiperobjeto es real si su modelo macroscópico (ODE) reduce la entropía de sus componentes microscópicos (ABM) en >30% (EDI > 0.30).

## 2. Estructura del Repositorio (Consolidada)

### 00_Marco_Conceptual (Fundamentos)
*   `00_00_Marco_Conceptual.md`: Ontología OOO (Morton) y Causalidad (Bunge).
*   `00_01_Presupuestos_Axiomas.md`: Lógica formal del sistema.
*   `00_02_Glosario_Maestro.md`: Definiciones operativas (Aliasing, Nudging).
*   `00_03_Dialectica_Filosofica.md`: Defensa ante críticas (Reduccionismo, Tautología).
*   `00_11_Bibliografia.md`: Las 17 fuentes nucleares (Haken, Shannon, Soros).

### 01_Metodologia_Medicion (Rigor)
*   `01_01_Protocolo_Rigor.md`: Pipeline C1-C5.
*   `01_02_Indicadores_Metricas.md`: Justificación matemática de EDI y CR.
*   `01_03_Validez_y_Riesgos.md`: Niveles de Evidencia (LoE) y límites.

### 02_Modelado_Simulacion (Motor)
*   `02_01_Arquitectura_Hibrida.md`: Implementación de la clase `HybridModel`.
*   `02_02_Protocolo_y_Dialectica.md`: Navaja de Ockham (Híbrido vs Reducido).
*   `02_03_Glosario_Matematico.md`: Fórmulas específicas de simulación.
*   `caso_clima/`: Código fuente Python (Caso Exitoso).
*   `caso_finanzas/`: Código fuente Python (Caso Fallido/Reflexivo).

### 03_Validacion_Praxis (Resultados)
*   `03_01_Evidencia_Empirica.md`: Clima, Energía, Epidemiología (LoE 4-5).
*   `03_02_Evidencia_Prospectiva.md`: Justicia, Estética (LoE 1-2).
*   `03_03_Post_Mortem_y_Falsacion.md`: Análisis del fallo en Finanzas.
*   `03_8_Matriz_Validacion_00_01.md`: Cuadro de mando final.

### 04_Casos_De_Estudio (Detalle)
*   `04_01_Evidencia_Dura.md`: Mecánica de los sistemas físicos.
*   `04_02_Exploraciones_Sociales.md`: Mecánica de los sistemas sociales.
*   `04_03_Fronteras_y_Aliasing.md`: Límites técnicos del modelo.

## 3. Estado de los Modelos
*   **Caso Clima:** VALIDADO (EDI 0.45). Demuestra inercia macro.
*   **Caso Finanzas:** RECHAZADO (EDI 0.05). Demuestra reflexividad y aliasing temporal.

## 4. Instrucciones para la IA
*   Priorizar la **Navaja de Ockham**: Si algo se puede explicar sin la capa macro, se descarta el hiperobjeto.
*   Mantener el **Rigor Académico**: Citar siempre a Haken (Sinergética) o Shannon (Entropía) al hablar de métricas.