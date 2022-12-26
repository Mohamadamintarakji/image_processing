import cv2

img = cv2.imread("bridge.jpg", cv2.IMREAD_GRAYSCALE)

SobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0,ksize=5)
SobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1,ksize=5)


cv2.imshow("Original", img)
cv2.imshow("SobelX+Y", SobelX+SobelY)

cv2.waitKey(0)
cv2.destroyAllWindows()