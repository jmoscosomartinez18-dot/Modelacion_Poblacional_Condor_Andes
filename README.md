# 🦅 Modelación y predicción poblacional del Cóndor de los Andes

---

## 📌 ¿De qué trata el proyecto?
Este proyecto busca analizar, modelar y predecir el comportamiento poblacional del Cóndor de los Andes en Colombia, especie en peligro crítico. Usamos programación, matemáticas y datos para entender su evolución y apoyar su conservación.

---

## 👥 Integrantes y retos
### 🟢 RETO 1 | *JULIÁN*
✅ Modelo matemático (Ecuación Logística)
✅ Método numérico: *Método de Heun*
✅ Simulaciones en 3 escenarios:
   1. Conservación buena
   2. Deforestación / pérdida de hábitat
   3. Caza y envenenamiento
✅ Gráficas y uso de *Pandas* para organizar datos
📂 Archivo: notebooks/julian_reto1.ipynb + scripts/metodos_numericos.py

### 🟡 RETO 2 | *SAMUEL*
✅ Recopilar datos reales de censos (1990 - 2025)
✅ Organizar, limpiar y guardar datos con *Pandas*
✅ Calcular valores iniciales: población, tasa de crecimiento
📂 Archivo: data/datos_poblacion_condor.csv + notebooks/samuel_reto2.ipynb

### 🔴 RETO 3 | *SAID*
✅ Unir todo el trabajo
✅ Análisis comparativo de resultados
✅ Interpretación de gráficas
✅ Conclusiones y recomendaciones de conservación
📂 Archivo: notebooks/said_reto3.ipynb + CONCLUSIONES_FINALES.md

---

## 📐 Modelo matemático
$$\frac{dP}{dt}=rP\left(1-\frac{P}{K}\right)$$
- $P$ = Población
- $r$ = Tasa de crecimiento
- $K$ = Capacidad de carga del ambiente

---

## 📂 Estructura del proyecto