import cv2
import numpy as np

img=cv2.imread("lena.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(15,15),0)
edges=cv2.Canny(blurred,100,200)
cv2.imshow("Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindow()                        
                         
