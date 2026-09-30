'''
4.1
tao list random
'''
from time import process_time_ns

n = int(input("moi nhap vao so phan tu ma ban muon tao: "))
list1 = []
import  random
for i in range(n):
    list1.append(random.randint(1,100))
print(list1)

'''
cach khac
a = int(input("moi nhap vao so phan tu ma ban muon tao: "))
n = random.randint(1,100)
list1 = []
for i in range(a):
    list1.append(n)
'''

'''
4.2
nhap 1 danh sach cac so nguyen
tao list chua cac cac so nguyen
list2 chua binh phuong cac so nguyen
den co bao nhieu phan tu lon hon 50
'''
list2 = []
n = int(input("So nhap so luong phan tu muon nhap: "))
for i in range(n):
    val = int(input(f"[{i+1}]: "))
    list2.append(val)
list3   =[]
for i in range(n):
    list3.append(list2[i]**2)
print("list goc")
print(list2)
print("binh phuong")
print(list3)
so  =0
for i in range(n):
    if list3[i]>50:
        so+=1
print(f"co {so} lon hon 50")


'''
4.3
nhap 1 list cac so nguyen, sau do:
#i: in ra co bao nhiu so nho hon 5
#2: in ra vi tri index cua cac so do
goi y: for i in range(len(lst)) de duyet theo index
'''
so =0
nau =  random.randint(1,10)
list4 = []
list5 = []
for i in range(5):
    list4.append(n)
    if list4[i]<5:
        so+=1
        list5.append(i)

print("List4")
print(list4)
print(f"co {so} nho hon 5")

'''
tach so chan va so le
'''
list_so = []
list_le = []
list_chan = []
number = int(input("So nhap so luong phan : "))
for i in range(number):
    aaaa = random.randint(1,100)
    list_so.append(aaaa)

for i in list_so:
    if i%2==0:
        list_chan.append(i)
    else:
        list_le.append(i)

print("List cac so: ",list_so)
print("List cac so le: ",list_le)
print("List cac so chan: ",list_chan)
