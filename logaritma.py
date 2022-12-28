import cv2
import numpy as np
from math import log

photo = cv2.imread("cat.jpg" , 0)  
result = 255 / np.log(1 + np.max(photo))

log = result * (np.log(photo + 1))
log = np.array(log, dtype=np.uint8)

cv2.imshow("Original", photo)
cv2.imshow("log", log)
cv2.waitKey(0)
cv2.destroyAllWindows()