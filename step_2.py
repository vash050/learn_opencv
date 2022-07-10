import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1000)
cap.set(4, 1000)

while True:
    success, img = cap.read()
    cv2.imshow('res', img)
    cv2.waitKey(1)

    # if cv2.waitKey(33) & 0xFF == ord('q'):
    #     break
