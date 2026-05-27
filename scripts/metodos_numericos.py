import numpy as np
import pandas as pd

# Ecuación del modelo logístico
def modelo_logistico(t, P, r, K):
    return r * P * (1 - P / K)

# Método numérico de Heun
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

# Crear tabla con Pandas
def crear_tabla(t, P, nombre_escenario):
    return pd.DataFrame({
        'Tiempo (años)': t.round(0),
        'Población': P.round(0),
        'Escenario': nombre_escenario
    })