# Arquitectura: Crisis Logística y Efecto Látigo

## 1. Concepto: El Hiperobjeto "Retraso"
Este caso estudia cómo el tiempo (delay) se convierte en una fuerza física.
- **Hipótesis:** En redes con capacidad finita y retrasos de información, la búsqueda de equilibrio local genera caos global (Efecto Látigo).

## 2. Formalización (DDE + Colas)
### Macro (DDE - Delay Differential Equation)
A diferencia de la ODE estándar, el estado futuro depende de un estado pasado $t - 	au$.
$$ \frac{dP}{dt} = \alpha (D(t) - S(t-	au)) - \beta P(t) $$
Donde $P$ es el precio del flete, $D$ demanda, $S$ suministro retrasado.

### Micro (Red de Colas)
- **Agentes:** Nodos (Minorista $	o$ Mayorista $	o$ Fábrica).
- **Estado:** Inventario $I$ y Pedidos en Curso $O$.
- **Regla:** Política de pedido $(S, s)$ con pánico. Si $I < s$, pedir $S$. Si hay retraso, **pedir doble** (comportamiento de acaparamiento).

## 3. Variable Puente: "Backlog" (Pedidos Pendientes)
El acumulado de pedidos no satisfechos en el Micro se convierte en la "Presión de Demanda" en el Macro.

## 4. Validación
Contrastaremos la "Presión Simulada" contra el precio de la acción **ZIM** (proxy de tarifas de contenedores) durante 2020-2024.
