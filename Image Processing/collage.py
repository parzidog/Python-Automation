import os
import cv2
import numpy as np

columns = 3
rows = 2

margin = 25

images = os.listdir("assets/images")
image_objects = [cv2.imread(f"assets/images/{filename}") for filename in images]

shape = cv2.imread("assets/images/1.jpeg").shape

big_image = np.zeros(
    (
        ((shape[0] + margin) * rows + margin),
        ((shape[1] + margin) * columns + margin),
        shape[2],
    ),
    np.uint8,
)

big_image.fill(255)

positions = [(x, y) for x in range(columns) for y in range(rows)]

for (pos_x, pos_y), image in zip(positions, image_objects):
    x = pos_x * (shape[1] + margin) + margin
    y = pos_y * (shape[0] + margin) + margin

    big_image[y : y + shape[0], x : x + shape[1]] = image

cv2.imwrite("assets/filled_grid.jpeg", big_image)
