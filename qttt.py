import cv2
import numpy as np

img=cv2.imread("lena.png")
img[100:200,100:200]=[0,100,0]
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindow()
