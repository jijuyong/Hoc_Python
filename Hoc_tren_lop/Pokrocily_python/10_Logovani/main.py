'''
Logging là việc ghi lại những thông tin về quá trình hoạt động của chương trình.
Ví dụ, thay vì chỉ dùng print():
'''
import logging

logging.warning(("Dang ket noi database...."))
logging.info("ket noi thanh cong!")
logging.error("Co loi xay ra❌❌")

'''
Điểm khác biệt là logging có thể phân loại mức độ thông báo và ghi thông tin vào file.
Python có 5 mức độ logging phổ biến:

Mức độ	                    Ý nghĩa

DEBUG	                    Thông tin chi tiết để kiểm tra chương trình
INFO	                    Thông báo chương trình hoạt động bình thường
WARNING	                    Cảnh báo có vấn đề tiềm ẩn
ERROR	                    Đã xảy ra lỗi
CRITICAL	                Lỗi nghiêm trọng, có thể khiến chương trình không hoạt động
'''

logging.basicConfig(level=logging.DEBUG) #hiển thị tất cả các mức từ DEBUG trở lên.

logging.debug("Dang kiem tra chuong trinh")
logging.info("Chuong trinh dang chay")
logging.warning("Bo nho sap day")
logging.error("Khong tim thay file")
logging.critical("He thong gap loi nghiem trong")

'''
Nếu bạn đặt:
logging.basicConfig(level=logging.WARNING)
Thì chỉ hiển thị WARNING, ERROR và CRITICAL
'''

#Ghi log vào file
print('*'*50)
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
    '''
    format - Định dạng nội dung nhật ký.
    %(asctime)s: Thời gian ghi log.
    %(levelname)s: Mức độ log.
    %(message)s: Nội dung thông báo.
    '''
)
logging.info("Chuong trinh bat dau")
logging.warning("Day la canh bao")
logging.error("Da xay ra loi")


print("*"*50)
print("Kết hợp Logging với try-except")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

try:
    number = int(input("Nhap mot so: "))
    result = 10 / number

    logging.info("Tinh toan thanh cong")
    print("Ket qua:", result)

except ValueError:
    logging.error("Nguoi dung nhap khong phai so nguyen")

except ZeroDivisionError:
    logging.error("Khong the chia cho 0")


