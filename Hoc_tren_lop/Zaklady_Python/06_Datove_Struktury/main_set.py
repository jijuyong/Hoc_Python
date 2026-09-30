#khai bao set
s = {1,1,2,2,3,4,5}
print(f"do dai cua s la: {len(s)}")
print(s)

# set rong
s1 = {}
s2 =()
print("--------------------------------")
print(f"type cua s1: {type(s1)}")
print(f"type cua s2: {type(s2)}")

#them/xoa phan tu
print("--------------------------------")
s3 = {1,2,3}
print(f"s3:{s3} ")
print("--------------------------------")
print(".add()")
s3.add(4) # them 4
print(s3)
print("--------------------------------")
print(".update()")
s3.update([5,6,7]) # them nhieu
print(s3)
print("--------------------------------")
print(".remove()")
s3.remove(1)# bao loi neu 1 ko ton tai
print(s3)
print("--------------------------------")
print(".discard()")#dung de xoa 1 phan tu  khoi set
s3.discard(99) # khong bao loi
print(s3)
print("--------------------------------")
print(".clear()")
s3.clear()

#phep toan tong ho (diem manh)
A = {'C','D','E','F','G'}
B = {'E','F','G','A','B'}
print("---------------------------")
print(f"A: {A}")
print(f"B: {B}")
print("---------------------------")
print(f" A - B = {A-B}")
print("---------------------------")
print(f" A | B = {A|B}")# hop tat ca phan tu cua ca hai
print("---------------------------")
print(f" A & B = {A&B}") # in ra nhung phan tu co chung
print("---------------------------")
print(f" A ^ B = {A^B}")# cac phan tu khg chung

#dung thuc te
# loai bo trung lap trong list
nams = ["An","Binh","An","Cuong","Binh"]
unique = list(set(nams)) # ep list sang set

#tim 1 phan tu chung giua hai list
common = list(set(A)&set(B))
print(f"nhung cai ten la: {nams}")
print(f"phan tu chung: {common}")
