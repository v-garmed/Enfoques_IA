import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
imagen = cv2.imread('perros.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar un suavizado para reducir el ruido
imagen_suave = cv2.GaussianBlur(imagen, (5, 5), 0)

# Aplicar Detección de Bordes con Canny
bordes = cv2.Canny(imagen_suave, 50, 150)

# Aplicar Segmentación por Umbral
_, segmentada = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Mostrar los resultados
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1), plt.imshow(imagen, cmap='gray'), plt.title('Original')
plt.subplot(1, 3, 2), plt.imshow(bordes, cmap='gray'), plt.title('Detección de Aristas (Canny)')
plt.subplot(1, 3, 3), plt.imshow(segmentada, cmap='gray'), plt.title('Segmentación por Umbral')
plt.show()
