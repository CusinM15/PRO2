dol = 622
v0 = 80 / 3.6
def povprecna_hitrost(l, z, k):
    '''
        vrne povprečno hitrost za pot dolžine l vstopni in iztopni čas z, k
    '''
    return l / (k - z) # vrne v m/s

def krsitve(podatki, krsitve):
    '''
        prebere podatkee iz datoteke in vrne kršitelje
    '''
    kršitelj = 0
    rez = open(krsitve, 'w')
    bes = open(podatki).readlines()
    for vrst in bes:
        (z, k, r) = vrst.split()
        v = povprecna_hitrost(dol, int(z), int(k))
        if v > v0:
            kršitelj += 1
            rez.write(r + ' ' + str(v) + ' m/s\n')
    rez.close()
    return kršitelj

print(krsitve('119.txt', 'rez.txt'))
