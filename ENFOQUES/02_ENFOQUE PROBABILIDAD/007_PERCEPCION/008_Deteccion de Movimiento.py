import cv2

# Capturar video desde la cámara (0 = cámara predeterminada)
cap = cv2.VideoCapture(0)

# Leer el primer frame
ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

while True:
    # Leer el siguiente frame
    ret, frame2 = cap.read()
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calcular la diferencia entre frames
    diferencia = cv2.absdiff(frame1_gray, frame2_gray)

    # Umbral para resaltar las áreas de cambio
    _, umbral = cv2.threshold(diferencia, 25, 255, cv2.THRESH_BINARY)

    # Mostrar el resultado
    cv2.imshow('Movimiento Detectado', umbral)

    # Actualizar el frame anterior
    frame1_gray = frame2_gray.copy()

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
