'''
1. Cestování v čase
Zeptejte se uživatele ("Kolik ti je let?"). Načtenou hodnotu převeďte na číslo, přičtěte k ní 10 a vypište: "Za 10 let ti bude [vysledek]."
'''
tuoi_hien_tai = int(input("kolik je ti let: "))
print("za 10 let bude ti:",tuoi_hien_tai+10)

'''
2. BMI Kalkulačka
Načtěte od uživatele:

Váhu v kg (jako float).
Výšku v metrech (jako float). Vypočítejte BMI podle vzorce: BMI = vaha / (vyska * vyska). Vypište výsledek.
'''
vaha = float(input("kolik vazis: "))
vysku = float(input("kolik meris: "))
BMI = vaha / (vysku * vysku)
print(f"BMI cua ban la: {BMI}")

'''
3. Typová kontrola
Vytvořte proměnné x = 100 a y = "100". Vypište jejich datové typy pomocí funkce type().
'''
x=100
y ="100"
print(type(x))
print(type(y))