# koda za branje podatkov
# ...
# zmišleni podatki...
vsehPostelj = 1000
prostihPostelj = 200
zasedenihPostelj = 800

vsehVentilatojev = 600
delujocihVentilatorjev = 450
uporabljenihVentilatorejv = 440

# kašen graf bo treba narest je ful odvisen on kašni podatki bojo podani
# https://matplotlib.org/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))

# postelje
plt.subplot(131)
names = ["vsehPostelj", "prostihPostelj", "zasedenihPostelj"]
values = [vsehPostelj, prostihPostelj, zasedenihPostelj]
plt.bar(names, values)
plt.title("Postelje")
plt.xlabel("Vrste Postelj")
plt.ylabel("Število")

# ventilatorji
# neki podobnega
plt.subplot(133)
names = ["vsehVentilatojev", "delujocihVentilatorjev", "uporabljenihVentilatorejv"]
values = [vsehVentilatojev, delujocihVentilatorjev, uporabljenihVentilatorejv]
plt.scatter(names, values)
plt.title("Ventilatorji")
plt.xlabel("Vrste Ventilatorjev")
plt.ylabel("Število")

plt.savefig("Grafi.pdf")
# besede se mal prekrivajo sam pr dejasnkih podatkih to pomojem ne bo problem