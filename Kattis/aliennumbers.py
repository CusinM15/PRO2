def razreši(stevilo, vhod_sistem, izhod_sistem):
    '''pretvori stevilo iz vhodnega sistema v izhodni'''
    vnos_slovar = {v: i for i, v in enumerate(vhod_sistem)}
    # slovar vhodnega sistema zato da potem deluje hitreje
    vmes = 0
    for ind, znak in enumerate(stevilo[::-1]):
        # zato da prevede v desetiški sistem, -1 zato da začnemu pri 10^0 itd.
        vmes += vnos_slovar[znak] * len(vhod_sistem) ** ind
    rez = ''
    while vmes:
        # sedaj pa še iz desetiškega nazaj v želen sistem
        rez = izhod_sistem[vmes % len(izhod_sistem)] + rez
        vmes //= len(izhod_sistem)
        # zato da odrežemo dosti stran
    return rez

c = int(input())
kateri = 0
for e in range(c):
    original, vhod, izhod = input().split()
    kateri += 1
    print('Case #{0}: {1}'.format(kateri, razreši(original, vhod, izhod)))
