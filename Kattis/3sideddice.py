import fractions

def gauss(matrika):
    '''
        na matriki opravi Gaussov postopek
    '''
    št_vrstic = len(matrika)
    # da vidimo razsežnost matrike
    št_stolpcev = len(matrika[0])
    kateri_stolpec = 0
    for števec in range(št_vrstic):
        for vrstica in range(kateri_stolpec, št_vrstic):
            if matrika[vrstica][števec] != 0:
                # poišče pivot (prvi neničelni člen)
                nenič_vrst = vrstica
                break
        else:
            continue
        matrika[kateri_stolpec], matrika[nenič_vrst] = matrika[nenič_vrst], matrika[kateri_stolpec]
        pivot = matrika[kateri_stolpec][števec]
        for j in range(št_stolpcev):
            # s pivotom uničiti (spremeni v 0) člene
            matrika[kateri_stolpec][j] /= pivot
        for k in range(št_vrstic):
            if k != kateri_stolpec:
                # čistimo še druge stolpce kjer s pivotom lahko
                koliko = matrika[k][števec]
                matrika[k] = [k_vrst - koliko * piv_vrst for k_vrst, piv_vrst in zip(matrika[k], matrika[kateri_stolpec])]
        kateri_stolpec += 1
    return matrika



def začetek():
    '''
        preveri če je matrika želimo linearna kombinacija podanih treh
    '''
    # večina kode ni moj "izum"
    matrika_vrstice = list()
    for _ in range(3):
        # preberemo in shranimo kot trojke trojk (matrika)
        vrstica = list(map(int, input().split()))
        if sum(vrstica) == 0:
            return False
        matrika_vrstice.append(vrstica)
    želimo = list(map(int, input().split()))
    matrika_vrstice = [[fractions.Fraction(x, 10000) for x in vrst] for vrst in matrika_vrstice]
    # shrani kot "matriko" v stolpcih
    matrika_stolpec = [[matrika_vrstice[j][i] for j in range(3)] for i in range(3)]
    # isto kot zgoraj le da je zapisana po stolpcih
    želimo = [fractions.Fraction(x, 10000) for x in želimo]
    # kar želimo pa zapišemo kot vekzor
    dodaj_stolpec = [matrika_stolpec[vrstica] + [želimo[vrstica]] for vrstica in range(3)]
    # podani matriki v stolpcih dodamo v nov stolpec še vektor želimo
    matrika_Gauss = gauss(dodaj_stolpec)
    rank = sum(1 for vrsta in matrika_Gauss if sum(vrsta[:-1]) != 0)
    # prešteje število neničelnih vrstic
    if rank == 1:
        print('YES' if želimo in matrika_vrstice else 'NO')
    elif rank == 2:
        preverjanje = False
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                stvari = list()
                for vrstica in range(3):
                    if matrika_stolpec[vrstica][i] == matrika_stolpec[vrstica][j]:
                        stopničke = None
                    else:
                        stopničke = (želimo[vrstica] - matrika_stolpec[vrstica][j]) / (matrika_stolpec[vrstica][i] - matrika_stolpec[vrstica][j])
                    if stopničke is not None:
                        stvari.append(stopničke)
                preverjanje |= all(0 < stopničke < 1 for stopničke in stvari) and (len(set(stvari)) == 1)
                # več pogojev hkrati preveri
        print('YES' if preverjanje else 'NO')
    else:
        if all(vrst[-1] > 0 for vrst in matrika_Gauss):
            print('YES')
        else:
            print('NO')
    return True

while True:
    res = začetek()
    if not res:
        break
    input()

