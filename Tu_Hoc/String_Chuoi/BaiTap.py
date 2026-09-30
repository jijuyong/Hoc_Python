'''
Dem am nguyen 'a' 'e' 'i' 'o'
'''
s = 'Lap trinh Python rat thu vi'
s1 ='aeio'
tong =0
for c in s1:
    for d in s:
        if c == d:
            tong+=1
    print(f"chu '{c}' xuat hien {tong} lan")
    tong =0
print("-"*40)
'''
dem s thuonng va hoa
'''
s2 = 'Samsung'
s3 = 's'
for c in s2:
    if c == s3 and c!=s3.upper():
        tong+=1
    elif c == s3.upper():
        tong+=1
    else : continue
    print(f"chu '{c}' xuat hien {tong} lan")

#hoac
print(s2.count('s'))
print(s2.count('S'))
print("-"*40)

'''Tach chuoi bang split'''
#tach huong va so buoc
Lenh = input("lenh: ")
huong = Lenh.split()
so = 0
if len(huong)>2:
    so = int(huong[2])
    print(f"Di {huong[0]} {huong[1]} {so}  buoc")
else:
    so = int(huong[1])
    print(f"Di {huong[0]} {so}  buoc")
print("-"*40)
''' Tach theo duoi phay. lay ten, tuoi, thanh pho'''
TT = (input("moi ban nhap thong tin ca nhan: ")).split(',')
ten = TT[0]
tuoi = TT[1]
thanh_pho = TT[2]
print(f"Ten {ten}, tuoi {tuoi}, thanh pho {thanh_pho}")

#hoac
# ten,tuoi,thanh_pho = TT.split(',')
# print(f"Ten {ten}, tuoi {tuoi}, thanh pho {thanh_pho}")


'''
Dem chua 'a', tim vi tri 'n' dau tien, tim 'z' (an toan)
'''

print("-"*40)
s3 = 'banana'
print(f"co {s3.count('a')} chu 'a' trong s3")
print(f"vi tri index dau tien cua 'n' la [{s3.find('n')}]")
print(f"vi tri index dau tien cua 'z' la [{s3.find('z')}]")

'''
Loc file va ktra ma trong danh sach
'''
print("-"*40)
files = ["bao_cao.pdf","anh.png","ghichu.txt","du_lieu.pdf"]
print("cac file kthuc voi duoi .pdf la: ",end="")
for f in files:
    if f.endswith(".pdf"):
        print(f,end=" ")
print("")

''' kiem tra ma hop le'''
ma_dung = ["6B","7C","AB"]
ma_nguoi_nhap =""
while ma_nguoi_nhap != ma_dung:
    ma_nguoi_nhap = input("MOI BAN NHAP VAO MA DE KIEM TRA: ")
    if ma_nguoi_nhap in ma_dung:
        print("hop le, ban da thong qua")
        break
    else:
        print("khong hop le,MOI NHAP LAI")



