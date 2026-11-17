# Phần này giúp bạn viết Regex ngắn gọn hơn.

'''
Ky hieu                 Y nghia                         vi du
\\d                     Chữ số	                         0–9
\\D	                    Không phải chữ số	            a, b, @
\\w	                    dấu cách và các dấu câu	        a, B, 1, _
\\W	                    Không phải ký tự thuộc từ	    @, !, dấu cách
\\s	                    Khoảng trắng	            Space, Tab, xuống dòng
\\S	                    Không phải khoảng trắng	           a, 1, @
'''
import re

print("               ---- \\d ------")
text = "Hello Word123 !"
print(re.findall(r'\d',text))

print("               ---- \\D ------")
print(re.findall(r'\D',text))

print("               ---- \\w ------")
print(re.findall(r'\w',text))

print("               ---- \\W ------")
print(re.findall(r'\W',text))

print("               ---- \\s ------")
print(re.findall(r'\s',text))

print("               ---- \\S ------")
print(re.findall(r'\S',text))

