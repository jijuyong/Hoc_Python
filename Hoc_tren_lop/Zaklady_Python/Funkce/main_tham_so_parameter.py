# loai 2 co tham so, ko return
def Tinh_tong(a,b):
    print(f"{a} + {b} = {a+b}")
# loai  1: ko tham so, ko return
def chao_morning():
    print("Morning")
#loai 3 - ko tham so, co return
def Luong():
    return 12000000
#loai 4 - co tham so, co return
def Tinh_hieu(a,b):
    return a-b

print("****loai 1: ko tham so, ko return****")
chao_morning()
print("****loai 2 co tham so, ko return****")
Tinh_tong(2,3)
print("****loai 3 - ko tham so, co return****")
print(f"luong dau vao cua ban la {Luong()}")
print("****loai 4 - co tham so, co return****")
print(f"2 - 3 = {Tinh_hieu(2,3)}")

#return - dung ham ngay lap tuc, minh co the loi dung de 'early return'
def Kiem_tra(so):
    if so<0:
        return "Am"
    elif so == 0 :
        return "khong"
    else:
        return "Duong "

#1.tham so bat buoc
def ham(a,b):
    print(f"{a} + {b} = {a+b}")

print("***tham so co gia tri mac dinh*******")
#2. tham so co gia tri mac dinh
def gioi_thieu(ten,quoc_tich="Viet nam",gioi_tinh="Nam"):
    print(f"{ten} - {quoc_tich} - {gioi_tinh}")

#nhung cach goi sau do
gioi_thieu("Hana")
gioi_thieu("Mimi","An Do","Nu")
gioi_thieu("hoa",quoc_tich="An Do")

##HAM NAC DANH - LAMBDA