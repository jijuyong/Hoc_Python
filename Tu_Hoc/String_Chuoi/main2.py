# khoang trang va thay the - 1.str.strip(chars)
#chars (tuy chon) - tap hop cac ky tu can xoa o dau/cuoi chuoi. Mac dinh:xoa khoang trang

#NHOM 1
# strip() - xo atung ky tu don le, khong phai chuoi con
#vd: strip(' #') - nghia la: xoa BAT KY ky tu nao thuoc tap {' ', '#'} o dau va cuoi chuoi
print("-"*40)
s = '  #Hello world^####~##  '
print(f"chuoi s: {s}")

print(s.strip()) # khong chuyen cai ji vao se thanh xoa space
print(s.strip(' ^#'))# chi xoa den # truoc ~

# str.replace(old,new,count) - thay theo chuoi con
print("-"*40)
s2 = 'ab12cd3412cd'
print(f"chuoi s2: {s2}")
print(f"chuoi sau khi bi thay the {s2.replace('12','21')}")
print(f"chuoi sau khi bi thay the 1 lan {s2.replace('12','21',1)}")


#3. str.split(sep,maxsplit) - sep mac dinh la space
print("-"*40)
s3 = 'abacdaef'
print(f"chuoi s3: {s3}")
print(f"chuoi 3 sau tach 'a': {s3.split('a')}")
print(f"chuoi 3 sau tach 'a' 1 lan: {s3.split('a',1)}")
print(f"chuoi 3 sau tach lan: {s3.split()}")

#4. partition(sep) - tra tuple 3 phan(tuoc,sep,sau) - tach tai lan xuat hien dau tien cua sep
print("-"*40)
s4 = '123456'
print(f"chuoi s4: {s4}")
print(f"chuoi s4 sau tach '34': {s4.partition('34')}")
print(f"chuoi s4 sau tach '78': {s4.partition('78')}")
#rpartition (sep) - tach tai lan xuat hien cuoi cung
print("-"*40)
s5 = '12345634'
print(f"chuoi s5: {s5}")
print(f"chuoi s5 sau tach '34': {s5.rpartition('34')}")


# NHOM 2
# .count(sub,start,end)
print("-"*40)
s6 = 'abcdabfabbcd'
print(f"chuoi s6: {s6}")
print(f"co {s6.count('ab')} am 'ab' trong chuoi")
print(f"co {s6.count('ab',2,9)} am 'ab' trong chuoi tu index 2->8") # dem tu index 2 den 8

# .find(sub,start,end) - tra indec DAU TIEN, khong tiem thay -> -1
print("-"*40)
s7 = '0123456'
print(f"chuoi s7: {s7}")
print(f"index dau tien khi xuat hien so 5 la {s7.find('5')}")
print(f"index dau tien khi xuat hien so 5 tu [1->3] la {s7.find('5',1,4)}")

# indec(sub,start,end) - giong find(), nhung neu khong tim thay -> ValueError
print("-"*40)
print(f"chuoi s7: {s7}")
#print(f"index dau tien khi tim thay so 9 la: {s7.index('9')}") bi error

#nhom 3: tra ve true/flase
print("-"*40)
print(f"trong chuoi 'abc123' co so va chu cai khong: {'abc123'.isalnum()}")
print(f"trong chuoi 'abc 123' co so va chu cai khong: {'abc 123'.isalnum()}")

print("-"*40)
print(f"chuoi 'abc' co phai la cac chu cai ko: {'abc'.isalpha()}")
print(f"chuoi 'abc1' co phai la cac chu cai ko: {'abc1'.isalpha()}")

print("-"*40)
print(f"chuoi '123' co phai toan so ko: {'123'.isdigit()}")
print(f"chuoi '123b' co phai toan so ko: {'123b'.isdigit()}")

print("-"*40)
print(f"trong chuoi '    ' toan la space ak: {'    '.isspace()}")
print(f"trong chuoi ' 12a' toan la space ak: {' 12a'.isspace()}")

print("-"*40)
print(f"chuoi 'hello' duoc viet thuong ak: {'hello'.isupper()}")
print(f"chuoi 'Hello' duoc viet thuong ak: {'Hello'.isupper()}")

print("-"*40)
print(f"chuoi 'HELLO' la viet hoa dk: {'HELLO'.isupper()}")
print(f"chuoi 'Hello' la viet hoa dk: {'Hello'.isupper()}")

print("-"*40)
print(f"'Hello World' co phai dc viet hoa moi chu cai dau ko: {'Hello World'.istitle()}")
print(f"'Hello horld' co phai dc viet hoa moi chu cai dau ko: {'Hello world'.istitle()}")

# NHOM 4 - chuyen doi hoa/thuong
print("-"*40)
print(f"'abc' sau khi chuyen sang viet hoa: {'abc'.upper()}")
print("-"*40)
print(f"'AabCcC' sau khi chuyen sang viet thuong: {'abc'.lower()}")
print("-"*40)
print(f"'hello worl, I am Hana' sau khi chuyen sang viet hoa chu cai dau tien: {'hello worl, I am Hana'.capitalize()}")
print("-"*40)
print(f"'Hello World' sau khi chuyen tu sang hoa<->thuong: {'Hello World'.swapcase()}")
print("-"*40)
print(f"'hello world' sau khi viet hoa nhung chu cai dau tien: {'hello world'.title()}")

#nhom  5 - kiem tra dau/cuoi
print("-"*40)
s8 = '12abcdef'
print(f"chuoi s8: {s8}")
print(f"s8 bat dau voi '12' phai ko: {s8.startswith('12')}")
print(f"s8 bat dau voi '12' trong pham vi index [0->4] phai ko: {s8.startswith('12',0,5)}")
print(f"s8 bat dau voi 'ab' phai ko: {s8.startswith('ab')}")

print("-"*40)
s9 = 'abcdef12'
print(f"chuoi s9: {s9}")
print(f"s9 ket thuc voi '12' phai ko: {s9.endswith('12')}")
print(f"s9 ket thuc voi 'ef' phai ko: {s9.endswith('ef')}")
