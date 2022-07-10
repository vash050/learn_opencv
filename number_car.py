import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img = cv2.imread("images/car_2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

filters = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(filters, 30, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 8, True)
    if len(approx) == 4:
        pos = approx
        break

print(pos)
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

pl.imshow(cv2.cvtColor(bitwise_img, cv2.COLOR_BGR2RGB))
pl.show()
