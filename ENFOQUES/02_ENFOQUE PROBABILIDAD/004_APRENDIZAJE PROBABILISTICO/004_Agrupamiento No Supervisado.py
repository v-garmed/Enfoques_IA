# Importar librerías necesarias
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import numpy as np

# Generar datos sintéticos
np.random.seed(42)
data = np.vstack([
    np.random.normal(0, 1, (100, 2)),
    np.random.normal(5, 1, (100, 2))
])

# Aplicar DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(data)

# Visualizar los resultados
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.title('Clustering con DBSCAN')
plt.show()
