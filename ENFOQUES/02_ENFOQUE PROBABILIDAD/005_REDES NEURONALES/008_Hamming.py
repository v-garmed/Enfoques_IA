# Importar librerías necesarias
import numpy as np

# Patrones a almacenar
patterns = np.array([[1, -1, 1, -1],
                     [1, 1, -1, -1],
                     [-1, 1, -1, 1]])

# Entrenar la red de Hopfield
def train_hopfield(patterns):
    num_neurons = patterns.shape[1]
    W = np.zeros((num_neurons, num_neurons))
    for pattern in patterns:
        W += np.outer(pattern, pattern)
    np.fill_diagonal(W, 0)  # La diagonal principal se establece en cero
    return W / num_neurons

# Función de activación (signo)
def signum(x):
    return np.where(x >= 0, 1, -1)

# Recuperar un patrón
def recall(W, pattern, steps=5):
    for _ in range(steps):
        pattern = signum(np.dot(W, pattern))
    return pattern

# Entrenar y recuperar patrones
W = train_hopfield(patterns)
test_pattern = np.array([1, -1, 1, 1])
recalled_pattern = recall(W, test_pattern)
print(f"Recalled pattern: {recalled_pattern}")
