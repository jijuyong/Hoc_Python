#-------------1.Cau truc if------------------
cislo = 10

if cislo>5:
    print("so do lon hon 5")

print("Tohle se vypisuje vzdy")

#-------------2.Cau truc else------------------
vek =15

if vek>=18:
    print("vstup povolen")
else :
                    print("vstup zakazan")

#-------------3.Cau truc elif------------------
body = int(input("Kolik mas bodu: "))
if body >=90:
    print("mas A")
elif body>=80:
    print("mas B")
elif body >=70:
    print("mas C")
else : print("mas D")

#-------------4.Nested Ifs ------------------
ma_admin_prava = input("Ma admin prava: ")
uzivatel_prihlasen = ma_admin_prava

if uzivatel_prihlasen:
    if ma_admin_prava == "ma":
        print("Vitej, uzivateli")
else :
    print("Prosim, prihlaste se")

#-------------5.Toán tử ba ngôi (If trên một dòng)------------------

stav = "dospely" if vek>=18 else "nezlietily"
print(f"vase stav je: {stav}")

#-------------6. Cấu trúc match-case (Python 3.10+, switch case)------------------
status_kod = 404

match status_kod:
    case 200:
        print("OK")
    case 404:
        print("Nenalezeno")
    case 500:
        print("Chyba severu")
    case _:
        print("Neznamy stav") # hoat dong nhu mac dinh else

