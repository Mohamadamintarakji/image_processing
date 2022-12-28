import cv2
import numpy as np
import random

photo = cv2.imread('cat.jpg')

height, width, _ = photo.shape

random_number_generator = random.Random()

for i in range(height):
    for j in range(width):
        random_number = random_number_generator.uniform(0, 1)

        if random_number < 0.1:
            photo[i, j] = (0, 0, 0)

        elif random_number < 0.2:
            photo[i, j] = (255, 255, 255)

cv2.imshow('Salt and Pepper photo', photo)

cv2.waitKey(0)

cv2.destroyAllWindows()