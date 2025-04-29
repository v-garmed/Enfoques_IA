# Importar librerías necesarias
from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

# Generar datos sintéticos
np.random.seed(42)
data = np.random.rand(100, 3)

# Entrenar el SOM
# El SOM tiene una cuadrícula de 10x10 neuronas
som = MiniSom(x=10, y=10, input_len=3, sigma=1.0, learning_rate=0.5)
som.random_weights_init(data)
som.train_random(data, 100)

# Visualizar el SOM
plt.figure(figsize=(10, 10))
for i, x in enumerate(data):
    w = som.winner(x)  # Encontrar la neurona ganadora para cada dato
    plt.text(w[0], w[1], str(i), color='k')  # Mostrar el índice del dato en la posición de la neurona ganadora
plt.title('Mapa Autoorganizado de Kohonen (SOM)')
plt.xlabel('Neurona en X')
plt.ylabel('Neurona en Y')
plt.show()
