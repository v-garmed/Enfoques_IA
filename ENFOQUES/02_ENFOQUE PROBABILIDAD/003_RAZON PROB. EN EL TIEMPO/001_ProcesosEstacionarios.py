import numpy as np
import matplotlib.pyplot as plt

# Fijar la semilla para reproducibilidad de los resultados
np.random.seed(42)

# Crear un vector de tiempo de 0 a 99
t = np.arange(100)

# Generar un proceso estacionario: Ruido blanco (media y varianza constantes)
# Aquí se genera un conjunto de 100 valores aleatorios con distribución normal (media=0, desviación estándar=1)
ruido_blanco = np.random.normal(0, 1, size=100)

# Generar un proceso no estacionario: Tendencia creciente
# Se crea una tendencia lineal (t * 0.1) y se le suma ruido aleatorio con distribución normal
tendencia = t * 0.1 + np.random.normal(0, 1, size=100)

# Configurar el tamaño de la figura para las gráficas
plt.figure(figsize=(12, 5))

# Graficar el proceso estacionario (ruido blanco)
plt.subplot(1, 2, 1)  # Crear el primer subplot (1 fila, 2 columnas, posición 1)
plt.plot(t, ruido_blanco, label="Ruido blanco")  # Graficar el ruido blanco
plt.title("Proceso Estacionario")  # Título del gráfico
plt.xlabel("Tiempo")  # Etiqueta del eje X
plt.ylabel("Valor")  # Etiqueta del eje Y
plt.grid(True)  # Mostrar la cuadrícula
plt.legend()  # Mostrar la leyenda

# Graficar el proceso no estacionario (tendencia creciente)
plt.subplot(1, 2, 2)  # Crear el segundo subplot (1 fila, 2 columnas, posición 2)
plt.plot(t, tendencia, color="orange", label="Tendencia creciente")  # Graficar la tendencia
plt.title("Proceso No Estacionario")  # Título del gráfico
plt.xlabel("Tiempo")  # Etiqueta del eje X
plt.ylabel("Valor")  # Etiqueta del eje Y
plt.grid(True)  # Mostrar la cuadrícula
plt.legend()  # Mostrar la leyenda

# Ajustar el diseño de los subplots para evitar superposición
plt.tight_layout()

# Mostrar las gráficas
plt.show()
