'''
Bài 1: Lời chào bằng sys.argv
Yêu cầu:
- Nếu không nhập tên thì in Lỗi: Hãy nhập tên.
- Nếu nhập Petr thì in Xin chào Petr.
'''

# import sys
import argparse

# if len(sys.argv)<2:
#     print("loi, hay nhap ten")
# if sys.argv[1]=="Petr":
#     name= sys.argv[1]
#     print(f"Xin chao {sys.argv[1]}")


'''
Bài 2: Lũy thừa bằng argparse
Đề bài yêu cầu:
- Đối số bắt buộc so kiểu int.
- Đối số tùy chọn --luy-thua kiểu int.
- Giá trị mặc định của --luy-thua là 2.
- In kết quả phép lũy thừa.
'''

parser = argparse.ArgumentParser(description="Lũy thừa bằng argparse")

parser.add_argument("so",type=int,help="Nhap so can tinh")
parser.add_argument("--luy_thua",type=int,default=2,help="Nhap so mu: ")

args = parser.parse_args()

result = args.so**args.luy_thua
print(f"{args.so} mu {args.luy_thua} la: {result}")
