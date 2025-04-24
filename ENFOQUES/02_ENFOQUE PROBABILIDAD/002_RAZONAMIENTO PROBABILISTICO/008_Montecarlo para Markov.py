import random
import math
import matplotlib.pyplot as plt

# Función objetivo proporcional a la distribución deseada (una gaussiana sin normalizar)
def target_distribution(x):
    return math.exp(-x**2 / 2)

# Algoritmo Metropolis-Hastings
def metropolis_hastings(steps=10000, proposal_std=1.0):
    x = 0.0  # estado inicial
    samples = []

    for _ in range(steps):
        # Proponer un nuevo estado (muestra candidata)
        x_new = random.gauss(x, proposal_std)

        # Calcular probabilidad de aceptación
        p_current = target_distribution(x)
        p_new = target_distribution(x_new)
        acceptance = min(1, p_new / p_current)

        # Aceptar o rechazar
        if random.random() < acceptance:
            x = x_new  # Aceptamos la nueva muestra

        samples.append(x)

    return samples

# Ejecutar el muestreo
samples = metropolis_hastings()

# Graficar los resultados
plt.hist(samples, bins=50, density=True, alpha=0.7, label="Muestras MCMC")
plt.title("Distribución aproximada usando Metropolis-Hastings")
plt.xlabel("x")
plt.ylabel("Densidad")
plt.legend()
plt.grid(True)
plt.show()
