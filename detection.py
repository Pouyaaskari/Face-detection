import cv2

img_path = 'image.png'
img = cv2.imread(img_path)

detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

boxes = detector.detectMultiScale(img)
for box in boxes:
    x1, y1, width, height = box
    x2, y2 = x1 + width, y1 + height

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imshow('pooya', img)
cv2.waitKey(0)