from abc import ABC,abstractmethod

class animal:

    @abstractmethod
    def make_a_noise(self):
        pass

class Dog(animal):
    def make_a_noise(self):
        return "Half, Half!"

class Cat(animal):
    def make_a_noise(self):
        return "Meow, Meow!"

class Kohout(animal):
    def make_a_noise(self):
        return "Kikiriki!"

def make_noises(dong_Vat):
    print(dong_Vat.make_a_noise())

dan_dong_Vat = [Dog(),Cat(),Kohout()]

for i in dan_dong_Vat:
    make_noises(i)