import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("face",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break