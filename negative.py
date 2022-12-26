import cv2 as cv2
import numpy as np

img = cv2.imread("bridge.jpg")
img_neg = 255 - img - 1

cv2.imshow("Original", img)
cv2.imshow("negative", img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()