import cv2

video = cv2.VideoCapture(1)
success, frame = video.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier("assets/faces.xml")
output = cv2.VideoWriter(
    "assets/webcam_output.avi", cv2.VideoWriter_fourcc(*"DIVX"), 15, (width, height)
)

while success:
    faces = face_cascade.detectMultiScale(frame, 1.05, 4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 6)

    output.write(frame)

    success, frame = video.read()

output.release()
video.release()
cv2.destroyAllWindows()
