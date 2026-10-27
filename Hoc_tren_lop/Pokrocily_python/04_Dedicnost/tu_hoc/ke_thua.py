class Sieu_nhan:
    suc_manh=80
class sieu_nhanKteam(Sieu_nhan):# ke thua
    #neu ko muon ke thua bien suc manh cua sieu_nhan thi viet ra bien cua ring no
    suc_manh = 40

hero1 = sieu_nhanKteam()
print(f"suc manh cua hero1 la: {hero1.suc_manh}")

# ke thua ham constructor
class Firma:
    def __init__(self,ten:str,truc_vu:str,tong_so:int):
        self.ten = ten
        self.chuc_vu = truc_vu
        self.tong = tong_so

    #Ke thua phuong thuc
    def gioi_thieu(self):
        print(f"Xin chao, chung toi la {self.ten}, chung toi co {self.tong} {self.chuc_vu}")

class School(Firma):# thua huong dc ca constructor cua thang cha
    #ke thua phuong thuc
    pass



#neu muon co them attribute vao constructor
class Obchod(Firma):
    def __init__(self, ten, truc_vu, tong_so, luong:float):
        super().__init__(ten, truc_vu, tong_so)
        self.salary = luong
    #ke thua phuong thuc va sua lai 1 ty
    def gioi_thieu(self):
        super().gioi_thieu()
        print(f"luong cua ho la: {self.salary}")

print("*********ke Thua***********")
school1 = School("Gynazium","teacher",35)
print(f"truong {school1.ten}, chuc vu {school1.chuc_vu} co {school1.tong} nguoi")
print(school1.__dict__)

print("**********Ham Super**********")
Obchod1 = Obchod("Docen","SalesAssistant",40,23563.21)
print(Obchod1.__dict__)

#ke thua phuong thuc
print("**********Ke thua phuong thuc**********")
print("---Ke thua y nguyen ----")
school1.gioi_thieu()
print("--------ke thua + chinh sua--------" )
Obchod1.gioi_thieu()