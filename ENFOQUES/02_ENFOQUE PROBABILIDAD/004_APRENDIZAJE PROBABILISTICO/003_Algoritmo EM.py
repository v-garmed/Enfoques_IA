# Importar librerías necesarias
# numpy para manejo de datos numéricos, sklearn para el modelo GMM, y matplotlib para visualización
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Generar datos sintéticos
# Se crean dos conjuntos de datos con distribución normal, uno centrado en (0,0) y otro en (5,5)
np.random.seed(42)  # Fijar la semilla para reproducibilidad
data = np.vstack([
    np.random.normal(0, 1, (100, 2)),  # 100 puntos con media 0 y desviación estándar 1
    np.random.normal(5, 1, (100, 2))  # 100 puntos con media 5 y desviación estándar 1
])

# Aplicar el algoritmo EM
# Se utiliza el modelo Gaussian Mixture Model (GMM) con 2 componentes
gmm = GaussianMixture(n_components=2)  # Inicializar el modelo con 2 componentes
gmm.fit(data)  # Ajustar el modelo a los datos
labels = gmm.predict(data)  # Predecir las etiquetas de los datos según el modelo ajustado

# Visualizar los resultados
# Graficar los puntos de datos coloreados según las etiquetas asignadas por el modelo
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')  # Colorear por etiquetas
plt.title('Clustering con Gaussian Mixture Model')  # Título del gráfico
plt.show()  # Mostrar el gráfico
