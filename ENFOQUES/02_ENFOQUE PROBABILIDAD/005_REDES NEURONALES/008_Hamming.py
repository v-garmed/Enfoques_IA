# Importar librerías necesarias
import numpy as np

# Patrones a almacenar
# Estos son los patrones que queremos que la red de Hopfield aprenda y recuerde.
patterns = np.array([[1, -1, 1, -1],
                     [1, 1, -1, -1],
                     [-1, 1, -1, 1]])

# Entrenar la red de Hopfield
# Esta función entrena la red de Hopfield calculando la matriz de pesos sinápticos (W).
def train_hopfield(patterns):
    num_neurons = patterns.shape[1]  # Número de neuronas (dimensión de los patrones)
    W = np.zeros((num_neurons, num_neurons))  # Inicializar la matriz de pesos con ceros
    for pattern in patterns:  # Para cada patrón en los datos de entrenamiento
        W += np.outer(pattern, pattern)  # Sumar el producto externo del patrón consigo mismo
    np.fill_diagonal(W, 0)  # La diagonal principal se establece en cero (sin auto-conexiones)
    return W / num_neurons  # Normalizar la matriz de pesos dividiendo por el número de neuronas

# Función de activación (signo)
# Esta función aplica la regla de activación signo, que convierte los valores en 1 o -1.
def signum(x):
    return np.where(x >= 0, 1, -1)

# Recuperar un patrón
# Esta función intenta recuperar un patrón almacenado dado un patrón inicial y la matriz de pesos.
def recall(W, pattern, steps=5):
    for _ in range(steps):  # Realizar un número fijo de iteraciones
        pattern = signum(np.dot(W, pattern))  # Actualizar el patrón usando la matriz de pesos y la función de activación
    return pattern  # Devolver el patrón recuperado

# Entrenar y recuperar patrones
W = train_hopfield(patterns)  # Entrenar la red de Hopfield con los patrones dados
test_pattern = np.array([1, -1, 1, 1])  # Patrón inicial que queremos recuperar (puede estar ruidoso o incompleto)
recalled_pattern = recall(W, test_pattern)  # Recuperar el patrón más cercano almacenado en la red
print(f"Recalled pattern: {recalled_pattern}")  # Imprimir el patrón recuperado
