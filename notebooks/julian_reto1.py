# ==================================================
# RETO 1 - JULIÁN - MODELACIÓN DEL CÓNDOR DE LOS ANDES
# ==================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----------------------
# FUNCIONES MATEMÁTICAS
# ----------------------

# Modelo Logístico
def modelo_logistico(t, P, r, K):
    return r * P * (1 - P / K)

# Método de Heun
def metodo_heun(funcion, t_inicial, t_final, P_inicial, pasos, r, K):
    h = (t_final - t_inicial) / pasos
    t = np.linspace(t_inicial, t_final, pasos + 1)
    P = np.zeros(pasos + 1)
    P[0] = P_inicial
    for i in range(pasos):
        k1 = funcion(t[i], P[i], r, K)
        P_pred = P[i] + h * k1
        k2 = funcion(t[i+1], P_pred, r, K)
        P[i+1] = P[i] + (h / 2) * (k1 + k2)
    return t, P

# Crear tablas
def crear_tabla(t, P, nombre):
    return pd.DataFrame({
        'Tiempo': t.round(0),
        'Poblacion': P.round(0),
        'Escenario': nombre
    })

# ----------------------
# CARGAR DATOS DE SAMUEL
# ----------------------
datos = pd.read_csv('../data/datos_poblacion_condor.csv')

# ----------------------
# PARÁMETROS DEL MODELO
# ----------------------
r = 0.04
P0 = 63
tiempo = 50
pasos = 50

# ----------------------
# EJECUTAR LOS 3 ESCENARIOS
# ----------------------

# 🟢 ESCENARIO 1: CONSERVACIÓN BUENA
t1, P1 = metodo_heun(modelo_logistico, 0, tiempo, P0, pasos, r, 250)
tabla1 = crear_tabla(t1, P1, "Conservacion Buena")

# 🟠 ESCENARIO 2: DEFORESTACIÓN
t2, P2 = metodo_heun(modelo_logistico, 0, tiempo, P0, pasos, r, 150)
tabla2 = crear_tabla(t2, P2, "Deforestacion")

# 🔴 ESCENARIO 3: CAZA / ENVENENAMIENTO
t3, P3 = metodo_heun(modelo_logistico, 0, tiempo, P0, pasos, 0.015, 200)
tabla3 = crear_tabla(t3, P3, "Caza / Envenenamiento")

# ----------------------
# MOSTRAR RESULTADOS
# ----------------------
print("===== TABLA 1: CONSERVACIÓN =====")
print(tabla1)
print("\n===== TABLA 2: DEFORESTACIÓN =====")
print(tabla2)
print("\n===== TABLA 3: RIESGO =====")
print(tabla3)

# ----------------------
# GRÁFICA FINAL
# ----------------------
plt.figure(figsize=(10,6))
plt.plot(t1, P1, 'g-', linewidth=2, label='Conservación')
plt.plot(t2, P2, 'orange', linewidth=2, label='Deforestación')
plt.plot(t3, P3, 'r-', linewidth=2, label='Caza / Riesgo')
plt.scatter(datos['anio'] - 2025, datos['poblacion'], color='blue', s=50, label='Datos Reales')
plt.title('EVOLUCIÓN DEL CÓNDOR DE LOS ANDES | Modelación Julián')
plt.xlabel('Años desde 2025')
plt.ylabel('Número de Individuos')
plt.legend()
plt.grid(True)
plt.show()

# ==================================================
# 📝 EXPLICACIÓN DEL TRABAJO (LO QUE ENTREGAS)
# ==================================================
"""
1. MODELO MATEMÁTICO:
Usé el Modelo Logístico dP/dt = rP(1-P/K) porque es el ideal para especies que tienen un límite de espacio y comida.
- r = tasa de crecimiento
- K = capacidad máxima del territorio

2. MÉTODO NUMÉRICO:
Implementé el Método de Heun. Es mejor que el método de Euler porque predice un valor y lo corrige, 
dando resultados mucho más exactos y confiables para la simulación.

3. INTERPRETACIÓN DE ESCENARIOS:
🟢 CONSERVACIÓN: Con K=250, la población crece y se estabiliza alta. -> CONCLUSIÓN: Si cuidamos, sobreviven.
🟠 DEFORESTACIÓN: Bajo K=150. Crece muy lento. -> CONCLUSIÓN: Sin bosque, hay pocos cóndores.
🔴 CAZA: Bajo r=0.015. Casi no crece. -> CONCLUSIÓN: La acción humana es el mayor peligro de extinción.

4. COMPARACIÓN:
Los puntos azules son censos reales desde 1990. Vemos que vamos camino al escenario rojo/amarillo, 
pero si cambiamos las políticas de cuidado, podemos llegar a la línea verde.
"""