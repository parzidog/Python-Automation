import cv2

image = cv2.imread("assets/humans.jpeg")
face_cascade = cv2.CascadeClassifier("assets/faces.xml")

faces = face_cascade.detectMultiScale(image, 1.05, 4)

for x, y, w, h in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (10, 255, 10), 6)

cv2.imwrite("assets/human_faces_detected.jpeg", image)
