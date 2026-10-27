class Vozidlo:
    def __init__(self,znacka):
        self.znacka = znacka
        self.motor_bezi = False

    def nastartuj(self):
        self.motor_bezi = True
        print(f"{self.znacka}: motor bezi")

class Auto(Vozidlo):# dedime z vozidlo
    def zatrub(self):
        print(f"{self.znacka}: Tuuut!")


auto1 = Auto("Skoda")

auto1.zatrub()

#ham super
class Autobus(Vozidlo):
    def __init__(self, znacka,pocet_sedadel):
        super().__init__(znacka)
        # nay co nghia la de cho class bo me nastavit znacku
        self.pocet_sedadel = pocet_sedadel
        # cai nay la thuoc tinh cua class con

    def __repr__(self):
        return f"znacka: {self.znacka!r}, pocet sedadel: {self.pocet_sedadel!r}"


bus = Autobus("Karosa",45)
bus.__repr__()
bus.nastartuj()


