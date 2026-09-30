#---------ep kieu du lieu-------------
from typing import List

a= "10"
b = "20"
print(a+b)# noi chuoi
print(int(a) + int(b))

#---------Boolean falsy Values-------------
#nhung gia tri luon luon la false
'''
bool(0)
bool("")
bool([])
bool(None)
'''
#nhung gia tri luon luon la true
'''
bool(1)
bool("abc")
'''
c = bool(0)
print(c)# c se bang false

#---------Ham type() - kiem tra kieu-------------
type(1)
type("hello")
type(3.14)
type(True)
print(type(2+3j))


