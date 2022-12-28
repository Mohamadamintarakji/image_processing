import cv2
import numpy as np
from scipy import ndimage

Xaxis = np.array([[1, 0], [0, -1]])
Yaxis = np.array([[0, 1], [-1, 0]])

photo = cv2.imread("cat.jpg", 0).astype('float64')

photo /= 255.0
X = ndimage.convolve(photo, Xaxis)
Y = ndimage.convolve(photo, Yaxis)

edged_photo = np.sqrt(np.square(Y) + np.square(X))

cv2.imshow("Original", photo)
cv2.imshow("Robert", edged_photo)
cv2.waitKey(0)
cv2.destroyAllWindows()