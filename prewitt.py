import cv2
import numpy as np


photo = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)

Xaxis = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
Yaxis = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

X = cv2.filter2D(photo, -1, Xaxis)
Y = cv2.filter2D(photo, -1, Yaxis)

cv2.imshow("Original", photo)
cv2.imshow("X+Y", X+Y)

cv2.waitKey(0)
cv2.destroyAllWindows()