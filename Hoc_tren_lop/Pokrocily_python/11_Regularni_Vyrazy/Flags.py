'''
FLAGS - Các cờ Regex
Flags giúp thay đổi cách Regex tìm kiếm.
'''
import re

# A. re.IGNORECASE – Không phân biệt chữ hoa, chữ thường
text = "HELLO Python"
print("-----------re.IGNORECASE------------")
print(re.search(r"hello",text,re.IGNORECASE))

#B. re.DOTALL – Dấu chấm có thể khớp xuống dòng
print("-----------re.DOTALL------------")
text2 = "Hello\nPython vsdiufd h"
result = re.findall(r"Hello.Python",text2,re.DOTALL)
print(result)
'''
- Mặc định: Ký tự . đại diện cho bất kỳ ký tự nào ngoại trừ ký tự xuống dòng (\n).
- Khi bạn truyền tham số re.DOTALL vào hàm re.findall(), nó sẽ thay đổi hành vi của dấu . 
    thành: khớp với mọi ký tự, kể cả ký tự xuống dòng (\n).
'''


# C. re.MULTILINE – Kiểm tra từng dòng
print("-----------re.MULTILINE------------")

text3 = """Hello
Python
World"""
print(re.findall(r'^Python',text3,re.MULTILINE))
'''
Thông thường ^ chỉ kiểm tra đầu toàn bộ chuỗi.
Khi có re.MULTILINE, nó kiểm tra đầu từng dòng.
'''