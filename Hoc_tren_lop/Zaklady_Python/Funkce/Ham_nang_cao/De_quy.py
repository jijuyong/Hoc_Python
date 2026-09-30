'''
De quy la gi?
- ky thuat ham TU GOI LAI CHINH MINH
ham de quy BAT BUOC phai co dieu kien - neu khong se goi mai mai va bao loi
'''

'''
Cau truc bat buoc

def ham_de_quy(tham_so):
    if dieu_kien_dung:
        return ket_qua 
    return ham_de_quy(nho_ho)
'''

def giai_thua(n):
    if n <=1:
        return n  # dieu kien dung
    return n*giai_thua(n-1)
    # bc1. 5*4 -> nguoc len lai if kiem tra dieu kien roi lai xuong return
    # -> n luc nay se bi tru di 1 -> 4*3

print(f"giai thua cua 5 la: {giai_thua(5)}")