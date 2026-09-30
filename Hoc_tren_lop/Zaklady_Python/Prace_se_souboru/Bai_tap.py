'''Bai 1'''
print("**********BAI 1***********")
cau_tho = ""
with open("basnicka.txt", "w", encoding="utf-8") as f:
    while cau_tho!= 'stop':
        cau_tho = input("hay viet vao cau tho cua ban: ")
        if cau_tho == 'stop': break
        f.write(cau_tho + '\n')

'''Bai 2'''
print("**********BAI 2***********")
with open("basnicka.txt", "r", encoding="utf-8") as f:
    for dong in f:
        print('->'+dong)

'''Bai 3'''
print("**********BAI 3***********")
with open("basnicka.txt", "a", encoding="utf-8") as f:
    f.write("autor: Chagpt")
