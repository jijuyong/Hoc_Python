from abc import ABC, abstractmethod

'''ABC - Lớp cơ sở để tạo lớp trừu tượng
    @abstractmethod - Đánh dấu phương thức bắt buộc lớp con phải triển khai
    pass - 	Chưa có phần xử lý cụ thể
'''
class DongVat(ABC):
    @abstractmethod
    def make_a_noise(self):
        pass

#dongvat = DongVat() se bi loi 
# vi chỉ dùng làm khuôn mẫu chung, 
# không phải lớp để tạo đối tượng trực tiếp.

# Lớp con phải triển khai phương thức trừu tượng
class Dog(DongVat):
    def make_a_noise(self):
        print("Half Half!!")
        #ko dung super, vi method nay chua dc dinh nghia o lop cha

class Cat(DongVat):
    def make_a_noise(self):
        print("meow, meow!!")

cat1 = Cat()
dong1 = Dog()
cat1.make_a_noise()
dong1.make_a_noise()

'''Điểm quan trọng: Nếu lớp con không triển khai đầy đủ các phương thức trừu tượng còn thiếu,
Python sẽ không cho phép tạo đối tượng của lớp đó.'''

'''
class Chim(DongVat):
    pass
Lý do là Chim chưa triển khai phat_ra_am_thanh().
chim = Chim()  # Lỗi!
'''