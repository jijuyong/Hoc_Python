#cach tao file an toan
# mode "w" write
with open("a.txt", "w", encoding="utf-8") as f:
    f.write("Hello World")
#den day file se tu dong close

# mode "w" writelines
bai_tho = [
    "My mother is my shining light,\n",
    "She makes my days warm and bright.\n",
    "Her love is gentle, pure, and true,\n"
]
with open("b.txt", "w", encoding="utf-8") as f:
    f.writelines(bai_tho)

# mode "r" - .read() - in ra ca tep
print("MODE R")
with open("b.txt", "r", encoding="utf-8") as f:
    print(f.read())
print("*"*50)
#  mode "r" - .readline - in ra 1 dong
with open("b.txt", "r", encoding="utf-8") as f:
    dong = f.readline()
print(dong)
print("*"*50)

# mode "r" - .readlines
with open("b.txt", "r", encoding="utf-8") as f:
    print(f.readlines())
print("*"*50)

# read bang vong lap
print("Read bang vong lap")
f = open("b.txt", "r")
for line in f:
    print(line)
f.close()
print("*"*50)

# mode "a" - them vao cuoi tep
print("MODE 'a' ")
with open("a.txt", "a", encoding="utf-8") as f:
    f.write("I love python")

#mode "rb" "wb" "ab" - dung cho nhi phan
print("file nhi phan")
with open("data.bin", "wb") as f:
    f.write("xin chào".encode("utf-8"))
with open("data.bin", "rb") as f:
    b = f.read()
print(b)
f.close()

print("*"*50)
print("MODE r+")
# mode "r+" - doc + ghi de, ko xoa file
f = open("b.txt", "r+")
f.write("XY")
f.seek(0); print(f.read())
# dau ; cho phep viet 2 cau lenh tren cug 1 dong
f.close()

# mode "w+" - xoa sach khi mo, roi ghi(doc phai seek)
print("*"*50)
print("MODE w+")
f = open("b.txt", "w+") #xoa file, con tro o 0
print(f.read()); f.write("123")
#luc in ra file se tronf -> viet vao 123 -> chuyen con tro len 0 -> roi doc
f.seek(0); print(f.read())
f.close()

#mode "a+" - doc phai seek 0, nhung GHI luon o cuoi
print("*"*50)
print("MODE a+")
f = open("b.txt", "a+")
f.write("tac gia: khong ky ten")
f.seek(0); print(f.read())
f.close()

