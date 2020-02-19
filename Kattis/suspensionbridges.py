import math
razdalja, upogib = map(int, input().split())


def f(a, d, s):
    '''prvo enačba v nalogi "enačim z 0"'''
    return a * math.cosh(d / (2 * a)) - a - s


def iskanje_a(levo, desno, razdalja, upogib):
    '''
        izračuna a (parameter) s katerih izračunam razdaljo
    '''
    meja = (levo + desno) / 2
    primerjava = f(meja, razdalja, upogib)
    if abs(primerjava) < 0.000001:
        return meja
    if primerjava > 0:
        # s pomočjo bisekcije da prideš vedno bližje
        return iskanje_a(meja, desno, razdalja, upogib)
    else:
        if primerjava < 0:
            return iskanje_a(levo, meja, razdalja, upogib)
        else:
            return meja
a = iskanje_a(0, 1000000000, razdalja, upogib)
print(2 * a * math.sinh(razdalja / (2 * a)))

