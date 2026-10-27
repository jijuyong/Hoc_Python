class Hero:
    def __init__(self,ten,id,vu_khi):
        self._name =ten
        self._ID = id
        self.weapon = vu_khi

    @property # getter cho phep ban lay gia tri 
    #thuoc tinh khi o che do: protected, privated
    def name(self): return self._name

    @name.setter
    def name(self,other): 
        if other == None: raise ValueError("ten dang trong")
        self._name = other

print('*'*10,"Ham getter",'*'*10)
hero1 = Hero("Batman",665,"Day xich")
print(hero1.name) # neu khong co getter thi se bi loi, vi name la protected

print('*'*10,"Ham setter",'*'*10)
hero1.name = "dssd"
print(f"ten cua hero1 ssau khi dung setter la: {hero1.name}")

# ham deleter
del hero1.name
print(hero1.name)
# sau khi in ra se bi loi vi ko tim thay thuoc tinh hero1.name




