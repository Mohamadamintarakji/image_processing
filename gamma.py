import cv2
import numpy as np

img_1 = cv2.imread("bridge.jpg",0)
c = 1
img = np.zeros(img_1.shape , dtype="uint8")


img_2 = c * np.power(img_1, 3)

img_3 = c * np.power(img_1, 4)

img_4 = c * np.power(img_1, 5)

cv2.imshow("Original", img_1)
cv2.imshow("Gamma 3", img_2)
cv2.imshow("Gamma 4", img_3)
cv2.imshow("Gamma 5", img_4)

cv2.waitKey(0)
cv2.destroyAllWindows()