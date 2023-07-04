import cv2
import webbrowser as web

image = cv2.imread("qr.jpg")

detector = cv2.QRCodeDetector()

url, coords, pixels = detector.detectAndDecode(image)

web.open_new_tab(url)
cv2.destroyAllWindows()
