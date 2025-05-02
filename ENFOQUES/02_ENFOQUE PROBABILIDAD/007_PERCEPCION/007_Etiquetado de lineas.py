import cv2
import numpy as np

# Cargar imagen en escala de grises
imagen = cv2.imread("lineas.png", cv2.IMREAD_GRAYSCALE)

# Aplicar umbral para convertir la imagen en binaria
_, binaria = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY_INV)

# Encontrar componentes conectados
num_labels, etiquetas = cv2.connectedComponents(binaria)

# Convertir etiquetas a colores para visualización
etiquetas_coloreadas = cv2.applyColorMap((etiquetas * 10).astype(np.uint8), cv2.COLORMAP_JET)

# Mostrar el resultado
cv2.imshow("Etiquetado de Lineas", etiquetas_coloreadas)
print(f"Número de líneas detectadas: {num_labels - 1}")  # Se resta 1 porque la etiqueta 0 es el fondo

cv2.waitKey(0)
cv2.destroyAllWindows()
