'''
a=10
b=0
print(a/b)
se  bi loi division zero
'''

try:#Chứa đoạn code có khả năng gây lỗi.
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:#Chứa đoạn code được thực hiện khi lỗi xảy ra.
    print("Khong the chia cho 0")

'''ValueError
number = int("hello")
Python không thể chuyển "hello" thành số nguyên nên phát sinh ValueError
'''

'''
IndexError
numbers = [10,20,30]
print(numbers[5])
List chỉ có 3 phần tử, nhưng chúng ta lại truy cập vị trí số 5.
'''

'''
Xử lý nhiều loại lỗi
Một chương trình có thể gặp nhiều loại lỗi khác nhau. Ta có thể sử dụng nhiều except

try:
    number = int(input("Nhap mot so: "))
    result = 100/number

except ValueError:
    print("Ban phai nhap so")
except ZeroDivisionError:
    print("Khong the chia cho 0")
'''


# else va finally
'''
else: Chạy khi không xảy ra lỗi trong khối try.
finally: Luôn chạy, dù có lỗi hay không.
'''
print("*"*20,'Else va finally','*'*20)

try:
    number = int(input("Nhap so: "))
    result = 100/number

except ValueError:
    print("phai nhao so!!!")
except ZeroDivisionError:
    print("khong the chia cho !!!")
else: print("Ket qua: ",result)
finally: print("Chuong trinh ket thuc!!!")

print("*"*20,'Tự tạo Exception bằng raise','*'*20)
age = int(input("Nhập tuổi: "))
if age <= 0:
    raise ValueError("Tuổi phải lớn hơn 0!")
print("Tuổi của bạn:", age)

print("*"*20,'Tự tạo loại Exception riêng','*'*20)

class InsufficientMoneyError(Exception):
    pass
money = 50
if money<100:
    raise InsufficientMoneyError("Khong du tien")
