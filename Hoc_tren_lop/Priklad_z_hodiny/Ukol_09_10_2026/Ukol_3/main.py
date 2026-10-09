def pridej_opravneni(profil, opravneni, role=None):


def klonuj_a_uprav_profil(puvodni_profil, nova_data):
    
    
p1 = {"jmeno": "Jan", "prava": ["read"]}
p2 = pridej_opravneni(p1, "write")

kopie = klonuj_a_uprav_profil(p1, {"jmeno": "Petr", "prava": ["admin"]})
print("Původní:", p1)
print("Kopie:", kopie)
