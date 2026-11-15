#Regex là một chuỗi ký tự đặc biệt dùng để tìm kiếm, kiểm tra hoặc thay thế nội dung trong văn bản.3
import re

text = "Hello Python 123"
result = re.search(r"\d+", text)
'''
\\d: Đại diện cho một chữ số từ 0 đến 9.
+: Một hoặc nhiều lần.
group(): Lấy phần văn bản tìm được.
'''
print("********* \\d+ **********")
if result is not None:
    print(result.group())
else:
    print("Khong tim thay!")

print("********* \\d{5} **********")
text2 = '12345'
if re.fullmatch(r"\d{5}",text2):
    print("hop le")
else: print("khong hop le")