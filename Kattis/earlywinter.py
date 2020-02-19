n, danM = map(int, input().split())
# n = koliko let nazaj oz. koliko primerov bo v drugem
# vnosu, danM pa dan prvega snega
n_let = input().split()
# danM zadnjih n let
koliko = 0
for dn in n_let:
    # samo preveri ce je katero leto že prej snežilo
    if int(dn) <= danM:
        print("It hadn't snowed this early in {0} years!".format(koliko))
        break
    else:
        koliko += 1
if koliko == n:  # ce pride skozi celo zanko in ni ikoli bilo
    print("It had never snowed this early!")