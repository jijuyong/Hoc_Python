
print("*********Tham so *args*********")
#3. tham so co do dai thay doi *args
def tinh_tong(a,b,*phan_con_lai):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"phan con lai = {phan_con_lai}")

    tong = a+b
    for x in phan_con_lai:
        tong = tong+x
    return tong
print("*khi ko nhap phan con lai*")
print(f"tong = {tinh_tong(2,3)}")
#a=2 b=3, phan con lai = tuple (rong)
print("*khi nhap phan con lai*")
print(f"tong = {tinh_tong(1,2,3,4,5)}")
# a=1 b=2 phan con lai =3,4,5 -> tuple = (3,4,5)
