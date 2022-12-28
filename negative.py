import cv2 as cv2
import numpy as np

photo = cv2.imread("cat.jpg")
photo_neg = 255 - photo - 1

cv2.imshow("Original", photo)
cv2.imshow("negative", photo_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()