from os.path import join, dirname, realpath

path = join(dirname(realpath(__file__)), "test.txt")

pocet_spravny =0
pocet_byl = 0
pocet_heslo = 0
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()


        pravidlo, heslo = line.split(": ")
        druhy_cast,ZNAK = pravidlo.split(" ")
        MIN,MAX = druhy_cast.split("-")
        MIN  = int(MIN)
        MAX = int(MAX)

        pocet_byl = heslo.count(ZNAK)
        if pocet_byl>=MIN and pocet_byl<=MAX:
            #print(f"heslo: {heslo} je platna")
            pocet_spravny+=1
        pocet_heslo +=1
    print(f"Výsledek: {pocet_spravny} platna heslo ze {pocet_heslo} hesel")