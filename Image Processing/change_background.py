import cv2
import numpy as np

foreground = cv2.imread("assets/giraffe.jpeg")
background = cv2.imread("assets/safari.jpeg")
width = foreground.shape[1]
height = foreground.shape[0]

for i in range(width):
    for j in range(height):
        pixel = foreground[j, i]
        if np.any(pixel == [1, 255, 1]):
            foreground[j, i] = background[j, i]

cv2.imwrite("assets/output.jpeg", foreground)
