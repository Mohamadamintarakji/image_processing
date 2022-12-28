import cv2

photo = cv2.imread("cat.jpg", cv2.IMREAD_GRAYSCALE)

X = cv2.Sobel(photo, cv2.CV_64F, 1, 0,ksize=5)
Y = cv2.Sobel(photo, cv2.CV_64F, 0, 1,ksize=5)


cv2.imshow("Original", photo)
cv2.imshow("X+Y", X+Y)

cv2.waitKey(0)
cv2.destroyAllWindows()