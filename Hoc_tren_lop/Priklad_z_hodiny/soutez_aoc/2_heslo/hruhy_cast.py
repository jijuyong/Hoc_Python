from os.path import join, dirname, realpath

path = join(dirname(realpath(__file__)), "test.txt")

index=0
pocet=0
pocet_heslo = 0
with open(path,'r',encoding = "utf-8") as f:
    for line in f:
        line = line.strip()


        pravidlo, heslo = line.split(": ")
        druhy_cast,ZNAK = pravidlo.split(" ")
        MIN,MAX = druhy_cast.split("-")

        prvni = heslo[int(MIN) - 1] == ZNAK
        druhy = heslo[int(MAX) - 1] == ZNAK

        '''
        prvni = heslo.find(ZNAK)
        '''

        if prvni != druhy:
            pocet += 1

        pocet_heslo += 1

print(f"Výsledek: {pocet} platných hesel ze {pocet_heslo} hesel")
