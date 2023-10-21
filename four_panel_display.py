import cv2
import numpy as np

def process_depth_canny(depth_image):
    return cv2.Canny(depth_image, 100, 200)

def process_rgb_orb(rgb_image):
    orb = cv2.ORB_create()
    kp, des = orb.detectAndCompute(rgb_image, None)
    return cv2.drawKeypoints(rgb_image, kp, None, color=(0,255,0), flags=0)

def main(rgb_image_path, depth_image_path):
    rgb_image = cv2.imread(rgb_image_path, cv2.IMREAD_COLOR)
    depth_image = cv2.imread(depth_image_path, cv2.IMREAD_UNCHANGED)

    depth_canny = process_depth_canny(depth_image)
    rgb_orb = process_rgb_orb(rgb_image)

    # Convertir depth_canny a una imagen a color
    depth_canny_color = cv2.cvtColor(depth_canny, cv2.COLOR_GRAY2BGR)

    combined_top = np.hstack((rgb_image, depth_image))
    combined_bottom = np.hstack((rgb_orb, depth_canny_color))
    final_image = np.vstack((combined_top, combined_bottom))

    cv2.imshow('Four Panel Display', final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main('rgb_image.jpg', 'depth_image.jpg')
