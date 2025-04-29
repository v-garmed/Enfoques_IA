# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definir funciones de activación
# La función sigmoide transforma la entrada en un valor entre 0 y 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# La función ReLU (Rectified Linear Unit) devuelve el valor de entrada si es positivo, de lo contrario devuelve 0
def relu(x):
    return np.maximum(0, x)

# La función tanh (tangente hiperbólica) transforma la entrada en un valor entre -1 y 1
def tanh(x):
    return np.tanh(x)

# Valores de entrada
# Generar una secuencia de valores entre -10 y 10
x = np.linspace(-10, 10, 100)

# Visualizar las funciones de activación
plt.figure(figsize=(12, 4))

# Gráfica de la función sigmoide
plt.subplot(1, 3, 1)
plt.plot(x, sigmoid(x))
plt.title('Sigmoid')
plt.xlabel('Entrada')
plt.ylabel('Salida')

# Gráfica de la función ReLU
plt.subplot(1, 3, 2)
plt.plot(x, relu(x))
plt.title('ReLU')
plt.xlabel('Entrada')
plt.ylabel('Salida')

# Gráfica de la función tanh
plt.subplot(1, 3, 3)
plt.plot(x, tanh(x))
plt.title('Tanh')
plt.xlabel('Entrada')
plt.ylabel('Salida')

plt.tight_layout()
plt.show()
