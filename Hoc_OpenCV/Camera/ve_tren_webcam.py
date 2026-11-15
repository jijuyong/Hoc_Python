import cv2

cap = cv2.VideoCapture("video.mp4")

while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # code ve line
    '''
    cv.rectangle(frame, (0,0), (width,height), (0,255,0), 0)
    - frame - anh hoac khung hinh video dau vao
    - (0,0) - toa do goc ben trai - diem ket thuc
    - (widght, height) - toa do goc duoi ben trai
    - (0,255,0) - mau xanh la cay
    - 0 - de day cua net ve
    '''

    #ve line
    img=cv2.line(frame, (0,0), (width,height), (0,0,0), 5)
    img1=cv2.line(frame, (0,height), (width,0), (0,0,0), 5)
    img2 = cv2.circle(frame,(width//2,height//2), 50, (0,0,0),5)
    #ve hinh chu nhat , neu do day la -1 thi ca hinh se co mau ma
    img = cv2.rectangle(frame, (100,100),(400,400),(0,255,0),-1)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()