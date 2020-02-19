def štej(niz):
    '''
        vrne število elementov ki so različni od prejšnega
    '''
    barve = 1
    for i in range(len(niz)):
        if niz[i] != niz[i - 1]:
            barve += 1
    if barve % 2 == 1:
        # to pomeni sodo ujemanje znakov
        barve -= 1
    return barve


def kontrola(v):
    '''
        preveri če je vsaj en sosodnji par (ali pa prvi in zadnji) enak
    '''
    for i in range(len(v)):
        if v[i] == v[i - 1]:
            return True
    return False


def glavno():
    '''
        ta program pa preveri ali je možno
    '''
    n = int(input())
    imajo = input()
    želijo = input()
    if želijo == imajo:
        return 'yes'
    barv_imaj = štej(imajo)
    barv_želi = štej(želijo)
    if barv_imaj < 1:
        # če ni nobenega ujemanja
        return 'no'
    if barv_imaj > barv_želi:
        # če imemo več "skupnih" kot pa jih želimo se da
        return 'yes'
    if barv_imaj < barv_želi:
        return 'no'
    if barv_imaj == barv_želi and kontrola(želijo):
        # če jih je enako se da,  razen če nima nobenega sosednjega
        return 'yes'
    else:
        return 'no'
print(glavno())
