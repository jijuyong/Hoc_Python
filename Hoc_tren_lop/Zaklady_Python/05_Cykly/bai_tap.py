'''
1. Bộ đếm
Sử dụng vòng lặp for để in các số từ 1 đến 10 (bao gồm cả 10).
'''
print("Bai tap 1")

for i in range(11):
    print(i,end=" ")
print(" ")

'''
2. Đánh vần
Nhập một từ từ người dùng. Sử dụng vòng lặp for để in mỗi chữ cái trên một dòng riêng biệt.
'''
print("Bai tap 2")
word = input("Moi ban nhap vao 1 tu de danh van: ")
for tu in word:
    print(tu, end=" ")
print("")

'''
3. Chương trình kiên trì
Sử dụng vòng lặp while để hỏi người dùng "Bạn có muốn tiếp tục không?". 
Chỉ kết thúc vòng lặp khi người dùng nhập "không".
'''
print("Bai tap 3")

choice = ""

while choice != "khong":
    choice = input("Ban co muon tiep tuc khong: ")
    choice =choice.lower()

'''
4. Số chẵn
In ra tất cả các số chẵn từ 0 đến 20. 
Hãy thử giải bài này bằng cách sử dụng tham số step trong hàm range.
'''

print("Bai tap 4")
for i in range(0,20,2):
    print(i,end=" ")
print(" ")