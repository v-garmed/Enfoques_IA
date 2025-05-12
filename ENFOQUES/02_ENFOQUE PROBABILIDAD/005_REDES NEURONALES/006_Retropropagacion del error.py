# Importar librerías necesarias
import numpy as np

# Función de activación (sigmoide) y su derivada
# La función sigmoide convierte un valor en un rango entre 0 y 1
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide, utilizada para calcular gradientes
def sigmoid_derivative(x):
    return x * (1 - x)

# Datos de entrada y salida esperada para el problema XOR lógico
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Entradas
y = np.array([[0], [1], [1], [0]])  # Salidas esperadas

# Inicializar pesos aleatoriamente para las conexiones entre capas
np.random.seed(42)  # Fijar la semilla para reproducibilidad
weights_input_hidden = np.random.uniform(size=(2, 2))  # Pesos entre capa de entrada y capa oculta
weights_hidden_output = np.random.uniform(size=(2, 1))  # Pesos entre capa oculta y capa de salida

# Parámetros de entrenamiento
learning_rate = 0.1  # Tasa de aprendizaje
epochs = 10000  # Número de iteraciones de entrenamiento

# Bucle de entrenamiento
for epoch in range(epochs):
    # Forward pass: calcular las salidas de cada capa
    hidden_layer_input = np.dot(X, weights_input_hidden)  # Entrada a la capa oculta
    hidden_layer_output = sigmoid(hidden_layer_input)  # Salida de la capa oculta
    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)  # Entrada a la capa de salida
    predicted_output = sigmoid(output_layer_input)  # Salida predicha (final)

    # Backward pass: calcular los errores y ajustar los pesos
    error = y - predicted_output  # Error entre la salida esperada y la predicha
    d_predicted_output = error * sigmoid_derivative(predicted_output)  # Gradiente de la salida predicha

    error_hidden_layer = d_predicted_output.dot(weights_hidden_output.T)  # Error propagado a la capa oculta
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)  # Gradiente de la capa oculta

    # Actualizar pesos utilizando el gradiente descendente
    weights_hidden_output += hidden_layer_output.T.dot(d_predicted_output) * learning_rate  # Actualizar pesos de salida
    weights_input_hidden += X.T.dot(d_hidden_layer) * learning_rate  # Actualizar pesos de entrada

# Imprimir la salida predicha después del entrenamiento
print(f"Predicted output: {predicted_output}")
