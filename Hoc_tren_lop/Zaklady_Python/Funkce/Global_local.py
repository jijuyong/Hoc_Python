# Bien toan cuc - global variable
Thue_Vat = 0.1

def tinh_gia_sau_thue(gia_goc):
    print(f"Thue Vat hien tai: {Thue_Vat}")
    return gia_goc*(1+Thue_Vat )

#NEU THAT SU CAN SUA BIEN TOAN CUC, CO THE LAM NTN
dem = 0

def tang_dem():
    global dem
    dem = dem +1

