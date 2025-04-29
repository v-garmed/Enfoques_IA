# Importar librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Generar datos linealmente separables
np.random.seed(42)
X = np.random.randn(100, 2)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, 0)

# Visualizar los datos
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr')
plt.title('Datos Linealmente Separables')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()

# Entrenar el Perceptrón
perceptron = Perceptron()
perceptron.fit(X, y)
print(f"Perceptron weights: {perceptron.weights}, bias: {perceptron.bias}")
