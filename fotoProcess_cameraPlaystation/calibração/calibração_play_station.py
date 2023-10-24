import numpy as np
import cv2

# Define el tamaño del patrón (número de esquinas)
patron_size = (8, 11)  # Por ejemplo, para un tablero de ajedrez de 9x6

# Prepara las coordenadas de los puntos del patrón
objp = np.zeros((np.prod(patron_size), 3), dtype=np.float32)
objp[:, :2] = np.mgrid[0:patron_size[0], 0:patron_size[1]].T.reshape(-1, 2)

# Arrays para almacenar puntos de imagen y puntos de objeto de todas las imágenes
objpoints = []  # 3D puntos del mundo real
imgpoints = []  # 2D puntos de la imagen

# Lista de imágenes del patrón (reemplaza con tus propias imágenes)
images = ['imagen1.png', 'imagen2.png', 'imagen3.png']

for fname in images:
    img = cv2.imread(fname)
    if img is None:
        print(f'Error al cargar la imagen: {fname}')
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Intenta encontrar el patrón en la imagen
    ret, corners = cv2.findChessboardCorners(gray, patron_size, None)

    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

# Calibra la cámara
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Guarda los parámetros de calibración en un archivo YAML
calibration_data = {
    'Camera.fx': mtx[0, 0],
    'Camera.fy': mtx[1, 1],
    'Camera.cx': mtx[0, 2],
    'Camera.cy': mtx[1, 2],
    'Camera.k1': dist[0],
    'Camera.k2': dist[1],
    'Camera.p1': dist[2],
    'Camera.p2': dist[3],
    'Camera.k3': dist[4],
    'Camera.fps': 30.0,  # Ajusta la tasa de fotogramas según corresponda
    'Camera.RGB': 1
}

with open('calibracion.yaml', 'w') as f:
    yaml.dump(calibration_data, f)
print("Calibración completa. Parámetros guardados en calibracion.yaml")
print(images)
