import cv2

image = cv2.imread("assets/galaxy.jpeg")


def calculate_size(scale, width, height):
    new_width = int(width * scale)
    new_height = int(height * scale)

    return (new_width, new_height)


def resize(path, scale):
    image = cv2.imread(path)
    new_dim = calculate_size(scale, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite("assets/resized_image.jpeg", resized_image)


resize("assets/galaxy.jpeg", 0.5)
