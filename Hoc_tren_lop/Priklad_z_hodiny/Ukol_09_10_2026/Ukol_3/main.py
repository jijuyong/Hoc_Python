def pridej_opravneni(profil, opravneni, role=None)-> dict:
    if role== None:
        relo=[]
    role.append(opravneni)
    profil["role"] = role
    return profil



def klonuj_a_uprav_profil(puvodni_profil, nova_data)->dict:
    return { k: nova_data[k] if k in nova_data else v for k,v in puvodni_profil.items() }
    # doc vong for truoc duyet key va value trong puvodni_profil
    # sao do neu Nếu k có trong nova_data, lấy giá trị mới nova_data[k].
    # #Nếu không có, giữ giá trị cũ v.

p1 = {"jmeno": "Jan", "prava": ["read","write"]}

kopie = klonuj_a_uprav_profil(p1, {"jmeno": "Petr", "prava": ["admin"]})
print("Původní:", p1)
print("Kopie:", kopie)
