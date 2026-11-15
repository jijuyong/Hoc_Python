
import math


class DragonEffect:

    def __init__(self):
        self.active = False
        self.gesture_start = None
        self.hold_duration = 0.7

    def is_dragon_gesture(self, hands):
        if hands is None or len(hands) != 2:
            return False

        hand_data = []

        for hand in hands:
            lm = hand.landmark

            # Ngón trỏ duỗi
            index_extended = (
                math.dist((lm[8].x, lm[8].y), (lm[0].x, lm[0].y))
                >
                math.dist((lm[6].x, lm[6].y), (lm[0].x, lm[0].y)) * 1.1
            )

            # Ba ngón còn lại gập
            folded_count = 0

            for tip, pip in [(12, 10), (16, 14), (20, 18)]:
                tip_dist = math.dist(
                    (lm[tip].x, lm[tip].y),
                    (lm[0].x, lm[0].y)
                )

                pip_dist = math.dist(
                    (lm[pip].x, lm[pip].y),
                    (lm[0].x, lm[0].y)
                )

                if tip_dist < pip_dist * 1.15:
                    folded_count += 1

            # Tâm bàn tay
            palm = (
                (lm[0].x + lm[5].x + lm[17].x) / 3,
                (lm[0].y + lm[5].y + lm[17].y) / 3
            )

            index_tip = (lm[8].x, lm[8].y)

            hand_data.append({
                "extended": index_extended,
                "folded": folded_count,
                "palm": palm,
                "tip": index_tip
            })

        # Cả hai ngón trỏ phải duỗi
        if not all(h["extended"] for h in hand_data):
            return False

        # Mỗi tay có ít nhất 2 ngón còn lại gập
        if not all(h["folded"] >= 2 for h in hand_data):
            return False

        # Hai bàn tay phải ở gần nhau
        palm_distance = math.dist(
            hand_data[0]["palm"],
            hand_data[1]["palm"]
        )

        return palm_distance < 0.30

    def update(self, hands, current_time):
        gesture = self.is_dragon_gesture(hands)

        if gesture:
            if self.gesture_start is None:
                self.gesture_start = current_time

            if current_time - self.gesture_start >= self.hold_duration:
                self.active = True
        else:
            self.gesture_start = None
            self.active = False

        return self.active
