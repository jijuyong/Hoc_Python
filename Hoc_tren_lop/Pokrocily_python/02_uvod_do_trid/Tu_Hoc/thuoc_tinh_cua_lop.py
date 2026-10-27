class Sieu_nhan:
    suc_manh = 50 # thuoc tinh trong lio, khi cap nhat thi 
    # thi gia cua toan bo doi tuong cua lop nay cung se duoc cap nhat
    so_thu_tu =0
    def __init__(self,ten:str,vu_khi:str):
        self.ten = "Sieu nhan "+ten
        self.vu_khi = vu_khi
        Sieu_nhan.so_thu_tu+=1
        self.so_thu_tu = Sieu_nhan.so_thu_tu

    def info(self)->None:
        print(f"{self.ten}, co vu khi la: {self.vu_khi}, voi diem suc manh: {self.suc_manh}")

sieu_nhan_A = Sieu_nhan("Gao","Luc kiem")
print("*"*20)
print(sieu_nhan_A.info())
print("*"*20)
print(f"suc manh cua {sieu_nhan_A.ten} la: {sieu_nhan_A.suc_manh}")
print(f"suc manh cua {sieu_nhan_A.ten} goi bang class la: {Sieu_nhan.suc_manh}")

#cap nhat gia tri thong qua lop
Sieu_nhan.suc_manh = 40
sieu_nhan_B = Sieu_nhan("Hong","Truy")
sieu_nhan_C = Sieu_nhan("Do","thuoc doc")
print("*"*20)
print(f"suc manh cua {sieu_nhan_A.ten}, sau khi cap nhat la: {sieu_nhan_A.suc_manh} ")
print(f"suc manh cua {sieu_nhan_A.ten}, sau khi cap nhat, goi bang class la: {Sieu_nhan.suc_manh} ")
print("*"*20)
print("tog so sieu nhan hien tai la: ",Sieu_nhan.so_thu_tu)
print(f"{sieu_nhan_A.ten} la sieu nhan thu {sieu_nhan_A.so_thu_tu}")
print(f"{sieu_nhan_B.ten} la sieu nhan thu {sieu_nhan_B.so_thu_tu}")
print(f"{sieu_nhan_C.ten} la sieu nhan thu {sieu_nhan_C.so_thu_tu}")

#cap nhat gia tri thuoc tinh thong qua doi tuong 
# neu chi thay doi a doi tuong thi class van giu nguyen
sieu_nhan_A.suc_manh = 70
print("*"*20)
print(f"suc manh cua {sieu_nhan_A.ten} la: {sieu_nhan_A.suc_manh}")
print(f"suc manh cua {sieu_nhan_B.ten} la: {sieu_nhan_B.suc_manh}")
print(f"suc manh cua {sieu_nhan_C.ten} la: {sieu_nhan_C.suc_manh}")




