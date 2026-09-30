# -------ham printf-----------
from traceback import print_tb

print("Hello World")
print('Hello World')
print("Hello" "World")
print(123)
# Kết quả: 10:20:30 (trên cùng một dòng)
print(10, 20, 30, sep=":")
# Kết quả: Xin chào... (con trỏ vẫn ở cùng một dòng)
print("Xin chào", end="...")
print("\n")
# ctrl + D de copy

#noi chuoi
print("ten"+" toi")
#-----------Định dạng chuỗi (f-string)-------------
ten = "Stepan"
tuoi = 25
tuoitoi = 20

'''
Cách cũ (không khuyến khích nếu không cần thiết)
print("Tên là", ten, "và", tuoi, "tuổi")
'''

# Cách hiện đại (f-string)
print(f"Toi tên là {ten} và {tuoi} tuổi.")

#nhap thong tin tu ban phim
ngay_le = input("nhap ngay le: ")
nguoi_gui = input("nhap nguoi gui: ")
nguoi_nhan = input("nhap nguoi nhan: ")
#input gia tri nguoi dung nhap vao luc nao cung la chuoi , nen neu nhap so phai ep
print("-*-*"*10)
print(f"nhan dip {ngay_le}")
print(f"nguoi gui: {nguoi_gui}")
print(f"chuc nguoi nhan {nguoi_nhan} co dip nghi le vui ve")
print("-*-*"*10)

#hoac la co the viet nhu the nay
print("-*-*"*10)
print("nhan dip " + ngay_le)
print(f"nguoi gui: " +nguoi_gui)
print(f"chuc nguoi nhan " +nguoi_nhan+" co dip nghi le vui ve")
print("-*-*"*10)



