import cv2
import pytesseract

# Ruta de instalación de tesseract si es necesario (ej. en Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Cargar la imagen
imagen = cv2.imread("texto_escrito.jpg")

# Preprocesar la imagen: convertir a escala de grises y aplicar umbral
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_, umbral = cv2.threshold(gris, 150, 255, cv2.THRESH_BINARY)

# Usar Tesseract para reconocer texto
texto_detectado = pytesseract.image_to_string(umbral, lang='spa')

# Mostrar resultado
print("Texto reconocido:")
print(texto_detectado)

# Mostrar la imagen (opcional)
cv2.imshow("Imagen Preprocesada", umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
