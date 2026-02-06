# 00_02 Glosario Maestro: El SDK de la Tesis

Este es el Diccionario de Datos del proyecto. Considera estos términos como los nombres de las clases principales de nuestro framework de investigación.

---

## [Class] Hiperobjeto
Sistemas distribuidos masivamente que superan la percepción humana directa.
*   **Propiedades:**
    *   `.is_local = False` (Está en todas partes).
    *   `.persistence = High` (Dura más que la ejecución del observador).
    *   `.emergence = Strong` (Produce efectos que no están en el código de sus partes).
*   **Ejemplos:** `class Climate`, `class GlobalEconomy`.

## [Function] Symploke()
Algoritmo de delimitación de fronteras. Determina qué pertenece al sistema y qué es ruido externo.
*   **Input:** `data_stream_A`, `data_stream_B`.
*   **Logic:** Compara si el acoplamiento interno es mayor que las interferencias externas.
*   **Return:** `Boolean` (True si el sistema es cohesivo).

## [Pattern] Nudging / Asimilación
Patrón de diseño para mantener la sincronía entre dos procesos (Macro y Micro).
*   **Propósito:** Evita que la simulación de baja escala se desvíe de la realidad observada en alta escala.
*   **Mecánica:** Es como un `git pull --rebase` constante de los datos reales hacia el modelo.

## [Variable] C1-C5
Array de validación obligatoria. Si alguna posición es `False`, el modelo no se despliega (no se considera válido).
*   **C1:** Convergencia (Unit Test).
*   **C2:** Robustez (Stress Test).
*   **C3:** Replicación (Determinismo).
*   **C4:** Validez (Lógica de Negocio).
*   **C5:** Incertidumbre (Logging de Error).

## [Concept] Inferencia a la Mejor Explicación (IME)
Es nuestro buscador de "Root Cause". Si el modelo híbrido es la explicación más simple que no pierde datos, lo aceptamos como verdadero.
