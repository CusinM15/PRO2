import io
file = io.open("Clanki.txt", mode="r", encoding="utf-8")
# lahko tudi samo
# file = open("Clanki.txt", "r")
# samo ta funkcija nima utf-8 branja

koncnSeznam = list()
text = file.readlines()
for line in text:
    besede = list(line.split(","))
    if besede[0].count(" ") == 1:
        koncnSeznam.append(besede[0])
        koncnSeznam.append(len(besede)-1)

        tocke = 0.0
        for beseda in besede[1:]:
            tocke += float(beseda.split(":")[1])
        koncnSeznam.append(tocke)

try:
    file = io.open("seznam.txt", "x", encoding="utf-8")
except:
    file = io.open("seznam.txt", "w", encoding="utf-8")
# enako kot na začetku, lahko samo     file = open("seznam.txt", "x")

i = 0
for element in koncnSeznam:
    print(element)
    if i == 3:
        i = 0
        file.write("\n")
    file.write(str(element))
    file.write(", ")
    i += 1
