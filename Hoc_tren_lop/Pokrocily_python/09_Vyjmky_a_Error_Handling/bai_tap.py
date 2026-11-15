'''
1. Máy tính có xử lý lỗi
Viết chương trình thực hiện các yêu cầu sau:

Nhận hai số từ người dùng.
Chia số thứ nhất cho số thứ hai.
Xử lý ValueError (nếu người dùng nhập văn bản) và ZeroDivisionError (nếu chia cho 0).
In kết quả hoặc thông báo lỗi.
'''

while True:
    try:
        a = int(input("Hay nhap vao so a: "))
        b = int(input("Hay nhap vao so b: "))
        print(f"{a} : {b} = {a/b}")
        break

    except ZeroDivisionError:
        print("KHong chia cho 0")
    except ValueError:
        print("chi dc nhap so")


'''
2. Bộ kiểm tra dữ liệu
Viết hàm dang_ky(ten), hàm này sẽ phát sinh ValueError nếu tên để trống hoặc có ít hơn 3 ký tự. Gọi hàm trong khối try-except và bắt ngoại lệ đó.
'''

def dang_ky(ten):
    if not ten:
        raise ValueError("Ten bi trong")

    if len(ten) < 3:
        raise ValueError("Ten phai co it nhat 3 ky tu")

    print("Dang ky thanh cong!")


while True:
    try:
        ten = input("Nhap ten dang ky: ")
        dang_ky(ten)
        break

    except ValueError as e:
        print("Loi:", e)
        print("Vui long nhap lai!\n")

