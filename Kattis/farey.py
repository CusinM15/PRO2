def razbitje(število):
    '''
        vrne množico praštevil iz katerih je število
        (če je več istih le enega)
    '''
    mn = set()
    i = 2
    while število != 1:
        if število % i == 0:
            mn.add(i)
            število //= i
        else:
            i += 1
    return mn


def euler_theorem(sez, n):
    '''
        vrne razliko v dolžini različnih
        ulomkov od prejšnega člena
    '''
    prod = 1
    for i in sez:
        # Euler’s totient function
        prod *= 1 - 1 / i
    prod *= n
    return prod


def rešitev():
    '''
        vrne slovar rešitev
    '''
    slo = dict()
    slo[2] = 3
    for i in range(3, 10001):
        # po Eulerju je naslednji  čleb tak
        slo[i] = slo[i - 1] + euler_theorem(razbitje(i), i)
    return slo

rez = rešitev()

C = int(input())
for _ in range(C):
    k, st = map(int, input().split())
    print(k, int(rez[st]))