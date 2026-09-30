'''
String la mot chuoi ky tu, day trong '' hoac " " hoac """  """
'''

#nhay don
s = 'Hoc python that thu vi'
#nhay kep
s2 = "Hoc python that thu vi"

print(f"type cua s la: {type(s)}")
print(f"type cua s2 la: {type(s2)}")

# nhay don ngoai, nhay kep trong (khong can escape)
s3  = 'Anh ay noi "toi thich python"'

# nhay kep o ngoai, nhay don o trong
s4 = "it's a beautiful day"

# ban nhay - chuoi nhieu dong
s5 = """
    dong 1
    dong 2
    dong 3
"""
print(f"chuoi s5: {s5}")

#escape characters - ky tu thoat
print("----------------------")
print("Dong1\ndong2")
print("----------------------")
print(f"{'Ten':<10}{'Diem':<10}{'Xep Loai':<10}")
print(f"{'An':<10}{'8.5':<10}{'Gioi':<10}")

# \\ - in giau \
print("----------------------")
print("Duong dan: C:\\Users\\Admin")

#in nhay don
print("----------------------")
print('it\'s Ok')

# in dau nhay kep
print("----------------------")
print("He said \"Hi\"")

# truy cap vao index

mystr = "This is text"
'''
0   1   2   3   4   5   6   7   8   9  10   11
T   h   i   s   _   i   s   _   t   e   x   t
-12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
'''
print("----------------------")

print(f"mystr[1]: {mystr[1]}")
print(f"mystr[0]: {mystr[0]}")
print(f"mystr[-1]: {mystr[-1]}")
print(f"mystrtu 2->8: {mystr[2:9]}")
print(f"mystrtu tu 3: {mystr[3:]}")
print(f"mystrtu tu 3: {mystr[3:]}")
print(f"mystrtu den 3: {mystr[:4]}")

#dao nguoc chuoi bang slicing
m = "Python"
print("----------------------")
print(f"m khi dao nguoc: {m[::-1]}")
# s = "Laptop" slicing "Lap" "top"
s6 = "Laptop"
print("----------------------")
print(f"slicing s6 {s6[0:3]} va {s6[3::1]}")
s7 = "abcdefgh"
print("----------------------")
print(f"s7: {s7[0::2]}")

#stk="0123456789" in ra chi hien 4 so o cuoi
stk = "0123456789"
i = 0
print("----------------------")
print(f"*"*(len(stk)-4)+stk[-4:])
s8 = "madam"
s9 = s8[::-1]
print("----------------------")
print(f"s8 co giong s9 ko: {bool(s8==s9)}")

#duyet tung ky tu bang for
print("----------------------")
for c in 'Python':
    print(c, end=" ")
print(" ")
# kiem tra chuoi con bang in
print("----------------------")
print("is co trong chuoi nay:",'is' in 'this is text')
print("is co trong chuoi nay:",'abc' in 'this is text')
#Xoa String - del
s10 = 'Hello'
del s10
#se ko in dc s10

# 3 cach dinh dang String - Cach 1:f-string
name = 'Jack'
age =9
print("-----------Dinh dang string------------")
print("------cach 1------")
print(f"My name is {name} and I am {age} years old.")
#cach 2 - .format()
print("------cach 2-------")
print('My name is {0}, and I am {1} years old.'.format(name, age))
# 0 la tham so thu nhat , 1 la tham so thu 2
print('Hello {}, age {}'.format('Jack',9))

#can chinh van ban khi xuat ra
print(f"{'An':<10}")#An________
print(f"{'An':>10}")#________An
print(f"{'An':^10}")#____An____

# VD
print("Khi dung f-string")
print(f"{'Ten':<15}{'Phong ban':<15}{'Luong':>10}")
print("-"*40)
print(f"{'Nguyen Van An':<15}{'IT':<15}{12000000:>10}")
print(f"{'Tran Thi Mai':<15}{'Ke toan':<15}{16000000:>10}")
print(f"{'Le Hoang':<15}{'Marketing':<15}{11000000:>10}")

#khi dung format
print(" ")
print("-"*40)
print("Khi dung .format()")
print("{:<15}{:<15}{:<10}".format("Ten","Phong Ban","Luong"))

print(" ")
#cach dinh dang 3 - kieu %
print("------")
print("%s")
print("Ten: %s"%'An')
print("------")
print("%c")
print("%c"% 65)
print("------")
print("%d")
print("Tuoi: %d"% 25)
print("------")
print("%.2f")# lam tron nen 2 desetinna mista
print("%.2f"% 20.45978)
print("------")
print("%f")
print("%f"% 8.5)
print("------")
print("%o")
print("%o"% 255)
print("------")
print("%x")
print("%x"%255)
print("------")
print("%X")
print("%X"%255)
print("------")
print("%e")
print("%e"% 1500)
print("------")
print("%%")# in dau %
print("%.1f%%"% 91.5)

