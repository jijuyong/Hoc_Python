def xin_chao():
    print("xin chao!")

'''
Nhưng nếu file khác import greeting, lệnh xin_chao() ở cuối file cũng sẽ chạy ngay. 
Điều này có thể gây phiền phức nếu bạn chỉ muốn sử dụng hàm mà không muốn tự động thực hiện phần code đó.
giai phap la:
'''
if __name__ == "__main__":
    print("Đang chạy trực tiếp greeting.py")
    xin_chao()