#cach khai bao tuple
from itertools import count
from time import process_time

t1 = (1,2,3,"python",False)
t2 = ()

print("t1: ",t1)
print("t2: ",t2)
print("type cua t1 la: ",type(t1))

#khi khao bao typle 1 phan tu
t3 = (132)
print("type cua t3 khi khong them dau phay dang sau: ",type(t3))
t4 = (135,)
print("type cua t4 khi them dau phay dang sau: ",type(t4))

#index giong list
t5 =         (1 , 2 , 3 , 4 , 5)
#index duong: 0 , 1 , 2 , 3 , 4
#index am:   -5 , -4, -3, -2, -1
print(f"t5[3]:{t5[3]}")
print(f"t5[-3]:{t5[-3]}")

# slicing
t6 = ("p","y","t","h","o","n")
print(f"in tat ca {t6[:]}")
print(f"in tu index 3 {t6[3:]}")
print(f"in tu index 3->5 {t6[3:5]}")
print(f"in tu index 0->4 nhay 2 {t6[0:5:2]}")
print(f"in dem index 4 {t6[:5]}")
print(f"in nguoc {t6[::-1]}")

#khong the thay doi phan tu
t7 = (1,2,3,4)
#t[0] =88 se bi loi

#khong xoa duong tung phan tu,nhung xoa ca tuple thi duoc
# del t7[0]
# print(t7) se bi error bi in t7

del t7 # nhung ko in dc ra vi da xoa di roi

#cac ham
t8 = (17,23,64,449,2,330,77,23)
print(f"so luong phan tu trong t8 la: {len(t8)}")
print(f"max trong t8 la: {max(t8)}")
print(f"min trong t8 la: {min(t8)}")
print(f"so lan 23 xuat hien trong tuple la: {t8.count(23)} ")
print(f"lam dau tien 23 xuat hien trong tuple la: {t8.index(23)} ")
list1 = list(t8)
print("sau khi chuyen tuple8 sang list")
print(list1)

#toan tu
tuple1 = (1,2,3)
tuple2 = ("a","b","c")
print(f"tuple1 + tuple2 = {tuple1+tuple2}")
print(f"tuple2 *3: {tuple2*3}")
print(f"a co trong tuple2 ko: {"a" in tuple2}")
print(f"b co trong tuple2 ko: {"a" not in tuple2}")

'''
LY DO DUNG TUPLE
- du lieu KHONG NEN thay doi
- ham tra ve nhieu gia tri - python tu dong goi 
- tuple nhanh hon - python toi uu bo nho
tuple dung lam key Dict dk, nhung list thi khongx
'''