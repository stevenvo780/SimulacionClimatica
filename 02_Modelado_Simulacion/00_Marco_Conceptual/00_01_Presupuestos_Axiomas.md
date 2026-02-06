# 00_01 Presupuestos y Axiomas: El Setup del Sistema (Versión Blindada)

## 1. Axiomas Operativos con Umbrales Críticos

Para eliminar la subjetividad, este sistema aplica los siguientes `asserts` numéricos:

| Axioma | Propiedad | Umbral de Aceptación (Hard Limit) |
| :--- | :--- | :--- |
| **A3: Emergencia** | Índice de Degradación (EDI) | `EDI > 30%` (Si la pérdida de precisión es menor, no hay emergencia fuerte). |
| **A5: Symploke** | Ratio de Cohesión (CR) | `CR >= 2.0` (La interacción interna debe duplicar a la externa). |
| **A6: Validez (C4)** | Consistencia de Leyes | `Violation_Count == 0` (Cero tolerancia a la violación de leyes físicas/lógicas). |

## 2. Definición de Fallo Estructural
Se considera que la investigación ha refutado la existencia de un Hiperobjeto si el sistema no logra mantener un `EDI > 30%` durante tres ejecuciones con semillas distintas. Esto garantiza que no estamos ante una "ilusión de complejidad".
