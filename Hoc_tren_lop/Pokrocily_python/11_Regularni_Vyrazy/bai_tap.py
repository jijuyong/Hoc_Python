'''
Bài 1: Tìm ngày tháng
Đề bài:
text = "Các ngày được lên lịch là 12.01.2023, 5.5.2023 và cả 31.12.2023."
Yêu cầu: Tìm các ngày có định dạng DD.MM.YYYY.
'''
import re

text = "Các ngày được lên lịch là 12.01.2023, 5.5.2023 và cả 31.12.2023."
result = re.findall(r'\d{1,2}.\d{1,2}.\d{4}',text)
print(result)


'''
Bài 2: Kiểm tra email
Đề bài:
- jan@novak.cz: hợp lệ.
- jan.novak.cz: không hợp lệ.
'''
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
'''
^ - bat dau chuoi
[\\w.-]+	Một hoặc nhiều chữ, số, dấu _, ., -

'''
email = input("zadejte email: ")
print(bool(re.search(pattern,email)))

'''
Bài 3: Kiểm duyệt mật khẩu
Đề bài:
text = "Mật khẩu bí mật là tajne123."
Yêu cầu: Thay tất cả chữ số bằng X.
'''
text1 = "Mật khẩu bí mật là tajne123."
result2 = re.sub(r'\d+','x',text1)
print(result2)