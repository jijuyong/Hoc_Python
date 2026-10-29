#Kiến thức đầu tiên: Hàm cũng là một đối tượng
#Trong Python, bạn có thể gán một hàm cho biến, giống như gán số hoặc chuỗi.

def cong(a,b):
    return a+b

phep_cong = cong # khong phai cong()
print(f"phep cong = {phep_cong(3,5)}")

'''
cong: tham chiếu đến hàm.
cong(): gọi hàm để thực thi.

phep_cong = cong - lay ham gan cho bien
phep_cong = cong() - chay ham roi lay ket qua gan cho bien
'''

# 3. Hàm nằm bên trong hàm
#Python cho phép định nghĩa một hàm bên trong một hàm khác.
print("*******Ham nam trong ham**********")
def ham_cha():
    print("toi la ham cha")

    def ham_con():
        print("toi la ham con")

    ham_con()

ham_cha()


#Tạo Decorator đầu tiên
print("------Tao decorator dau tien--------")
def decorator(ham_goc):
    def wrapper():
        print("---Bat dau---")

        ham_goc()

        print("---Ket thuc---")
    return wrapper

@decorator # ten phai giong ham decorator
def chao():# day la ham goc de truyen vao decorator
    print("Xin Chao!")

#cach viet 1
'''pozdrav = decorator(chao)
pozdrav()'''

#cach viet 2 - them @decorator vao truoc ham goc
print("********cah viet thu 2 - sau khi them @decorator************")
chao()





#decorator voi ham co tham so
print("********Decorator co tham so*************")
@decorator 
def Greeting(name):
    print(f"Heloo, {name}")

#se bi loi Greeting("An"), nen them *args, *kwargs
def DECORATOR(ham_goc):
    def wrapper(*args,**kwargs):
        print("****Bat Dau****")

        ket_qua= ham_goc(*args,**kwargs)

        print("****Ket thuc****")

        return ket_qua
    return wrapper

@DECORATOR
def POZDRAV(ten):
    print(f"chao, {ten}")


POZDRAV("AN")

'''functools.wraps
Nó giúp giữ lại các thông tin quan trọng của hàm gốc, chẳng hạn tên hàm và phần mô tả tài liệu (docstring).
'''
import functools

def D(ham_goc):
    @functools.wraps(ham_goc)
    def wrapper(*args,**kwargs):
        print("****Bat Dau****")

        ket_qua= ham_goc(*args,**kwargs)

        print("****Ket thuc****")

        return ket_qua
    return wrapper








