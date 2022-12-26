import cv2
import numpy as np
from scipy import ndimage

robertsX = np.array([[1, 0], [0, -1]])
robertsY = np.array([[0, 1], [-1, 0]])

img = cv2.imread("bridge.jpg", 0).astype('float64')

img /= 255.0
X = ndimage.convolve(img, robertsX)
Y = ndimage.convolve(img, robertsY)

edged_img = np.sqrt(np.square(Y) + np.square(X))

cv2.imshow("Original", img)
cv2.imshow("Robert", edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()