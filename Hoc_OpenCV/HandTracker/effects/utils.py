
import cv2
import numpy as np


def apply_glow(frame, overlay, blur_size=25, intensity=1.5):
    """
    frame: Hình ảnh webcam gốc
    overlay: Lớp hình ảnh chứa hiệu ứng
    blur_size: Độ rộng vùng phát sáng
    intensity: Cường độ ánh sáng
    """

    # Làm mờ lớp hiệu ứng để tạo quầng sáng
    glow = cv2.GaussianBlur(
        overlay,
        (blur_size, blur_size),
        0
    )

    # Ghép quầng sáng vào hình ảnh gốc
    frame = cv2.addWeighted(
        frame, 1.0,
        glow, intensity,
        0
    )

    # Ghép lại các chi tiết sắc nét của hiệu ứng
    frame = cv2.addWeighted(
        frame, 1.0,
        overlay, 0.8,
        0
    )

    return frame
