import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar imagen en escala de grises
imagen = cv2.imread('perros.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar filtro Gaussiano para suavizar la imagen
suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Aplicar filtro Sobel para detectar bordes en X e Y
sobelx = cv2.Sobel(suavizada, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(suavizada, cv2.CV_64F, 0, 1, ksize=5)

# Magnitud del gradiente
magnitud = np.sqrt(sobelx**2 + sobely**2)

# Mostrar resultados
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1), plt.imshow(imagen, cmap='gray'), plt.title('Original')
plt.subplot(1, 3, 2), plt.imshow(suavizada, cmap='gray'), plt.title('Suavizada (Gaussiano)')
plt.subplot(1, 3, 3), plt.imshow(magnitud, cmap='gray'), plt.title('Bordes (Sobel)')
plt.show()
