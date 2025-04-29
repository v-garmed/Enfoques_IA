# Importar librerías necesarias
import numpy as np

# Definir una función de activación (sigmoide)
# La función sigmoide transforma la entrada en un valor entre 0 y 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Parámetros de la neurona
# Los pesos y el sesgo son inicializados manualmente
weights = np.array([0.5, 0.5])
bias = 0.1

# Entradas
# Las entradas son un vector de valores binarios
inputs = np.array([1, 0])

# Cálculo de la salida de la neurona
# La salida se calcula como la función sigmoide de la suma ponderada de las entradas más el sesgo
output = sigmoid(np.dot(weights, inputs) + bias)
print(f"Salida de la neurona: {output}")
