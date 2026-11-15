import cv2
import time
import numpy as np# xu ly mang toa do
import math
from pathlib import Path

from hand import HandTracker
from effects.fire import FireEffect
from effects.dragon import DragonEffect

# Thu muc chua file main.py
BASE_DIR = Path(__file__).resolve().parent
# Duong dan video
FIRE_VIDEO = BASE_DIR / "assets" / "Fire" / "fire.mp4"

def main():

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #dung moi 0 thi camera hay bi lag, cao_Dshow - Tăng tốc độ khởi động camera,Giúp fix một số lỗi vặt

    #Kiểm tra webcam có mở thành công không
    if not cap.isOpened():
        print("kog the mo camera!!!")
        return

    #Cài đặt kích thước và tốc độ camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    cap.set(cv2.CAP_PROP_FPS,30) #chay 30 khung/s

    #Khởi tạo HandTracker
    tracker = HandTracker()
    fire_effect = FireEffect(str(FIRE_VIDEO))
    dragon = DragonEffect()

    start_time = time.time()

    try:
        while True:

            #doc hinh anh tu webcam
            ret,frame = cap.read()

            if not ret:
                print("Khong the doc duoc hinh anh tu webcam")
                return

            #Lật hình ảnh theo chiều ngang - vi muon hinh anh hoat dong giong guong
            frame = cv2.flip(frame,1) # 1- lat ngang, 0 - lat doc, -1 lat ca hai chieu


            #Nhận diện và vẽ các điểm trên bàn tay
            frame = tracker.find_hands(frame)

            #Lấy kết quả nhận diện
            results = tracker.results

            if results is not None:
                hand_landmarks_list = getattr(
                    results,
                    "multi_hand_landmarks",
                    None
                )
            else: hand_landmarks_list = None

            if hand_landmarks_list:
                for hand_landmarks in hand_landmarks_list:
                    if (tracker.is_palm_up(hand_landmarks, frame.shape)and tracker.is_hand_open(hand_landmarks)):
                        center = tracker.get_hand_center(
                            hand_landmarks,
                            frame.shape
                        )

                        frame = fire_effect.draw(
                            frame,
                            center,
                            width=120
                        )
            # NHAN DIEN CU CHI TRIEU HOI RONG
            dragon_active = dragon.update(hand_landmarks_list,time.time())

            if dragon_active:
                cv2.putText(frame,"DRAGON SUMMONED!",(30, 60),cv2.FONT_HERSHEY_SIMPLEX,
                            1,(0, 165, 255),3)
            else:
                cv2.putText(
                    frame,
                    "Waiting for gesture....",
                    (30,60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 255),
                    2
                )
            #hien thi hinh anh nen man hinh
            cv2.imshow("HandTracker",frame)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
            # Giai phong tai nguyen
            tracker.close()
            fire_effect.close()
            cap.release()
            cv2.destroyAllWindows()
    
    
if __name__ == "__main__":
    main()
    




