


casy = [0,10,20,30,40,50]
teploty = [72.5,84.0,86.2,85.1,80.0,91.4,]

def analyzuj_mereni(casy,teploty,limit=85.0):
    list_index =[]
    list_ca_hai = list(zip(casy,teploty))
    for index, value in enumerate(list_ca_hai):
        for j in value:
            if j>=limit:
                list_index.append(index)
        #hoac co the khong dung for j 
        # if value[1]>limit

    return(index+1, len(list_index), list_index)
    

vysledek = analyzuj_mereni(casy,teploty)
print(vysledek)