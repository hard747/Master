import cv2

# Inicia la captura de video
cap = cv2.VideoCapture(0)

while(True):
    # Captura frame por frame
    ret, frame = cap.read()

    # Muestra el frame resultante
    cv2.imshow('Video', frame)

    # Si presionas la tecla 'q', sale del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando todo esté listo, libera la captura
cap.release()
cv2.destroyAllWindows()
