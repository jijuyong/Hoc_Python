# nhu phan truoc, luc cap nhat suc manh cho sieu nhan A = 40, no ko kieu dg cau truc
class Sieu_nhan:
    suc_manh = 50
    def __init__(self,id:int,vu_khi:str):
        self.id =id
        self.vu_khi = vu_khi

    @classmethod
    def update_power(cls,smach:int):
        cls.suc_manh = smach

    @classmethod
    def from_string(cls,s):
        lst = s.split('-')
        new_list = [st.strip() for st in lst]
        id_hero,vu_khi = new_list

        return cls(id_hero,vu_khi)


hero1 = Sieu_nhan(556,"Kiem")
hero2 = Sieu_nhan(557,"Doc duoc")
hero2.update_power(100)# no se hieu la Sieu_nhan.update_power 
print(f"Hero{hero1.id}, suc manh {hero1.suc_manh}")
print(f"Hero{hero2.id}, suc manh {hero2.suc_manh}")


infor_str = "558 - am khi"
hero3 = Sieu_nhan.from_string(infor_str)
print(hero3.__dict__)

