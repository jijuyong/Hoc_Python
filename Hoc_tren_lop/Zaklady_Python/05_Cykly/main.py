#--------------1. Vòng lặp for--------------
print("Vong for 1 tham so")
for i in range (20):
    print(i,end=" ")
print("")

print("Vong for 2 tham so")
for i in range (10,20):
    print(i,end=" ")
print("")
print("Vong for 3 tham so")
for i in range(0,10,2):
    print(i,end=" ")
print("")
#---------duyet chuoi---------
print("Duyet chuoi")
for ky_tu in "Python":
    print(ky_tu,end=" ")
print("")

#--------------2.Vòng lặp while--------------
mat_khau =""

while mat_khau != "tajne123":
    mat_khau = input("Nhập mật khẩu: ")

#--------------3.Điều khiển luồng vòng lặp--------------
#---break----
print("Vong for dung break")
a = 5
for i in range(15):
    print(a,"*",i,"=",a*i)
    if i==12: break
#----continue-----
print("Vong for dung continue")
a = 5
for i in range(15):
    if i==12:
        continue
    print(a,"*",i,"=",a*i)
#----pass-----
tuoi = 18

if tuoi < 18:
    print("Chưa đủ tuổi")
elif tuoi == 18:
    pass  # Chưa làm gì với trường hợp đúng 18 tuổi
else:
    print("Đã đủ tuổi")

#--------------4. Nhánh else trong vòng lặp--------------
for so in range (5):
    if so ==10:
        print("Da tim thay")
        break
    else:
        print("Không tìm thấy (đã duyệt hết vòng lặp)")
        break

#--------------5. Vòng lặp lồng nhau (Nested Loops)--------------
for hang in range(3):
    for cot in range(3):
        print(f"[{hang},{cot}]", end=" ")
    print() # Xuống dòng

#--------------6. Ham Dem so phan tu len()--------------
fruit = ["banana","apple","watermelon"]
print(f"trong fruit co: {len(fruit)} qua")
for index in range(len(fruit)):
    print(fruit[index],end=" ")
print(" ")

#--------------7. For else--------------
for so in range (1,4):
    print(so)
else:
    print("vong lap for chay binh thuong")

for so in range (1,4):
    if so == 2:
        break
    print(so)
else:
    print("vong lap for chay binh thuong")# vi break khi gap 2 nen cua lenh o else se khong duoc in ra

#--------------lap qua list--------------
diem = [8,9.5,7,10]
tong =0
for d in diem:
    tong+=d
print(tong)

# for d in range(len(diem)):
#     tong+=diem[d]
# print(tong)