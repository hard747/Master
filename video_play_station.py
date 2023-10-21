import cv2

def grabar_video():
    # Intenta abrir la cámara PlayStation con el identificador 2
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        print("No se pudo abrir la cámara PlayStation")
        return

    # Define el codec y crea un objeto VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('video.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        # Lee un frame de la cámara
        ret, frame = cap.read()

        if not ret:
            print("No se pudo capturar el frame")
            break

        # Escribe el frame en el archivo de video
        out.write(frame)

        # Presiona 'q' para salir del bucle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera la cámara y el archivo de video
    cap.release()
    out.release()

if __name__ == "__main__":
    grabar_video()
