stevilo = int(input())
stej = 0
i = 1
while i * i <= stevilo:
    # kvadrat zato ker do kvadrata zadnjega
    # ker določenih ni treba preverjati
    if stevilo % i == 0:
        stevilo = stevilo / i
        stej += 1
        i = 1
    if stevilo == 1:
        stej += 1
    i += 1
print(stej)