import cv2
import numpy as np
import math
import time

from hand import HandTracker


def draw_fire(frame, center, t):
    x, y = center

    overlay = frame.copy()
    h, w = frame.shape[:2]

    # Hieu ung anh sang xung quanh ngon lua
    cv2.ellipse(overlay, (x, y + 15), (55, 35), 0, 0, 360, (0, 100, 255), -1)

    # Tao nhieu ngon lua chuyen dong
    for i in range(9):
        offset = math.sin(t * 8 + i * 1.7) * 12
        height = 65 + math.sin(t * 5 + i) * 20

        base_x = int(x + (i - 4) * 10)
        tip_x = int(base_x + offset)

        base_y = y + 25
        tip_y = int(base_y - height)

        # Lua mau cam
        flame = np.array(
            [
                [base_x - 12, base_y],
                [base_x - 9, int(base_y - height * 0.45)],
                [tip_x, tip_y],
                [base_x + 12, int(base_y - height * 0.45)],
                [base_x + 12, base_y],
            ],
            np.int32,
        )

        cv2.fillPoly(overlay, [flame], (0, 110, 255))

        # Loi lua mau vang ben trong
        inner = np.array(
            [
                [base_x - 6, base_y],
                [base_x - 4, int(base_y - height * 0.35)],
                [tip_x, int(tip_y + height * 0.3)],
                [base_x + 6, int(base_y - height * 0.35)],
                [base_x + 6, base_y],
            ],
            np.int32,
        )

        cv2.fillPoly(overlay, [inner], (0, 220, 255))

    # Tron hieu ung vao camera
    cv2.addWeighted(overlay, 0.75, frame, 0.25, 0, frame)



def main():
    # Khoi dong webcam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Khong the mo webcam!")
        return

    # Cai dat kich thuoc va toc do camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    # Khoi tao HandTracker
    tracker = HandTracker()

    start_time = time.time()

    try:
        while True:

            # Doc hinh anh tu webcam
            success, frame = cap.read()

            if not success:
                print("Khong the doc hinh anh tu webcam!")
                break

            # Lat hinh anh theo chieu ngang
            frame = cv2.flip(frame, 1)

            # Nhan dien va ve cac diem tren ban tay
            frame = tracker.find_hands(frame)

            # Lay ket qua nhan dien
            results = tracker.results

            hand_landmarks_list = (
                getattr(results, "multi_hand_landmarks", None)
                if results is not None
                else None
            )

            # Kiem tra co ban tay duoc nhan dien hay khong
            if hand_landmarks_list:

                for hand_landmarks in hand_landmarks_list:

                    # Kiem tra long ban tay co mo hay khong
                    if tracker.is_palm_open(hand_landmarks):

                        # Tinh toa do trung tam long ban tay
                        center = tracker.get_palm_center(
                            hand_landmarks,
                            frame.shape
                        )

                        # Tinh thoi gian chay
                        t = time.time() - start_time

                        # Tao hieu ung lua tren ban tay
                        draw_fire(frame, center, t)

                        # Hien thi thong bao
                        cv2.putText(
                            frame,
                            "FIRE ACTIVATED!",
                            (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 140, 255),
                            2,
                        )

            # Hien thi hinh anh tren man hinh
            cv2.imshow("HAND TRACKER - FIRE POWER", frame)

            # Nhan Q de thoat
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        # Giai phong tai nguyen
        tracker.close()
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
