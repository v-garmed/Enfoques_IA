import numpy as np

# Número de pasos de tiempo
n = 10

# Estado inicial: posición = 0, velocidad = 1
x = np.array([[0], [1]])  # [posición, velocidad]

# Matriz de transición del estado
F = np.array([[1, 1],
              [0, 1]])  # Posición = pos + vel * dt, Velocidad constante

# Matriz de observación (solo se observa posición)
H = np.array([[1, 0]])

# Matriz de covarianza del proceso (ruido del modelo)
Q = np.array([[1, 0],
              [0, 1]])

# Matriz de covarianza de la medición (ruido en las observaciones)
R = np.array([[2]])

# Matriz de covarianza del estado inicial
P = np.eye(2)

# Observaciones simuladas (posición con ruido)
np.random.seed(0)
observaciones = [x[0,0] + np.random.normal(0, np.sqrt(R[0,0])) for _ in range(n)]

# Filtro de Kalman
for z in observaciones:
    # PREDICCIÓN
    x = F @ x                          # Predicción del estado
    P = F @ P @ F.T + Q                # Predicción de la covarianza

    # CORRECCIÓN
    y = np.array([[z]]) - H @ x       # Innovación (residuo)
    S = H @ P @ H.T + R               # Covarianza del residuo
    K = P @ H.T @ np.linalg.inv(S)    # Ganancia de Kalman

    x = x + K @ y                     # Corrección del estado
    P = (np.eye(2) - K @ H) @ P       # Corrección de la covarianza

    print(f"Estimación -> Posición: {x[0,0]:.2f}, Velocidad: {x[1,0]:.2f}")
