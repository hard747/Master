import cv2
import numpy as np
import pyrealsense2 as rs

# Configurando el pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Iniciando el pipeline
pipeline.start(config)

try:
    while True:
        # Esperando un nuevo frame
        frames = pipeline.wait_for_frames()

        # Obteniendo el frame de color
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        # Convertir el frame a una imagen OpenCV
        color_image = np.asanyarray(color_frame.get_data())

        # Mostrar la imagen
        cv2.imshow('RealSense SR300', color_image)

        # Salir al presionar la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Cerrar el pipeline
    pipeline.stop()
    cv2.destroyAllWindows()

