# Importar librerías necesarias
import numpy as np  # Se utiliza para manejar arreglos y realizar operaciones matemáticas

# Datos de ejemplo (AND lógico)
# Conjunto de datos de entrenamiento con entradas (X) y salidas esperadas (y)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas: combinaciones de 0 y 1
y = np.array([0, 0, 0, 1])  # Salidas esperadas: resultado del AND lógico

# Clase Perceptrón
class Perceptron:
    def __init__(self, learning_rate=0.1, n_iterations=100):
        # Inicialización del perceptrón
        self.learning_rate = learning_rate  # Tasa de aprendizaje para ajustar los pesos
        self.n_iterations = n_iterations    # Número de iteraciones para el entrenamiento
        self.weights = np.zeros(X.shape[1]) # Inicializar los pesos a cero (uno por cada entrada)
        self.bias = 0                       # Inicializar el sesgo (bias) a cero

    # Función de activación (escalón)
    def step_function(self, x):
        # Devuelve 1 si la entrada es mayor o igual a 0, de lo contrario devuelve 0
        return np.where(x >= 0, 1, 0)

    # Entrenamiento del Perceptrón
    def fit(self, X, y):
        # Ajusta los pesos y el sesgo en función de los datos de entrenamiento
        for _ in range(self.n_iterations):  # Repetir el proceso de entrenamiento
            for xi, target in zip(X, y):    # Iterar sobre cada muestra de entrada y su salida esperada
                # Calcular la actualización basada en el error (diferencia entre salida esperada y predicción)
                update = self.learning_rate * (target - self.predict(xi))
                # Actualizar los pesos y el sesgo
                self.weights += update * xi
                self.bias += update

    # Predicción del Perceptrón
    def predict(self, X):
        # Calcula la salida lineal (producto punto de las entradas y los pesos, más el sesgo)
        linear_output = np.dot(X, self.weights) + self.bias
        # Aplica la función de activación para obtener la predicción final
        return self.step_function(linear_output)

# Entrenar el Perceptrón
perceptron = Perceptron()  # Crear una instancia del perceptrón con valores predeterminados
perceptron.fit(X, y)       # Entrenar el perceptrón con los datos de entrada y salida esperada
# Imprimir los pesos y el sesgo finales después del entrenamiento
print(f"Perceptron weights: {perceptron.weights}, bias: {perceptron.bias}")
