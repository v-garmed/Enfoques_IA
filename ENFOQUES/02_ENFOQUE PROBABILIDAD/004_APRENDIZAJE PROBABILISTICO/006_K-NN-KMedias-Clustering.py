# Importar librerías necesarias
from sklearn.datasets import load_iris  # Para cargar el conjunto de datos Iris
from sklearn.model_selection import train_test_split  # Para dividir los datos en entrenamiento y prueba
from sklearn.neighbors import KNeighborsClassifier  # Implementación del algoritmo k-NN
from sklearn.cluster import KMeans  # Implementación del algoritmo k-Medias
from sklearn.metrics import accuracy_score  # Para calcular la precisión del modelo
import matplotlib.pyplot as plt  # Para visualización de datos

# Cargar el conjunto de datos Iris
iris = load_iris()  # Carga el dataset Iris incluido en scikit-learn
X, y = iris.data, iris.target  # Separa las características (X) y las etiquetas (y)

# k-NN para clasificación
# Dividir los datos en conjuntos de entrenamiento y prueba (75% entrenamiento, 25% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Crear un clasificador k-NN con 3 vecinos
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenar el modelo k-NN con los datos de entrenamiento
knn.fit(X_train, y_train)

# Predecir las etiquetas del conjunto de prueba
y_pred = knn.predict(X_test)

# Calcular la precisión del modelo k-NN
accuracy = accuracy_score(y_test, y_pred)
print(f"k-NN Accuracy: {accuracy}")  # Imprimir la precisión del modelo

# k-Medias para agrupamiento
# Crear un modelo k-Medias con 3 clusters (correspondientes a las 3 clases en el dataset Iris)
kmeans = KMeans(n_clusters=3)

# Entrenar el modelo k-Medias con todas las características del dataset
kmeans.fit(X)

# Obtener las etiquetas de los clusters asignados por k-Medias
labels = kmeans.labels_

# Visualizar los clusters
# Crear un gráfico de dispersión de las dos primeras características del dataset
# Colorear los puntos según las etiquetas de los clusters asignados
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title('Clustering con k-Medias')  # Título del gráfico
plt.show()  # Mostrar el gráfico
