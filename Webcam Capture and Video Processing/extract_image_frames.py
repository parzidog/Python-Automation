import cv2

video = cv2.VideoCapture("assets/video.mp4")

success, frame = video.read()

count = 1

while success:
    cv2.imwrite(f"assets/frames/{count}.jpg", frame)
    success, frame = video.read()
    count += 1
