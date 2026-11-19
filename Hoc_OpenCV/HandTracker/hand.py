import cv2
import numpy as np
from mediapipe.python.solutions import hands as mp_hands #find hands, 21 points of the hands, tracking hands
from mediapipe.python.solutions import drawing_utils as mp_drawing # ve cac diem noi tren ban tay

class HandTracker:
    def __init__(self, pocet_ruka=2,dections=0.5,tracking=0.5):
        self.mp_hands = mp_hands
        self.mp_draw = mp_drawing
        # luu thu vien vao cac doi tuong


        hands_options = { # thiet lap mo hinh
            "static_image_mode": False,
            #true - cho hinh anh tinh
            "max_num_hands": pocet_ruka, 
            "model_complexity": 1,
            # do phuc tap cua mo hinh, 
            "min_detection_confidence": dections,
            #mô hình cần đạt mức tin cậy tối thiểu 50% để chấp nhận phát hiện
            "min_tracking_confidence": tracking,
            #Ngưỡng tin cậy tối thiểu khi theo dõi bàn tay giữa các frame.
        }

        self.hands = self.mp_hands.Hands(**hands_options)
        '''tao ra mo hinh nhan dien ban tay
        ** - cách truyền các phần tử của dictionary vào hàm dưới dạng tham số có tên.
        vd: def hello(name,age): print(name,age)
            
            data = {
                "name":"Nam"
                "age": 20}
            hello(**data)
            znamena hello(name="Nam",age=20)
        '''
        self.results = None # ket qua nhan dien ban tay


    def find_hands(self,frame):
        rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # vi mediapipe dung rgb con cv2 dug bgr nen phai doi sag rgb
        self.results = self.hands.process(rgb)# goi mo hinh de xu ly hinh anh
        '''
        Các bàn tay được phát hiện.
        21 điểm tọa độ của từng bàn tay.
        '''

        #buoc3: lay danh sacch ban tay
        hand_landmarks = getattr(self.results,"multi_hand_landmarks",None)
        '''ham getattr(object,attribute,defaultf) - Nó có tác dụng lấy một thuộc tính của đối tượng- dung cho object
            - Nếu có danh sách bàn tay thì lấy danh sách đó.
            - Nếu không có thì trả về None
        '''

        #buoc 4: Kiểm tra có bàn tay hay không
        if hand_landmarks:
            #BUOC5: #duyet tung ban tay
            for landmarks in hand_landmarks:
                #buoc 6: Lấy các đường kết nối
                connections = list(self.mp_hands.HAND_CONNECTIONS)

                #buoc 7: ve ban tay
                self.mp_draw.draw_landmarks(frame,landmarks,connections)
                # (Hình ảnh cần vẽ,Các điểm trên bàn tay,Các đường nối giữa các điểm)

        #buoc 8: tra ve hinh anh
        return frame

    def is_palm_open(self,hand_landmarks):
        # hand_landmarks - dữ liệu các điểm trên bàn tay
        lm = hand_landmarks.landmark
        '''trong do lm[0] lm[1].....lm[20] - Mỗi phần tử là một điểm tọa độ trên bàn tay.
            - Một điểm có 3 thành phần chính:
                ~ lm[i].x - Tọa độ ngang.
                ~ lm[i].y - Tọa độ dọc.
                ~ lm[i].z - - Độ sâu tương đối.
        '''

        #buoc2: Xác định các ngón tay
        fingers = [(8,6),(12,10),(16,14),(20,18)]
        '''
        Trỏ - Đầu ngón(8) - Khớp gần đầu ngón(6)
        Giữa - Đầu ngón(12) - Khớp gần đầu ngón(10)
        Áp út - Đầu ngón(16) - Khớp gần đầu ngón(14)
        Út - Đầu ngón(20) - Khớp gần đầu ngón(18)
        '''

        #buoc3: Kiểm tra ngón tay đang duỗi
        extended = 0
        for tip,pip in fingers:
            if lm[tip].y < lm[pip].y:
                extended+=1
        '''
        Lấy tọa độ đầu ngón tay.
        So sánh với tọa độ khớp của ngón tay.
        Nếu đầu ngón nằm cao hơn khớp thì cộng thêm 1.
        - proc <?
            Phía trên có giá trị y nhỏ.
            Phía dưới có giá trị y lớn
            vd lm[8] = 0,2  lm[6] = 0.4 co nghia la ngon tro đang duỗi.
        '''

        # Bước 4: Kết luận bàn tay mở hay không
        return extended ==4# Nếu cả 4 ngón tay được kiểm tra đều duỗi thì trả về True.

    # Tính tâm lòng bàn tay
    def get_hand_center(self,hand_landmarks, frame_shape):
        #Bước 1: Lấy chiều cao và chiều rộng ảnh
        h,w,_ = frame_shape
        '''vd fame_shape(480,640,3) - h=480, w = 640 , _ = 3 - co 3 kenh mau
        tai sao lai dung '_' - vi chúng ta không cần quan tâm đến giá trị đó.
        '''

        #Bước 2: Lấy danh sách điểm
        lm = hand_landmarks.landmark 

        #Bước 3: Chọn các điểm để tính tâm
        point = [0,5,9,13,17]
        '''
        Chúng ta chọn 5 điểm:
            - 0: Cổ tay.
            - 5: Gốc ngón trỏ.
            - 9: Gốc ngón giữa.
            - 13: Gốc ngón áp út.
            - 17: Gốc ngón út.
        '''

        #Bước 4: Tính trung bình tọa độ X v Y
        x = sum(lm[i].x for i in point)/len(point)
        y = sum(lm[i].y for i in point) / len(point)

        '''
        .x va .y - do mediapipe tra ve khoảng từ 0.0 đến 1.0
        vd :
        - mediapipe trả về tọa độ .x của 5 điểm lần lượt là:[(0:0.40) (5:0.45) (9:0.50) (13:0.55) (17:0.60)]
        - sum(x) = 2.50 , tinh ty le tb 2.50/5 = 0.50
        - Tính tọa độ Pixel X thực tế = (0.50*640) = 320
        '''
        #Bước 5: Chuyển tọa độ về pixel
        '''
        MediaPipe trả về tọa độ chuẩn hóa từ 0 đến 1.
        Trong khi đó OpenCV sử dụng tọa độ pixel.
        '''
        return int(x*w), int(y*h)

    def is_palm_up(self, hand_landmarks, frame_shape):
        h, w = frame_shape[:2] # lay hai phan tu dau tien, ke phan tu thu 3
        lm = hand_landmarks.landmark

        # Lay 3 diem tren long ban tay
        wrist = np.array([
            lm[0].x * w,
            lm[0].y * h,
            lm[0].z * w
        ])

        index_mcp = np.array([
            lm[5].x * w,
            lm[5].y * h,
            lm[5].z * w
        ])

        pinky_mcp = np.array([
            lm[17].x * w,
            lm[17].y * h,
            lm[17].z * w
        ])

        # Tao hai vector tren mat phang long ban tay
        v1 = index_mcp - wrist
        v2 = pinky_mcp - wrist

        # Tinh vector phap tuyen cua long ban tay
        normal = np.cross(v1, v2)

        length = np.linalg.norm(normal)

        if length < 1e-6:
            return False

        normal = normal / length

        # Mat phang long ban tay gan nam ngang
        # thi vector phap tuyen gan truc doc cua camera
        return abs(normal[1]) > 0.65

    def is_hand_open(self, hand_landmarks):
        lm = hand_landmarks.landmark

        wrist = np.array([
            lm[0].x,
            lm[0].y
        ])

        fingers = [
            (8, 6),    # Ngon tro
            (12, 10),  # Ngon giua
            (16, 14),  # Ngon ap ut
            (20, 18)   # Ngon ut
        ]

        extended_count = 0

        for tip_id, pip_id in fingers:
            tip = np.array([
                lm[tip_id].x,
                lm[tip_id].y
            ])

            pip = np.array([
                lm[pip_id].x,
                lm[pip_id].y
            ])

            # Khoang cach tu dau ngon tay den co tay
            tip_distance = np.linalg.norm(tip - wrist)

            # Khoang cach tu khop giua den co tay
            pip_distance = np.linalg.norm(pip - wrist)

            if tip_distance > pip_distance * 1.15:
                extended_count += 1

        # Can it nhat 3/4 ngon tay duoc duoi
        return extended_count >= 3


    #8. Hàm close() – Giải phóng tài nguyên
    def close(self):
        self.hands.close()



