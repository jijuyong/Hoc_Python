import cv2
import numpy as np # lm viec vs data so, xu ly anh va video
cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3)) # ra chieu rongq
    height = int(cap.get(4)) # ra chieu daiq

    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # thu nho hinh anh xuong con 50%
    image = np.zeros(frame.shape, np.uint8)
    # frame.shape - tra ve khoi to bang cam

    # chia frame to thanh 4 hinh nho, roi dan dan do moi small frame vao goc cua fram to
    image[:height//2,:width//2] = small_frame
    image[:height//2,width//2:] = cv2.rotate(small_frame,cv2.ROTATE_180)
    image[height//2:,:width//2] = cv2.rotate(small_frame,cv2.ROTATE_180)
    image[height//2:,width//2:] = small_frame

    cv2.imshow("frame",image)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()