import numpy as np
import matplotlib.pyplot as plt
import cv2

img= cv2.imread('imagem1.jpg',1)

corners= cv2.goodFeaturesToTrack(img,100,0.01,10)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

