def skalarni_produkt(og1, og2, og3):
    '''
        vrne skalarni produkt
        <(ogl2 - ogl1), (ogl3 - ogl1)>
    '''
    x1, y1 = og1
    x2, y2 = og2
    x3, y3 = og3
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


def uredi_vrstni_red(sez_oglišč):
    '''
        vrne urejen vrstni red
    '''
    koliko = len(sez_oglišč)
    sez_oglišč = set(sez_oglišč)
    if koliko == 1:
        print(sez_oglišč)
    sez_oglišč = sorted(sez_oglišč)
    sez1 = list()
    sez2 = list()
    for ogl in sez_oglišč:
        while len(sez1) > 1 and skalarni_produkt(sez1[-2], sez1[-1], ogl) > 0:
            sez1.pop()
        while len(sez2) > 1 and skalarni_produkt(sez2[-2], sez2[-1], ogl) < 0:
            sez2.pop()
        sez2.append(ogl)
        sez1.append(ogl)
    urejeno = sez2 + sez1[1: -1][:: -1]
    return urejeno


def branje_izpis():
    '''
        prebere in izpiše
    '''
    št_ogl = int(input())
    vsa_ogl = list()
    for _ in range(št_ogl):
        x, y, parameter = input().split()
        if parameter == 'Y':
            vsa_ogl.append((int(x), int(y)))
    rešitev = uredi_vrstni_red(vsa_ogl)
    print(len(rešitev))
    for x, y in rešitev:
        print(x, y, sep = ' ')

branje_izpis()