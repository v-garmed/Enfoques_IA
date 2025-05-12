# Importar librerías necesarias
# sklearn.neural_network.MLPClassifier: Para crear y entrenar una red neuronal multicapa
# sklearn.datasets.make_classification: Para generar un conjunto de datos sintéticos
# sklearn.model_selection.train_test_split: Para dividir los datos en conjuntos de entrenamiento y prueba
# sklearn.metrics.accuracy_score: Para calcular la precisión del modelo
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar datos sintéticos
# Se crean 1000 muestras con 20 características, con una semilla aleatoria para reproducibilidad
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Dividir los datos en conjuntos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar una MLP (Red Neuronal Multicapa)
# Se define una red con dos capas ocultas, cada una con 10 neuronas
# Se establece un máximo de 1000 iteraciones para el entrenamiento
mlp = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=1000)
mlp.fit(X_train, y_train)  # Entrenar el modelo con los datos de entrenamiento

# Evaluar el modelo
# Se predicen las etiquetas para los datos de prueba
y_pred = mlp.predict(X_test)

# Calcular la precisión del modelo comparando las etiquetas reales con las predichas
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión del modelo
print(f"MLP Accuracy: {accuracy}")
