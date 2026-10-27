class Sieunhan:
    suc_mah =50
    def __init__(self,id:int,vu_khi:str):
        self.id = id
        self.weapon = vu_khi

    @staticmethod
    def bien_hinh():# ko can self
        print("1,2,3 bien hinh")


hero1 = Sieunhan(556,"kiem")
hero1.bien_hinh()