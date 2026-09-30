'''
De Bai - chuyen mot so trong pham vi 0-99 thanh phat am tieng viet
vd: 85 -> tam muoi lam
'''

n = int(input("moi ban nhap vao 1 so: "))
dict1 = {0:"không",1:"một",2:"hai",3:"ba",4:"bốn",5:"năm",6:"sáu",7:"bảy",8:"tám",9:"chín",10:"mười","hang chuc":"mươi" }
hang_chuc = n//10
hang_don_vi = n%10

for key,value in dict1.items():
    if n == key:
        print(value)
    elif n>10 and n<20:
        if hang_don_vi == key:
            print(dict1.get(10),value)
    elif hang_don_vi ==0 and n>=20:
        if hang_chuc == key:
            print(value,dict1.get("hang chuc"))
    elif n>20 and n<100:
        if hang_chuc == key:
            print(value,dict1.get("hang chuc"),end=" ")
            for key,value in dict1.items():
                if hang_don_vi == key:
                    print(value)







