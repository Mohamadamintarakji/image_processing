import cv2
import numpy as np
import random

image = cv2.imread('image.jpg')

height, width, _ = image.shape

random_number_generator = random.Random()

for i in range(height):
    for j in range(width):
        random_number = random_number_generator.uniform(0, 1)

        if random_number < 0.1:
            image[i, j] = (0, 0, 0)

        elif random_number < 0.2:
            image[i, j] = (255, 255, 255)

cv2.imshow('Salt and Pepper Image', image)

cv2.waitKey(0)

cv2.destroyAllWindows()