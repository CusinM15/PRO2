mno = {('4 * 4','4 * 4'), ('4 + 4', '4 + 4'), ('4 - 4', '4 - 4'), ('4 // 4', '4 / 4')}
operacija = {(' * ', ' * '), (' + ', ' + '), (' - ', ' - '), (' // ', ' / ')}
# naredi slovar vseh možnih scenarijev
slov = dict()
for prvi in mno:
    for drugi in mno:
        for znak in operacija:
            slov[eval(prvi[0] + znak[0] + drugi[0])] = prvi[1] + znak[1] + drugi[1]
k = int(input())
for _ in range(k):
    n = int(input())
    if n in slov:
        print(slov[n],'=', n)
    else:
        print('no solution')
