# Importar librerías necesarias
from minisom import MiniSom  # MiniSom es una librería para implementar Mapas Autoorganizados (SOM) de Kohonen.
import numpy as np  # NumPy se utiliza para trabajar con arreglos y realizar cálculos numéricos.
import matplotlib.pyplot as plt  # Matplotlib se utiliza para crear visualizaciones gráficas.

# Generar datos sintéticos
np.random.seed(42)  # Fijar la semilla para reproducibilidad de los datos aleatorios.
data = np.random.rand(100, 3)  # Crear un conjunto de 100 puntos de datos con 3 características (valores aleatorios entre 0 y 1).

# Entrenar el SOM
# El SOM tiene una cuadrícula de 10x10 neuronas
som = MiniSom(x=10, y=10, input_len=3, sigma=1.0, learning_rate=0.5)  
# x, y: Dimensiones de la cuadrícula del SOM (10x10).
# input_len: Número de características de entrada (3 en este caso).
# sigma: Radio de influencia de las neuronas vecinas.
# learning_rate: Tasa de aprendizaje para ajustar los pesos.

som.random_weights_init(data)  # Inicializar los pesos de las neuronas de forma aleatoria basándose en los datos de entrada.
som.train_random(data, 100)  # Entrenar el SOM con los datos de entrada durante 100 iteraciones.

# Visualizar el SOM
plt.figure(figsize=(10, 10))  # Crear una figura de tamaño 10x10 pulgadas.
for i, x in enumerate(data):  # Iterar sobre cada punto de datos.
    w = som.winner(x)  # Encontrar la neurona ganadora para el punto de datos actual.
    plt.text(w[0], w[1], str(i), color='k')  
    # Dibujar el índice del punto de datos en la posición de la neurona ganadora en la cuadrícula.

plt.title('Mapa Autoorganizado de Kohonen (SOM)')  # Título del gráfico.
plt.xlabel('Neurona en X')  # Etiqueta del eje X.
plt.ylabel('Neurona en Y')  # Etiqueta del eje Y.
plt.show()  # Mostrar el gráfico.
