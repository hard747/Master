import cv2
import keyboard
import time

def encender_camara(identificador):
    cap = cv2.VideoCapture(identificador)

    if not cap.isOpened():
        print(f"No se pudo abrir la cámara con el identificador {identificador}")
        return

    print(f"Cámara {identificador} encendida. Presiona 'q' para apagar.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("No se pudo capturar el frame")
            break

        cv2.imshow("Camara", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    identificador = 2  # Cambia esto al identificador de tu cámara
    encender_camara(identificador)
