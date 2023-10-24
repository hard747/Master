import cv2
imagem=cv2.imread('imagem1.jpg', 0)
cv2.imshow('Prueba de imagen', imagem)
cv2.imwrite('grises.jpg',imagem)
cv2.waitKey(0)
cv2.destroyWindow()
