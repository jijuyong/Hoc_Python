'''
1. Mật khẩu
Nhập mật khẩu từ người dùng.

Nếu mật khẩu là "tajne123", in ra "Přístup povolen" (Truy cập được chấp nhận).
Ngược lại, in ra "Chybné heslo" (Mật khẩu sai).
'''

mat_khau = input("Vui long nhap mat khau: ")

if mat_khau == "tajne123":
    print("pristup je povolen")
else: print("chybne heslo")

'''
2. So sánh số
Nhập vào một số.

Nếu số lớn hơn 0: in ra "Kladné" (Số dương).
Nếu số nhỏ hơn 0: in ra "Záporné" (Số âm).
Ngược lại: in ra "Nula" (Số 0).
'''

so = float(input("moi nhap vao 1 so:"))

if so>0:
    print("Kladne")
elif so<0:
    print("zaporne")
else:
    print("Nula")

so = "kladne" if so>0 else "nho hon 0"

'''
3. Các ngày trong tuần (Match-case)
Nhập vào số thứ tự của ngày (1-7). Sử dụng match-case để in ra tên ngày 
(Pondělí - Thứ Hai, Úterý - Thứ Ba...). Đối với các số khác, in ra "Neplatný den" (Ngày không hợp lệ).
'''

ngay = int(input("moi nhap vao 1 so: "))

match ngay:
    case 2:
        print("Thu Hai")
    case 3:
        print("Thu Ba")
    case 4:
        print("Thu Tu")
    case 5:
        print("Thu Nam")
    case 6:
        print("Thu Sau")
    case 7:
        print("Thu Bay")
    case 8:
        print("Chu Nhat")
    case _:
        print("ngay nhap khong hop le")
