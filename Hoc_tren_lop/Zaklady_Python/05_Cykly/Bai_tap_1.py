'''
Bai tap 1: So hoan thien
'''

tong = 0
cac_so_hoan_thien = []
for i in range(2,1000):
    tong=0
    for j in range(1,i):
        if i%j==0:
            tong+=j
    if(tong==i):
        cac_so_hoan_thien.append(i)

for d in cac_so_hoan_thien:
    print(d,end=' ')
print(" ")

'''
Bai tap 2: kiem tra nam nhuan
'''
nam = int(input("nam: "))
nhuan = (nam,"la nam nhuan") if (nam%4==0 and nam%100!=0) or nam%400==0 else (nam,"khong phai la nam nhuan")
print(nhuan)
for d in range (2000,2100):
    if (d%4==0 and d%100!=0) or d%400==0 :
        print(d,end=" ")
print(" ")

'''
Bai tap 3: So nguyen to duoi 100
'''


def kiem_tra_nguyen_to (n):
    if n <= 1:
        return False  # Số <= 1 không phải số nguyên tố

    # Thử chia n cho các số từ 2 đến n - 1
    for i in range(2, n):
        if n % i == 0:
            return False  # Tìm thấy 1 ước số -> Không phải số nguyên tố

    return True  # Không chia hết cho số nào -> Là số nguyên tố

# 2. Dùng vòng lặp để in ra các số nguyên tố từ 2 đến 50

tong=0
print("Các số nguyên tố từ 2 đến 50 là:")
for i in range(2, 101):
    if kiem_tra_nguyen_to(i):
        tong+=i
        print(i, end=" ")
print(" ")

print(f"tong cac so nguyen to tu 2 den 100 la: {tong}")