'''
Lambda la cach tao ham nho, khong dung 1 lan bang 1 dong
'''

'''Cu Phap
lambda tham_so_1, tham_so_2 : bieu thuc tra ve
'''

# so sanh def va lambda

#cach 1: def thong thuong
def cong1(a,b):
    return a+b

#cach 2: lambda - tuong duong, ngan hon
cong2 = lambda a,b: a+b

print(f"phep cong dung def: {cong1(3,4)}")
print(f"phep cong dung lambda: {cong2(5,4)}")

#lambda khong tham so
print("***** Lambda khong tham so *****")
chao = lambda: "Xin chao!"
print(chao())

#lambda voi 1 tham so
print("***** Lambda voi 1 tham so *****")
binh_phuong = lambda x: x**2
print(binh_phuong(5))

