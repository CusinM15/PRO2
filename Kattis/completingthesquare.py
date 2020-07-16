koordinate = list()
for _ in range(3):
    x, y = input().split()
    koordinate.append((int(x), int(y)))

def razdalja(kor1, kor2):
    '''
        vrne razdaljo med dvema točkama
    '''
    return ((kor1[0] - kor2[0]) ** 2 + (kor1[1] - kor2[1]) ** 2) ** 0.5

slo = dict()
najd = 0
for i, kor in enumerate(koordinate):
    dol = razdalja(koordinate[i], koordinate[i - 1])
    slo[(i, i - 1)] = dol
    if najd < dol:
        najd = dol
mno = set()
for kluč in slo:
    vrednost = slo[kluč]
    if vrednost == najd:
        for i in kluč:
            # našel sem najbolj oddaljeno točko
            mno.add(koordinate[i])
            koordinate.remove(koordinate[i])
koordinate = koordinate[0]
for i, kord in enumerate(mno):
    # naredim še vektorja
    if i == 0:
        vektor_a = [kord[0] - koordinate[0], kord[1] - koordinate[1]]
    else:
         vektor_b = [kord[0] - koordinate[0], kord[1] - koordinate[1]]
print(vektor_a[0] + vektor_b[0] + koordinate[0], vektor_a[1] + vektor_b[1] + koordinate[1])