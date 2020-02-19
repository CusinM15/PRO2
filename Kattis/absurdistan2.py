import math
n = int(input())

def nad(n, k):
    '''
        vrne rezultat n nad k
    '''
    if k < 0 or k > n or n < 0:
        return 0
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


def rešitev(n):
    '''
        vrne koliko % možnosti je da se izide
    '''
    slo = dict()
    k = 2
    while k <= n:
        # vmesh možnih je (k - 1)^k
        vmes = (k - 1) ** k
        vsota = 0
        prišrevek = 2
        while prišrevek < k:
            # koliko jih je treba odstraniti
            vmes_vsota = slo[prišrevek]
            vmes_vsota *= nad(k - 1, prišrevek - 1)
            vmes_vsota *= (k - prišrevek - 1) ** (k - prišrevek)
            vsota += vmes_vsota
            prišrevek += 1
        slo[k] = vmes - vsota
        k += 1
    vse_mozno = (n - 1) ** n
    reš = slo[n] / vse_mozno
    return reš
print('{0:.12f}'.format(rešitev(n)))