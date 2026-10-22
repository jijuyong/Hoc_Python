#pubilc-cong khai
class Person:
    def __init__(self,name):
        self.name = name
person = Person("Binh")

print(f"ten cua person la: {person.name}")

person.name = "An"#co the thay doi dc vi dung public
print(f"ten cua person sau khi thay doi la: {person.name}")


#Protected - duoc bao ve
class Animal:
    def __init__(self,typy):
        self._typy = typy

animal = Animal("Pes")
print(f"Loai con vat: {animal._typy}")

animal._typy = "Kocka"
print(f"Loai con vat sau khi thay doi la: {animal._typy}")

#private - rieng tu
class Skola:
    def __init__(self,chuc_vu):
        self.__chuc_vu = chuc_vu

cv1 = Skola("giao vien")
#print(f"chuc vu cua cv1 la: {cv1.__chuc_vu}")
#se bi loi vi la private
print(f"chuc vu cua cv1 la: {cv1._Skola__chuc_vu}")

#properties - getter va setter

class Jidlo:
    def __init__(self,typy):
        self._typy = typy

    @property
    def typy(self):
        return self._typy

    @typy.setter
    def typy(self,jaky):
        if jaky=="pomeranc":
            return "Khong thich an"
        else:
            self._typy = jaky

otazka = input("typni muj oblibeny typy jidlo: ")
j1 = Jidlo(otazka)

print(f"si typoval: {j1.typy}")# dang dung getter
while j1.typy =="pomeranc":
    j1.typy = input("typni znovu: ") # dang dung setter
    # neu ghi la j1._typy = "chipsy" 
    # thi se sua thang luon khong goi ham setter de kiem tra nua







