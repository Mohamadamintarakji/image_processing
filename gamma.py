import cv2
import numpy as np

photo_1 = cv2.imread("cat.jpg",0)
varible = 1
photo = np.zeros(img_1.shape , dtype="uint8")


photo_2 = varible * np.power(photo_1, 3)

photo_3 = varible * np.power(photo_1, 4)

photo_4 = varible * np.power(photo_1, 5)

cv2.imshow("Original", photo_1)
cv2.imshow("Gamma 3", photo_2)
cv2.imshow("Gamma 4", photo_3)
cv2.imshow("Gamma 5", photo_4)

cv2.waitKey(0)
cv2.destroyAllWindows()