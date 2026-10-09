
data = []
with open("data.txt","r", encoding="utf-8") as f:
    for i in f:
        radek = i
        data.append(radek)


with open("number.txt","w", encoding="utf-8") as f:
    for i in range(len(data)):
        slovo = data[i].strip()
        print(slovo)
        for j in range(len(slovo)):
            if slovo[j].isdigit():
                f.write(slovo[j])













