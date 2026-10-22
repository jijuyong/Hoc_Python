from typing import Optional

tuoi : int = 25
ten: str = "Petr"
dang_hoat_dong: bool = True


#kieu bt
def chao_hoi (ten:str)->str:
    return "Xin chao"+ten

#kieu Optional | NONE
def find_user(user_id:int)->Optional[str]:
    users = {
        1:"An",
        2:"Binh"
    }
# Optional[str] = None - mac dinh la None neu ko truyen chuoi vao

    return users.get(user_id)
print("********Optional | None **********")
print(f" user_id[1] ten la: {find_user(1)}")
print(f" user_id[99] ten la: {find_user(99)}")

#kieu union
def process(value: int|str):
    #cach viet cu
    #def process(value: Union[intstr]):
    print("******************")
    print(f"kieu union: {value} ")

#cho biet ham se tra ve 1 so nguyen hoac la 1 chuoi
def so()->int|str:
    return 123

#kieu ANY
def processssss(value:any)->any:
    return value
    # neu chuyen vao str thi tra ve str, neu chuyen vao int thi tra ve int
print("*******ANY*********")
print(processssss("hana"))
print(processssss(123))


#kieu custom classes
class User:
    def __init__(self, name: str):
        self.name = name

def get_user(user: User) -> str:
    return f"Hello, {user.name}"

print("*********Custom classes**********")
u1 = User("Mini")
print(get_user(u1))