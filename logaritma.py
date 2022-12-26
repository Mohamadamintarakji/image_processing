import cv2
import numpy as np
from math import log

img = cv2.imread("bridge.jpg" , 0)  
c = 255 / np.log(1 + np.max(img))

logarithm = c * (np.log(img + 1))
logarithm = np.array(logarithm, dtype=np.uint8)

cv2.imshow("Original", img)
cv2.imshow("logarithm", logarithm)
cv2.waitKey(0)
cv2.destroyAllWindows()