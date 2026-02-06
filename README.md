# SimulacionClimatica: Ontología Operativa de Hiperobjetos

> **Tesis Doctoral:** Validación computacional de la existencia de entidades masivamente distribuidas mediante modelos híbridos (ABM + ODE).

Este repositorio contiene la implementación técnica y la fundamentación teórica para demostrar la **Eficacia Causal** de los hiperobjetos (Morton, 2013).

## 🚀 Instalación Rápida

```bash
git clone https://github.com/stevenvo780/SimulacionClimatica.git
cd SimulacionClimatica
pip install -r requirements.txt
```

## 🧪 Experimentos Principales

### 1. Caso Clima (El Éxito)
Modelo validado que demuestra cómo la inercia térmica global "esclaviza" las fluctuaciones locales.
*   **Ejecución:** `python3 02_Modelado_Simulacion/caso_clima/src/validate.py`
*   **Resultado:** EDI 0.45 (Emergencia Fuerte).

### 2. Caso Finanzas (El Rechazo)
Modelo que falla intencionalmente para demostrar los límites de la predicción en sistemas reflexivos (Soros).
*   **Ejecución:** `python3 02_Modelado_Simulacion/caso_finanzas/src/validate.py`
*   **Resultado:** EDI 0.05 (Ruido/Aliasing).

## 📚 Estructura de la Tesis (Versión Consolidada)

La documentación se ha condensado en 5 módulos de alta densidad académica:

*   **00_Marco_Conceptual:** Fundamentos filosóficos (OOO, Sinergética).
*   **01_Metodologia:** Protocolos de rigor C1-C5.
*   **02_Modelado:** Arquitectura del motor `HybridModel`.
*   **03_Validacion:** Matriz de evidencia y análisis de fallos.
*   **04_Casos:** Catálogo detallado de los 12 experimentos.

## ⚖️ Licencia
MIT License. Ver `LICENSE` para más detalles.
