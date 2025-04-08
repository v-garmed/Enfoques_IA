import random
import numpy as np

# Número de brazos (acciones disponibles)
k = 3

# Número total de pasos (episodios) de simulación
N = 1000

# Tasa de exploración: probabilidad de elegir acción aleatoria
epsilon = 0.1

# (Desconocidas para el agente) recompensas reales medias de cada brazo
true_means = [1.0, 2.0, 1.5]

# Inicializamos las estimaciones de la media de recompensa para cada brazo en 0
estimates = [0.0] * k

# Contador de cuántas veces hemos seleccionado cada brazo
counts = [0] * k

# Lista para almacenar la recompensa obtenida en cada paso
rewards = []

for t in range(1, N + 1):
    # Decisión ε‑greedy:
    # Generamos un número en [0,1). Si es menor que epsilon, exploramos.
    if random.random() < epsilon:
        # Exploración: elegimos un brazo al azar
        action = random.randrange(k)
    else:
        # Explotación: elegimos el brazo con mayor estimación de recompensa
        action = int(np.argmax(estimates))

    # Simulamos la recompensa: muestreo de una distribución normal
    # con media true_means[action] y desviación estándar 1.0
    reward = random.gauss(true_means[action], 1.0)

    # Actualizamos el contador de veces que seleccionamos este brazo
    counts[action] += 1

    # Actualización incremental de la estimación de la media:
    # new_estimate = old_estimate + (1 / count) * (reward - old_estimate)
    estimates[action] += (reward - estimates[action]) / counts[action]

    # Guardamos la recompensa obtenida para análisis posterior
    rewards.append(reward)

# Al finalizar la simulación, mostramos los resultados
print("Estimaciones finales de las medias:", estimates)
print("Número de selecciones por brazo:", counts)
print("Recompensa acumulada total:", sum(rewards))
