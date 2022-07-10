import cv2
import numpy as np

img = cv2.imread('images/920.jpg')


# print(img.shape)

# new_size = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))

cv2.imshow('show', img)
# img = cv2.flip(img, 1)
#
# # img = cv2.GaussianBlur(img, (7, 7), 0)
# # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #
# # img = cv2.Canny(img, 100, 100)
# # kernel = np.ones((5, 5), np.uint8)
# #
# # img = cv2.dilate(img, kernel, iterations=2)
# # img = cv2.erode(img, kernel, iterations=1)
# # #
# # cv2.imshow('show', img)
# # print(img.shape)
# cv2.waitKey(0)

# cap = cv2.VideoCapture('videos/car.mp4')
# cap = cv2.VideoCapture(0)  # обращение к веб камере
# cap.set(3, 2000)
# cap.set(4, 2000)
#
# while True:
#     success, img = cap.read()
#     # img = cv2.flip(img, 1)
#     # img = cv2.GaussianBlur(img, (7, 7), 0)
#     # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # img = cv2.Canny(img, 40, 40)
#     # kernel = np.ones((5, 5), np.uint8)
#     #
#     # img = cv2.dilate(img, kernel, iterations=1)
#     # img = cv2.erode(img, kernel, iterations=1)
#     print(img)
#
#     cv2.imshow('show', img)
#     cv2.waitKey(0)
#
#     # if cv2.waitKey(33) & 0xFF == ord('q'):
#     #     break
#
#     if 0xFF == ord('q'):
#         break

# def rotate(img_in, angle):
#     height, width = img_in.shape[:2]
#     point = (width // 2, height // 2)
#
#     math = cv2.getRotationMatrix2D(point, angle, 1)
#     return cv2.warpAffine(img_in, math, (width, height))
#
#

# img = cv2.imread('images/920.jpg')
# new_img = np.zeros(img.shape, dtype='uint8')
#
# b, g, r = cv2.split(img)
#
# img = cv2.merge([b, b, r])
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
# img = cv2.GaussianBlur(img, (7, 7), 0)
#
# img = cv2.Canny(img, 100, 140)
# con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#
# cv2.drawContours(new_img, con, -1, (255, 0, 0), 1)


# cv2.imshow('show', img)
# cv2.waitKey(0)
