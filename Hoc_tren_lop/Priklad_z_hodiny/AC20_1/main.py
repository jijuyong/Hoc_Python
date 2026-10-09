
list_so = []
with open("data.txt","r",encoding="utf-8") as f:
    for i in f:
        cislo1 = int(i.strip())
        list_so.append(cislo1)

# for i in range(len(list_so)-1):
#     print(list_so[])


for i in range(len(list_so)):
    for j in range(i+1,len(list_so)):
        if list_so[i]+list_so[j] == 2020:
            print(f"so thu nhat: {list_so[i]}")
            print(f"so thu hai: {list_so[j]}")
            print(f"soucin 2 cisel je: {list_so[i]*list_so[j]}")
            break

for i in range(len(list_so)):
    for j in range(i+1,len(list_so)):
        for k in range(j+1,len(list_so)):
            if list_so[i]+list_so[j]+list_so[k] == 2020:
                print(f"so thu nhat: {list_so[i]}")
                print(f"so thu hai: {list_so[j]}")
                print(f"so thu ba: {list_so[k]}")
                break


