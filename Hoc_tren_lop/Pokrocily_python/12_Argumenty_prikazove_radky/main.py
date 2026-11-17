'''
vd: python main.py Petr --tuoi 25
Petr - Tên được truyền vào chương trình.
--tuoi 25: Đối số tuổi được truyền vào
'''

#cach 1: sys.argv
import sys

name = sys.argv[1]
#Nhược điểm 1: Tất cả đều là chuỗi (string).
age = int(sys.argv[2])
'''Nhược điểm 2: Phải tự xử lý lỗi.
Ví dụ bạn chạy (run), Python sẽ báo lỗi: IndexError: list index out of range
Vì bạn chưa nhập tên nhưng chương trình lại cố lấy phần tử thứ nhất.
'''
if len(sys.argv)<2:
    print("loi hay nnhap ten")
else:
    name =sys.argv[1]
    print(f"my name is {name}, I'm {age} years old")

'''MODULE ARGPARSE - Cách chuyên nghiệp hơn'''
