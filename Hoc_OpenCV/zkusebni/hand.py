
import cv2
from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_drawing


class HandTracker:

    def __init__(self, max_hands=2, detection_confidence=0.5, tracking_confidence=0.5):

        self.mp_hands = mp_hands
        self.mp_draw = mp_drawing

        # Thiet lap mo hinh nhan dien ban tay
        hands_options = {
            "static_image_mode": False,
            "max_num_hands": max_hands,
            "model_complexity": 1,
            "min_detection_confidence": detection_confidence,
            "min_tracking_confidence": tracking_confidence,
        }

        self.hands = self.mp_hands.Hands(**hands_options)

        self.results = None

    # Tim va ve cac diem tren ban tay
    def find_hands(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(rgb)

        # Lay danh sach ban tay duoc nhan dien
        hand_landmarks = getattr(
            self.results, "multi_hand_landmarks", None
        )

        if hand_landmarks:
            for landmarks in hand_landmarks:

                connections = list(self.mp_hands.HAND_CONNECTIONS)

                self.mp_draw.draw_landmarks(
                    frame,
                    landmarks,
                    connections
                )

        return frame

    # Kiem tra long ban tay co mo hay khong
    def is_palm_open(self, hand_landmarks):

        lm = hand_landmarks.landmark

        fingers = [(8, 6), (12, 10), (16, 14), (20, 18)]

        extended = sum(
            1 for tip, pip in fingers
            if lm[tip].y < lm[pip].y
        )

        return extended == 4

    # Tinh toa do trung tam long ban tay
    def get_palm_center(self, hand_landmarks, frame_shape):

        h, w, _ = frame_shape

        lm = hand_landmarks.landmark

        points = [0, 5, 9, 13, 17]

        x = sum(lm[i].x for i in points) / len(points)
        y = sum(lm[i].y for i in points) / len(points)

        return int(x * w), int(y * h)

    # Dong mo hinh va giai phong tai nguyen
    def close(self):

        self.hands.close()
