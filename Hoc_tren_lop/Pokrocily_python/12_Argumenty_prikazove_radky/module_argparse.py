'''MODULE ARGPARSE - Cách chuyên nghiệp hơn'''
#Bước 1 – Import argparse
import argparse

#Bước 2 – Tạo Parser
parser = argparse.ArgumentParser(description="Chương trình tính tuổi")
'''
parser có thể hiểu là bộ phân tích các đối số người dùng nhập vào.
description là phần mô tả chương trình.
'''

# Bước 3 – add_argument() - có nghĩa là thêm một đối số mà người dùng được phép truyền vào.
parser.add_argument("ten")

'''Đối số bắt buộc và tùy chọn'''
#A. Đối số bắt buộc (Positional Argument)
'''
Ví dụ: parser.add_argument("ten")
- Không có dấu --
- Khi chạy 'python main.py Petr' -> Chương trình nhận được tên Petr
- Nhưng nếu chạy: python main.py -> Chương trình báo lỗi vì thiếu đối số bắt buộc.
'''
parser.add_argument("tuoi")
# B. Đối số tùy chọn (Optional Argument)
'''
vd: parser.add_argument("--tuoi")
- Khi chạy: python main.py Petr --tuoi 25
    Chúng ta có:
        Petr: Tên.
        --tuoi: Tên đối số tùy chọn.
        25: Giá trị của tuổi.
'''
parser.add_argument("--adress")

# sau khi nhap ten , Python sẽ lấy được giá trị ten, Sau đó chúng ta lấy dữ liệu bằng:
args = parser.parse_args()
print(args.ten)
if args.adress is not None:
    print(f"adress: {args.adress}")
print(f"age: {args.tuoi}")
# Đây là cách lấy dữ liệu từ đối số mà chúng ta đã khai báo bằng add_argument("ten").
'''type=int – Chuyển kiểu dữ liệu'''
