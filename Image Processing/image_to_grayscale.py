import cv2

color = cv2.imread("assets/galaxy.jpeg", 0)

cv2.imwrite("assets/galaxy_grey.jpeg", color)
