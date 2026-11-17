'''
Bạn có thể hiểu đơn giản: 
    Quantifiers cho máy tính biết một ký tự được phép xuất hiện bao nhiêu lần.

    Ky hieu                 Y nghia
    *                      0 hoặc nhiều lần
    +                      1 hoặc nhiều lần
    ?                      0 hoặc 1 lần
    {n}                    Chính xác n lần
    {n,m}                  Từ n đến m lần
'''

import re

print("          -----  '*'  ------")
text = "Ha Haf Haff Hafff"
print(re.findall(r"Haf*",text))
# se in ra ['Ha', 'Haf', 'Haff', 'Hafff']
# Vì f* có nghĩa là chữ f có thể xuất hiện 0 lần hoặc nhiều lần. 

print("          -----  '+'  ------")
print(re.findall(r'Haf+',text))

print("          -----  '?'  ------")
text2 = "Color Colour"# Vì u? có nghĩa là chữ u có thể xuất hiện hoặc không.
print(re.findall(r'Colou?r',text2))

print("          -----  {n}  ------")
text3 = "12 123 1234 12345"
print(re.findall(r"\d{2}",text3))

print("          -----  {n,m}  ------")
text3 = "1 12 123 1234 12345"# Nó tìm từ 2 đến 4 chữ số liên tiếp.
print(re.findall(r'\d{2,4}',text3))






