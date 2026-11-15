
import cv2
import numpy as np


class FireEffect:
    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.isOpened():
            raise RuntimeError(
                f"Khong the mo video lua: {video_path}"
            )

        self.low = 8
        self.high = 100

    def get_frame(self):
        # Doc frame tiep theo
        success, frame = self.cap.read()

        # Neu het video thi phat lai tu dau
        if not success:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, frame = self.cap.read()

        if not success:
            return None

        # Tao alpha tu do sang cua ngon lua
        brightness = np.max(frame, axis=2)

        alpha = (
            (brightness.astype(np.float32) - self.low)
            / (self.high - self.low)
        )

        alpha = np.clip(alpha, 0, 1)
        alpha = (alpha * 255).astype(np.uint8)

        # Tao anh BGRA
        fire_rgba = cv2.cvtColor(
            frame, cv2.COLOR_BGR2BGRA
        )

        fire_rgba[:, :, 3] = alpha

        return fire_rgba

    def draw(self, background, center, width=180):
        fire = self.get_frame()

        if fire is None:
            return background

        # Giu nguyen ti le video
        old_h, old_w = fire.shape[:2]
        height = int(old_h * width / old_w)

        fire = cv2.resize(
            fire, (width, height),
            interpolation=cv2.INTER_AREA
        )

        # Dat day ngon lua tai long ban tay
        x = int(center[0] - width / 2)
        y = int(center[1] - height)

        # Gioi han vung anh de khong vuot webcam
        h, w = background.shape[:2]

        x1 = max(0, x)
        y1 = max(0, y)
        x2 = min(w, x + width)
        y2 = min(h, y + height)

        if x1 >= x2 or y1 >= y2:
            return background

        # Vung tuong ung cua ngon lua
        fx1 = x1 - x
        fy1 = y1 - y
        fx2 = fx1 + (x2 - x1)
        fy2 = fy1 + (y2 - y1)

        overlay = fire[fy1:fy2, fx1:fx2]

        # Tach mau va alpha
        fire_color = overlay[:, :, :3].astype(np.float32)
        alpha = overlay[:, :, 3:4].astype(
            np.float32
        ) / 255.0

        roi = background[y1:y2, x1:x2].astype(
            np.float32
        )

        # Ghep ngon lua len webcam
        result = (
            fire_color * alpha
            + roi * (1 - alpha)
        )

        background[y1:y2, x1:x2] = np.clip(
            result, 0, 255
        ).astype(np.uint8)

        return background

    def close(self):
        self.cap.release()
