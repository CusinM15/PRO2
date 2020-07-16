stevilke = '0123456789ACDEFHJKLMNPRTVWX'
slovar_stevk_ind = {v: i for i, v in enumerate(stevilke)}
# naredi slovar števk pri vsaki števki je vrednost indeks v stevilke


def resi(s):  # ta ni čisto moja last
    '''preveri če je prav podano in "izračuna" novo število'''
    t = [slovar_stevk_ind[c] for c in s]
    # seznam indeksov niza s po slovar_stevk_ind
    u, preveri = t[:-1], t[-1]  # zadnji element spravi v preveri
    vmes_ste = 2 * u[0] + 4 * u[1] + 5 * u[2] + 7 * u[3] + \
               8 * u[4] + 10 * u[5] + 11 * u[6] + 13 * u[7]
    # po 'formuli' v nalogi
    vmes_ste %= 27
    if vmes_ste != preveri:
        return 'Invalid'
    rez = 0
    for st in u:
        rez *= 27
        rez += st
    return rez

# prebere in izpiše
n = int(input())
for _ in range(n):
    m, s = input().split()
    rez = resi(s)
    print(m, rez)