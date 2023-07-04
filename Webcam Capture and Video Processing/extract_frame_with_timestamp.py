import cv2

video = cv2.VideoCapture("assets/video.mp4")

nr_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(video.get(cv2.CAP_PROP_FPS))

timestamp = "00:00:02.50"
ts_list = timestamp.split(":")
ts_floats = [float(i) for i in ts_list]
hh, mm, ss = ts_floats

frame_nbr = (hh * 3600 + mm * 60 + ss) * fps

video.set(1, frame_nbr)

success, frame = video.read()

cv2.imwrite(f"assets/image_frame@{hh}:{mm}:{ss}.jpg", frame)
