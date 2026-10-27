
class BankovniUcet:
    def __init__(self,cislo_uctu: str,majitel: str,pocatecni_zustatek: float = 0.0) -> None:
        self._cislo_uctu = cislo_uctu
        self.majitel = majitel
        self.zustatek = pocatecni_zustatek
        self._historie: list[tuple[str, float]] = []

        if pocatecni_zustatek is not None:
            self._historie.append(("Vklad", pocatecni_zustatek))

    @property
    def zustatek(self) -> float:
        return self._zustatek
    @zustatek.setter
    def zustatek(self, value: float) -> None:
        if value < 0:
            raise ValueError("Zustatek nemuze byt zaporny.")
        self._zustatek = value

    @property
    def majitel(self) -> str:
        return self._majitel
    @majitel.setter
    def majitel(self, novy_jmeno: str) -> None:
        novy_jmeno = novy_jmeno.strip()
        if novy_jmeno == "":
            raise ValueError("Jmeno majitele nesmi byt prazdne.")
        self._majitel = novy_jmeno

    @property
    def cislo_uctu(self) -> str:
        return self._cislo_uctu

    def vloz(self, castka: float) -> bool:
        if castka <= 0:
            return False

        self._zustatek += castka
        self._historie.append(("Vklad", castka))
        return True

    def vyber(self, castka: float) -> bool:
        if castka <= 0 or castka > self._zustatek:
            return False

        self._zustatek -= castka
        self._historie.append(("Vyber", castka))
        return True

    def vypis_transakce(self) -> list[str]:
        vysledek: list[str] = []

        for typ, castka in self._historie:
            if typ == "Vklad":
                vysledek.append(f"Vklad: +{castka:.2f} Kc")
            else:
                vysledek.append(f"Vyber: -{castka:.2f} Kc")

        return vysledek

    def __str__(self) -> str:
        return (
            f"Ucet {self._cislo_uctu} ({self._majitel}) - "
            f"Zustatek: {self._zustatek:.2f} Kc"
        )

    def __repr__(self) -> str:
        return (
            f"BankovniUcet(cislo_uctu={self._cislo_uctu!r}, "
            f"majitel={self._majitel!r}, "
            f"zustatek={self._zustatek!r})"
        )


class Banka:
    def __init__(self, nazev: str) -> None:
        self.nazev = nazev
        self._ucty: dict[str, BankovniUcet] = {}#key la stk,value kieu bankovni ucet

    def zaloz_ucet(self,cislo_uctu: str,majitel: str,pocatecni_vklad: float = 0.0) -> BankovniUcet:
        if cislo_uctu in self._ucty:
            raise ValueError(f"Ucet {cislo_uctu} jiz existuje.")

        ucet = BankovniUcet(
            cislo_uctu, majitel, pocatecni_vklad
        )
        self._ucty[cislo_uctu] = ucet
        return ucet

    def ziskej_ucet(
        self, cislo_uctu: str
    ) -> BankovniUcet | None:
        return self._ucty.get(cislo_uctu)

    def preved_penize(
        self,
        z_uctu: str,
        na_ucet: str,
        castka: float
    ) -> bool:
        darce = self.ziskej_ucet(z_uctu)
        prijemce = self.ziskej_ucet(na_ucet)

        if darce is None or prijemce is None:
            return False

        if darce is prijemce:
            return False

        if not darce.vyber(castka):
            return False

        prijemce.vloz(castka)
        return True

    @property
    def celkovy_kapital(self) -> float:
        return sum(
            ucet.zustatek for ucet in self._ucty.values()
        )


banka = Banka("Python Banka")

ucet1 = banka.zaloz_ucet("111/0800", "Jan Novák", 1000.0)
ucet2 = banka.zaloz_ucet("222/0800", "Eva Černá", 500.0)

ucet1.vloz(500.0)
ucet1.vyber(200.0)

uspech = banka.preved_penize(
    "111/0800", "222/0800", 300.0
)
print(f"Prevod probehl: {uspech}")

print(ucet1)
print(ucet2)
print("Celkovy kapital banky:", banka.celkovy_kapital)
print("Historie uctu 1:", ucet1.vypis_transakce())
