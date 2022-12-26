import cv2
import numpy as np

def rgb_to_hsi(rgb_image):
    hsi_image = rgb_image.copy()

    rows, cols, _ = hsi_image.shape

    for i in range(rows):
        for j in range(cols):
            r, g, b = rgb_image[i, j]

            r, g, b = r / 255.0, g / 255.0, b / 255.0
            intensity = (r + g + b) / 3
            saturation = 1 - (3 / (r + g + b)) * min(r, g, b)
            hue = 0
            if saturation != 0:
                hue = (1/2) * ((r - g) + (r - b)) / ((r - g)**2 + (r - b) * (g - b))
                hue = math.acos(hue)
                if b > g:
                    hue = 360 - hue
            hsi_image[i, j] = (hue, saturation, intensity)

    return hsi_image

rgb_image = cv2.imread('rgb_image.jpg')

hsi_image = rgb_to_hsi(rgb_image)

cv2.imshow('HSI Image', hsi_image)

cv2.waitKey(0)
cv2.destroyAllWindows()