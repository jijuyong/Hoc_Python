class Hero:
    def __init__(self,ten:str,vukhi:str,nv:str,luong,):
        self.name = ten
        self.weapon = vukhi
        self.mission = nv
        self.salary = luong
    # muon ta ro rang object nay la gi : __str__
    def __str__(self):
        return 'Hero {}, power {}, mission {}, salary {}'.format(self.name,self.weapon,self.mission,self.salary)

    # thang anh em khac cua str
    def __repr__(self):
        return (
            f"Hero {self.name!r}, {self.weapon!r}, "
            f"{self.mission!r}, {self.salary!r}"
        )

    #tra ve do dai
    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.salary+ other

hero1 = Hero("Superman", "Sieu nang luc", "Bao ve thanh pho", 5000.0)
hero2 = Hero("Batman", "Batarang", "Bat toi pham", 4500.0)
hero3 = Hero("Wonder Woman", "Than kiem", "Cuu the gioi", 4800.0)
hero4 = Hero("Spider-Man", "Ban to nhien", "Cuu nguoi dan", 3500.0)
hero5 = Hero("Iron Man", "Giap cong nghe cao", "Chong ke xau", 6000.0)

#in thang ra
# print('*'*10,"in ra dia chi",'*'*10)
# print(hero1)# se in ra 1 cai dia chi nao do neu khong dunh han dinh nghia
print('*'*10,"in ra bang __str__",'*'*10)
print(str(hero1))#print(hero1)

print('*'*10,"in ra bang __repr__",'*'*10)
print(repr(hero2))

print('*'*10,"ham __len__",'*'*10)
print(f"do dai ten cua hero3 la: {hero3.__len__()}")

print('*'*10,"ham __add__",'*'*10)
print(f"luong cua hero4 + hero5 la {hero4.__add__(hero5.salary)}USD")




