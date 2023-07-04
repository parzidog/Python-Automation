import cv2

image = cv2.imread("assets/elfs.jpeg")
watermark = cv2.imread("assets/watermark.png")

h = image.shape[0] - watermark.shape[0]
w = image.shape[1] - watermark.shape[1]

watermark_placement = image[h:, w:]
cv2.imwrite("assets/watermark_place.jpeg", watermark_placement)

blend = cv2.addWeighted(watermark_placement, 0.5, watermark, 0.5, 0)

cv2.imwrite("assets/blend.jpeg", blend)

image[h:, w:] = blend

cv2.imwrite("assets/elfs_watermarked.jpeg", image)
