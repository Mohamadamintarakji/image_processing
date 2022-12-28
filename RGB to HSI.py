import cv2
import numpy as np

def convert_rgb_hsi(rgb_photo):
    photo = rgb_image.copy()

    rows, cols, _ = photo.shape

    for i in range(rows):
        for j in range(cols):
            r, g, b = rgb_photo[i, j]

            r, g, b = r / 255.0, g / 255.0, b / 255.0
            density = (r + g + b) / 3
            sat = 1 - (3 / (r + g + b)) * min(r, g, b)
            streak = 0
            if sat != 0:
                streak = (1/2) * ((r - g) + (r - b)) / ((r - g)**2 + (r - b) * (g - b))
                streak = math.acos(streak)
                if b > g:
                    streak = 360 - streak
           photo[i, j] = (streak, sat, density)

    return photo

rgb_photo = cv2.imread('cat.jpg')

photo = convert_rgb_hsi(rgb_photo)

cv2.imshow('HSI Image', photo)

cv2.waitKey(0)
cv2.destroyAllWindows()