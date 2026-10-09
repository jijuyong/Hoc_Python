vstup = "Python je skvělý, ale skriptovací jazyk je rychlý. Python má přehlednou syntaxi."
stop_slova = {"je", "ale", "má"}


def analyzuj_frekvenci_slov(text, ignorovana_slova):
    unikatni_slovo=[]
    list_slov = text.replace(".","").replace(",","").replace("?","").replace("!","").lower().split()
    #print(pomocny_retezec.split())
    frekvence = dict()
    for slovo in list_slov:
        if slovo in stop_slova:
            continue
        if slovo in frekvence:
            frekvence[slovo]+=1
        else : frekvence[slovo] =1
    #print(list_slov)

    for key, value in frekvence.items():
        if value>1:
            continue
        else : unikatni_slovo.append(key)
    #hoac co the dung
    '''
    unikatni = set(k for k, v in frekveence.items() if v==1)
    '''
    return frekvence, unikatni_slovo



frekvence, unikatni = analyzuj_frekvenci_slov(vstup,stop_slova)
print(f"frekvence: {frekvence}")
print(f"unikatni slovo: {unikatni}")