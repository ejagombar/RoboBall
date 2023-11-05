import cv2
import numpy as np
import time

# camera index (default = 0) (added based on Randyr's comment).
cam = cv2.VideoCapture(4)

print('cam has image : %s' % cam.read()[0])
# False = no pics for you to shoot at.

# Lets check start/open your cam!
if cam.read() is False:
    cam.open()

if not cam.isOpened():
    print('Cannot open camera')

while True:
    ret, frame = cam.read()
    cv2.imshow('webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
