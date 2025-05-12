# Importar librerías necesarias
# numpy para operaciones matemáticas y matplotlib para visualización
import numpy as np
import matplotlib.pyplot as plt

# Generar datos linealmente separables
# Se establece una semilla para reproducibilidad y se generan 100 puntos aleatorios en 2D
np.random.seed(42)
X = np.random.randn(100, 2)  # Matriz de características (100 muestras, 2 características)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, 0)  # Etiquetas binarias basadas en una regla lineal

# Visualizar los datos
# Se grafican los puntos con colores diferentes según su etiqueta (y)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr')  # 'bwr' para colores azul y rojo
plt.title('Datos Linealmente Separables')  # Título del gráfico
plt.xlabel('Característica 1')  # Etiqueta del eje X
plt.ylabel('Característica 2')  # Etiqueta del eje Y
plt.show()  # Mostrar el gráfico

# Entrenar el Perceptrón
# Aquí se intenta entrenar un modelo Perceptrón, pero falta la implementación de la clase Perceptron
perceptron = Perceptron()  # Crear una instancia del Perceptrón
perceptron.fit(X, y)  # Ajustar el modelo a los datos
print(f"Perceptron weights: {perceptron.weights}, bias: {perceptron.bias}")  # Imprimir los pesos y el sesgo
