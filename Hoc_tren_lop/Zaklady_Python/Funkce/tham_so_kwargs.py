print("**** Tham so **kwargs ****")
def hien_thi_tt(**thong_tin):
    print("Thong tin nhan vien")
    for key,value in thong_tin.items():
        print(f"{key} = {value}")
    print("********")

hien_thi_tt(ten="Nguyen An", tuoi=28, phong="Ky thuat")
hien_thi_tt(ten="Linh", tuoi=21, phong="Marketing", ID=123456)
