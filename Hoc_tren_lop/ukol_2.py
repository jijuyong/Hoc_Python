"""
Úkol 2: Datové struktury – řetězce, množiny, n-tice a slovníky.

Vyplňte těla jednotlivých funkcí podle zadání v komentářích a v README.md.
Neměňte názvy funkcí ani jejich parametry.
"""


def extrahuj_hashtagy(text: str) -> set[str]:
    text = text.split()
    znak = ",.?!;:"
    hashtagy = set()
    for i in text:
        i = i.lower()
        if "#" in i:
            i = i[1:]
            for j in znak:
                if j in i:
                    i=i[:-1]
                    hashtagy.add(i)
            hashtagy.add(i)
        elif znak in i:
            for j in znak:
                if j in i:
                    i = i[:-1]
                    hashtagy.add(i)
        else: hashtagy.add(i)

    return hashtagy

def porovnej_zajmy(student_a: set[str], student_b: set[str]) -> tuple[set[str], set[str], set[str]]:
    spolecne_zajmy = set()
    pouze_studenA = set()
    pouze_studenB = set()

    spolecne_zajmy = student_a & student_b
    pouze_student_a = student_a - student_b
    pouze_student_b = student_b - student_a

    return (spolecne_zajmy, pouze_student_a, pouze_student_b)


def katalog_knih(knihy: list[tuple[str, str, int]]) -> dict[str, list[str]]:
    katalog = {}
        
    for jmeno, zanr, rok in knihy:
        if zanr =="Sci-Fi" or zanr == "Fantasy":
            if zanr not in katalog:
                katalog[zanr] = []
        katalog[zanr].append(jmeno)
        if katalog[zanr] == []:
            return {}
    return katalog


def statistika_textu(text: str) -> dict:
    """
    Spočítá souhrnnou statistiku zadaného textu.

    Postup:
    1. Text převeďte na malá písmena.
    2. Odstraňte interpunkční znaménka: ',', '.', '!', '?', ':', ';'
    3. Rozdělte text na slova podle bílých znaků.
    4. Sestavte slovník s následujícími klíči:
       - "pocet_slov": celkový počet slov v textu (int)
       - "pocet_unikatnich": počet různých slov (int)
       - "nejdelsi_slovo": nejdelší nalezené slovo (str). Pokud má více slov stejnou
         maximální délku, vyberte první z nich. Pokud je text prázdný, hodnota je "".
       - "cetnost_delek": slovník (dict[int, int]), kde klíčem je délka slova a hodnotou
         je počet slov v textu s touto délkou.

    Pro prázdný text (nebo text obsahující pouze bílé znaky a interpunkci) vrátí:
       {"pocet_slov": 0, "pocet_unikatnich": 0, "nejdelsi_slovo": "", "cetnost_delek": {}}

    Příklad:
        text = "Rychlá hnědá liška skáče přes líného psa."
        statistika_textu(text) ->
        {
            "pocet_slov": 7,
            "pocet_unikatnich": 7,
            "nejdelsi_slovo": "rychlá",
            "cetnost_delek": {6: 2, 5: 3, 4: 1, 3: 1}
        }
    """
    # TODO: Doplňte implementaci
    return {
        "pocet_slov": 0,
        "pocet_unikatnich": 0,
        "nejdelsi_slovo": "",
        "cetnost_delek": {}
    }


def main():
    print("=== Testování funkcí Úkolu 2 ===")
    
    text = "Učíme se #Python a #datové_struktury! #python je #super."
    tagy = extrahuj_hashtagy(text)
    print(f"1. Hashtagy: {tagy}")

    a = {"python", "c++", "linux"}
    b = {"python", "sql", "git"}
    spolecne, pouze_a, pouze_b = porovnej_zajmy(a, b)
    print(f"2. Zájmy - Společné: {spolecne}, Pouze A: {pouze_a}, Pouze B: {pouze_b}")

    knihy = [
        ("1984", "Sci-Fi", 1949),
        ("Pán prstenů", "Fantasy", 1954),
        ("Duna", "Sci-Fi", 1965),
        ("Hobit", "Fantasy", 1937)
    ]
    kat = katalog_knih(knihy)
    print(f"3. Katalog podle žánrů: {kat}")

    ukazka = "Rychlá hnědá liška skáče přes líného psa."
    stats = statistika_textu(ukazka)
    print(f"4. Statistika textu: {stats}")


if __name__ == "__main__":
    main()
