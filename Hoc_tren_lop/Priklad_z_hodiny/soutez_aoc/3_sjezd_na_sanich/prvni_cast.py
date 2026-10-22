from os.path import join, dirname, realpath

path = join(dirname(realpath(__file__)), "test.txt")



def load_file(filenam:str)->list:
    with open (path, 'r', encoding = "utf-8") as f:
        return [line.strip() for line in f]

def prvni_cast(mapa:list)->int:
    x=0
    y=0
    s=0
    while y<len(mapa)-1:
        y+=1
        x+=3
        x = x%(len(mapa[0]))
        cf = mapa[y][x]
        if cf=="#":
            s+=1
    return s


mapa = load_file(path)
print(mapa)
vysledek = prvni_cast(mapa)
print(vysledek)