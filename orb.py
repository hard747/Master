import cv2

def process_rgb_orb(rgb_image_path):
    # Leer la imagen RGB
    rgb_image = cv2.imread(rgb_image_path, cv2.IMREAD_COLOR)

    # Inicializar el detector ORB
    orb = cv2.ORB_create()

    # Encontrar keypoints y descriptores con ORB
    kp, des = orb.detectAndCompute(rgb_image, None)

    # Dibujar keypoints en la imagen RGB
    rgb_orb = cv2.drawKeypoints(rgb_image, kp, None, color=(0,255,0), flags=0)

    # Guardar la imagen resultante
    cv2.imwrite('rgb_orb.jpg', rgb_orb)

if __name__ == '__main__':
    process_rgb_orb('rgb_image.jpg')
