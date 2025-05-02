import cv2

# Cargar una imagen
imagen = cv2.imread('personas.jpg')

# Cargar el modelo preentrenado de detección de personas (MobileNet + SSD)
modelo = cv2.dnn.readNetFromCaffe(
    'deploy.prototxt',
    'res10_300x300_ssd_iter_140000.caffemodel'
)

# Preparar la imagen
alto, ancho = imagen.shape[:2]
blob = cv2.dnn.blobFromImage(imagen, 1.0, (300, 300), (104.0, 177.0, 123.0))

# Realizar la detección
modelo.setInput(blob)
detecciones = modelo.forward()

# Dibujar cajas en las detecciones
for i in range(detecciones.shape[2]):
    confianza = detecciones[0, 0, i, 2]
    if confianza > 0.5:
        box = detecciones[0, 0, i, 3:7] * [ancho, alto, ancho, alto]
        (x1, y1, x2, y2) = box.astype("int")
        cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Mostrar la imagen con objetos detectados
cv2.imshow("Detecciones", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
