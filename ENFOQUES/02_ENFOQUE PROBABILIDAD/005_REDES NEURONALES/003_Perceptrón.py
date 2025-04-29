# Importar librerías necesarias
import numpy as np

# Datos de ejemplo (AND lógico)
# Conjunto de datos de entrenamiento con entradas y salidas esperadas
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])

# Clase Perceptrón
class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100):
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.n_iterations = n_iterations    # Número de iteraciones
        self.weights = np.zeros(X.shape[1]) # Inicializar pesos a cero
        self.bias = 0                       # Inicializar sesgo a cero

    # Función de activación (escalón)
    def step_function(self, x):
        return np.where(x >= 0, 1, 0)

    # Entrenamiento del Perceptrón
    def fit(self, X, y):
        for _ in range(self.n_iterations):
            for xi, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(xi))
                self.weights += update * xi
                self.bias += update

    # Predicción del Perceptrón
    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self.step_function(linear_output)

# Entrenar el Perceptrón
perceptron = Perceptron()
perceptron.fit(X, y)
print(f"Perceptron weights: {perceptron.weights}, bias: {perceptron.bias}")
