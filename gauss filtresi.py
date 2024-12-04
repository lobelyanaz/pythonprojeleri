import cv2
import numpy as np

[0,0,0,3,100,100,100]
img=cv2.imread("lena.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(15,15),0)
median=cv2.medianBlur(gray,15)
cv2.imshow("Gaussian Blur",blurred)
cv2.imshow("Median Blur",median)
cv2.waitKey(0)
cv2.destroyAllWindow()
