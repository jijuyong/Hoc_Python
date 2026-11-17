#Regex là một chuỗi ký tự đặc biệt dùng để tìm kiếm, kiểm tra hoặc thay thế nội dung trong văn bản.3
import re

text = "xin chao,  so dien thoai cua toi la 123456789"
# findall - Tìm TẤT CẢ kết quả.
# search() = Tìm kết quả ĐẦU TIÊN.
print("************ re.findall() **************")
print("               ** r'\\d' **  " )
'''
- re.findall(): tìm tất cả những gì khớp với mẫu.
- r"\\d" - tim 1 chu so tu 0 den 9
'''
print(re.findall(r"\d",text))

print("               ** r'\\d+' **  " )
print(re.findall(r"\d+",text))

print("               **Dấu chấm . **  " )
text1 = "abc adc aec"
print(re.findall(r"a.c",text1))
'''
a: bắt buộc có chữ a.
.: có một ký tự bất kỳ ở giữa.
c: bắt buộc có chữ c.
'''
print("               ** Dấu ^ – Bắt đầu chuỗi**  " )
text2 = "Hello Python"
print(re.search(r'^Hello',text2))# ko tim thay se ra none

print("               ** Dấu $ – Kết thúc chuỗi **  " )
text3 = "I love python"
print(re.search(r'$Python',text3))

print("               ** Dấu \\ – Escape **  " )
text4 = "Hello. How are you?" # tim dau cham
print(re.findall(r'\.',text4))

print("               ** Dấu | – Hoặc (OR) **  " )
text5 = "I like cat and dog" # Có nghĩa là tìm cat HOẶC dog.
print(re.findall(r"cat|dog",text5))


print("               ** Dấu [] – Tập hợp ký tự **  " )
text6 = "hello world"
print(re.findall(r'[aeiou]',text6))# tim cac ky tu a,e,i,o,u

print("               ** Dấu [^] – Phủ định **  " )
text7 = "abc123xyz"
print(re.findall(r'[^0-9]',text7)) # tim nhung ky tu khong phai la so

print("               ** Dấu () – Nhóm **  " ) # Dùng để gom các ký tự lại với nhau hoặc trích xuất một phần văn bản.
text8 = "I say Hello Python"
match = re.search(r"(Hello) (Python)",text8)
if match:
    print(match.group(1))
    print(match.group(2)) 
    print(match.group(0))# group(0) - lấy toàn bộ đoạn khớp










