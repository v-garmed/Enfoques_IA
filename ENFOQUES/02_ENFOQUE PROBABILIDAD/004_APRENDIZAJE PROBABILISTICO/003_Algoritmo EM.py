# Importar librerías necesarias
import numpy as np
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

# Generar datos sintéticos
np.random.seed(42)
data = np.vstack([
    np.random.normal(0, 1, (100, 2)),
    np.random.normal(5, 1, (100, 2))
])

# Aplicar el algoritmo EM
gmm = GaussianMixture(n_components=2)
gmm.fit(data)
labels = gmm.predict(data)

# Visualizar los resultados
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
plt.title('Clustering con Gaussian Mixture Model')
plt.show()
