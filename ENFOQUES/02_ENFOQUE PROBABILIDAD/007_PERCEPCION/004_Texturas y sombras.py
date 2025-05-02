import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import local_binary_pattern

# Cargar imagen en escala de grises
imagen = cv2.imread('Perros.jpg', cv2.IMREAD_GRAYSCALE)

# Parámetros de LBP
radio = 1
puntos = 8 * radio

# Aplicar el algoritmo Local Binary Pattern (LBP)
lbp = local_binary_pattern(imagen, puntos, radio, method='uniform')

# Mostrar la imagen original y la textura
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray'), plt.title('Imagen Original')
plt.subplot(1, 2, 2), plt.imshow(lbp, cmap='gray'), plt.title('Textura con LBP')
plt.show()
