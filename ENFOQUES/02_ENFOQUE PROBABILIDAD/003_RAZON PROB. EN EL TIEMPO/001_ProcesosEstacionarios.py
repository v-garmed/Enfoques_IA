import numpy as np
import matplotlib.pyplot as plt

# Generar proceso estacionario: Ruido blanco (media y varianza constantes)
np.random.seed(42)
t = np.arange(100)
ruido_blanco = np.random.normal(0, 1, size=100)

# Generar proceso no estacionario: Tendencia creciente
tendencia = t * 0.1 + np.random.normal(0, 1, size=100)

# Graficar ambos procesos
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t, ruido_blanco, label="Ruido blanco")
plt.title("Proceso Estacionario")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, tendencia, color="orange", label="Tendencia creciente")
plt.title("Proceso No Estacionario")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
