import cv2

import numpy as np

photo = cv2.imread("images/920.jpg")

img = np.zeros((photo.shape[:2]), dtype='uint8')

circle = cv2.circle(img.copy(), (0, 0), 100, 255, -1)
square = cv2.rectangle(img.copy(), (55, 10), (640, 750), 255, -1)

img = cv2.bitwise_and(photo, photo, mask=square)

cv2.imshow('Photo', img)

cv2.waitKey(0)

