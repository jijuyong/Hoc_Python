import cv2

cap = cv2.VideoCapture(0)# neu co nhieu cam thi them id webcam 1,2,3
#cap = cv2.VideoCapture("video.mp4") mo video

'''
ret(return) - tra ve flase/true, cho biet doc hinh anh co thanh cong hay khog
fram - chua hinh anh vua doc duoc tu camera hoac video
'''
while True:
    ret,frame = cap.read()

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        # ord() - chuyen ky tu thanh ma so Unicode
        break
cap.release() # giai phong camera
cv2.destroyAllWindows()# thoat cac cua so

