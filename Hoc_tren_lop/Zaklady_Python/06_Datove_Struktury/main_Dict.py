#cach khai bao 1
from os import remove
d = {
    "mot":1,
    "hai" :2,
    "ba":3
}
print("dict: ",d)
print("type cua d: ",type(d))


#cach 2
'''
key PHAI la chuoi hop le nhu ten bien
- khong ngoac kep, dau cach
- khong bat dau bang so
'''
car = dict( brand="Honda", model="Civil", year=1972)
print("----------------------------------")
print(car)

# Dict long nhau - value co the la dict khac
school = {
    'office':{'room1':'Finance','room2':'Logistics'},
    'lab':{'lab1':'physics','lab2':'Chemistry'}
}

'''key phai la bien : string, int, tuple
khong duoc: list, dict,set
vd: d = {[1,2] : "list"}
'''

'''
Key khong duoc trung lap
d = {"a":1, "b":2, "a":99}
sau khi in ra a dau tien se co value la 99
'''

'''
key phan biet kieu du lieu
d = {1:"int", "1":"string"}
print(len(d)) // se bang 2
'''

#truy cap gia tri
#cach 1
print("----------------------------------")
print(f"ten brand cua car la: {car["brand"]}")
print(f"nam san xuat cua car la: {car["year"]}")
# print(f"nam san xuat cua car la: {car["color"]}") se bi loi vi color ko existuje

#cach 2 - an toan hon thong qua get
print(f"model cua car la: {car.get("model")}")
print(car.get("color","N/A"))# co the gan gia tri cho key ko tton tai

#them, sua, xoa

d1 = {"a":1, "b":2}
d1["c"] =3 # them moi
d1["a"] =99 # sua value
del d1["b"] # xoa
print(d1) # {'a':99, 'c':3}

#duyet key
print("----------------------------------")
print("vong for duyet dict car")
for key in car:
    print(key,":",car[key])

#duyet key + value khuyen nen dung
print("----------------------------------")
print("vong for duyet key va value")
for key, value in car.items():
    print(key,":",value)

#for chi duyet value
print("----------------------------------")
print("vong for duyet value")
for v in car.values():
    print(v)

# cac methods chinh
# .key()
print("----------------------------------")
print(f"method duyet qua tat ca cac keys: {car.keys()}")
#.value()
print("----------------------------------")
print(f"method duyet qua tat ca cac values: {car.values()}")
#.items()
print("----------------------------------")
print(f"method duyet qua tat ca cac keys:value : {car.items()}")
#----.update(dict2) - gop dict2 vao (them + ghi de)
print("----------------------------------")
car.update({"color":"red","price":2100})
print(f"Dict car sau update: {car}")

#------.pop(key) - xoa key, tre ve value da xoa
print("----------------------------------")
removed = car.pop("color")
print(f"gia tri da xoa: {removed}")
print(car)

#------.popitem() - xoa last pair
print("----------------------------------")
last = car.popitem()
print(f"cap key:value cuoi cung da bi xoa la: {last}")
print(car)
#-----.setdefault(key,val) - lay value, chua co -> tu them
print("--------------------------------")
car.setdefault("color","Black")
#key "color" chua co -> them "color":"Black"
car.setdefault("brand","Toyota")
#key "brand" da co -> khong ghi de (Honda giu nguyen)

#----- in - kiem tra ton tai | .copy() | .clear()
print("brand" in car)
car2 = car.copy() # ban sao doc lap
car2.clear()

#dict.fromkeys() - dung de tao 1 dict moi tu 1 danh sach cac keys
keys = {'a','e','i','o','u'}
d2 = dict.fromkeys(keys)# ban lay tung phan tu trong keys gan cho keys cua dict d2
print("--------------------------------")
print("khi khong gan value")
print(d2) # vi ban khong truyen value nen , value tu dong bang none

#cung voi value mac dinh (0)
print("--------------------------------")
print("khi gan value")
d3 = dict.fromkeys(keys,0) # o day value cua cac keys se bang 0
print(d3)
