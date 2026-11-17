'''
- re.search() - tim kiem o bat ky vi tri nao
            - tim thay ket qua dau tien
- re.match() - chi tim o dau chuoi
- re.findall() - tim tat ca ket qua
- re.sub() - Thay the van ban( search and replace)
- re.split() - chia chuoi
'''

import re

text = 'I love python Python, Python, Python'
print("         -- re.search() --")
print(re.search(r'Python',text))

print("         -- re.findall() --")
print(re.findall(r'Python',text))

print("         -- re.match() --")
print(re.match(r'Python',text))

print("         -- re.sub() --")
text1 = "Hello      Python!          !!"
print("thay the khoang cac khoang trang bang ' ' ",re.sub(r"\s+"," ",text1))
print("thay the khoang cac khoang trang bang ',' ",re.sub(r"\s+",",",text1))

print("         -- re.split() --")
text2 = "apple,banana;orange"
print(re.split(r'[,;]',text2))

'''
GROUPS - Nhóm và trích xuất dữ liệu
'''
print("=========GROUPS - Nhóm và trích xuất dữ liệu===========")
text3 =  "Giá: 500 Kč" # chi muon lay so 500

pattern = r"Giá: (\d+) Kč"
match = re.search(pattern,text3)
if match is not None:
    print(match.group(1))
'''
- Giá: : tìm đúng chữ Giá và dấu cách.
- (\\d+): tìm một hoặc nhiều chữ số và lưu chúng vào nhóm 1.
- Kč: tìm đơn vị Kč.
- group(1): lấy nội dung nằm trong cặp ngoặc đầu tiên.
'''
print("----VD KHAC---")
text4 = "Name: John, Age: 25"
pattern = r"Name: (\w+), Age: (\d+)"
match1 = re.search(pattern,text4)
if match1 is not None:
    print(match1.group(1))
    print(match1.group(2))
