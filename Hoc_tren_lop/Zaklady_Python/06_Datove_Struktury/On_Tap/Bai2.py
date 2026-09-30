'''
De bai
Xay dung chuong trinh quan ly nhan du voi 3 truong:
- ma gen - Ho va ten - Bo Phan
Menu 5 lua lua chon:
1 - Hien thi CSDL (Rong -> CSDL trong)
2 - Them CSDL (ma GEN ton tain -> KHONG cho them)
3 - Sua CSDL (kiem tra ma Gen ton tai thi moi sua)
4 - Xoa CSDL (Kiem tra ma GEN ton tai thi moi xoa)
5 - thoat
'''
from random import choice

print ("----------MENU------------")
print("1. Hien thi CSDL")
print("2. Them CSDL")
print("3. Sua CSDL")
print("4. Xoa CSDL")
print("5. Thoat")

CSDL = {
    2026001 :{"Ho va ten":"Nguyen Van A", "Bo Phan":"CNC"},
    2026002 : {"Ho va ten":"Tran Thi B", "Bo Phan":"QA"},
}

choice = 0
while choice!=5:
    choice = int(input("Su lua chon cua ban la: "))
    match choice:
        case 1:
            print("---Hien thi CSDL----")
            for key,value in CSDL.items():
                print(f"GEN: {key}: {value}")
        case 2:
            print("---Them CSDL----")
            Chia_khoa = int(input("Them GEN: "))
            while Chia_khoa in CSDL.keys():
                Chia_khoa = int(input("Gen nay da ton tai, moi nhap GEN khac: "))
            TEN = input("Ho va ten: ")
            Bo_Phan = input("Bo Phan: ")
            CSDL[Chia_khoa] = {"Ho va ten":TEN, "Bo Phan":Bo_Phan}
        case 3:
            print("---Sua CSDL----")
            Ma_gem_muon_sua = int(input("Ma GEN muon sua: "))
            while Ma_gem_muon_sua not in CSDL.keys():
                Ma_gem_muon_sua = int(input("Ma GEN khong ton tai, nhap lai ma GEN khac: "))
            if Ma_gem_muon_sua in CSDL.keys():
                CSDL[Ma_gem_muon_sua]["Ho va ten"] = input("Ho va ten: ")
                CSDL[Ma_gem_muon_sua]["Bo Phan"] = input("Bo Phan: ")

        case 4:
            print("---Xoa CSDL----")
            ma_gen_muon_xoa = int(input("Ma GEN muon xoa: "))
            if ma_gen_muon_xoa in CSDL.keys():
                CSDL[ma_gen_muon_xoa].clear()
print("---Thoat---")
