import requests
import re


class drustvo:
    def __init__(self, sez):
        self.maticna = sez[0]
        self.ime = sez[1]
        self.mesto = sez[2]
        self.naziv = sez[4]
        self.dejavnost = sez[6]
        self.datum = sez[7]
        self.zap_ste = sez[8]
        self.aktivnost = sez[10]
        self.naslov = sez[11]
        self.prosto = sez[13]

    def __str__(self):
        return self.ime + 'je društvo iz ' + self.mesto + ', ki se ukvarja' + self.dejavnost

    def __repr__(self):
        return self.ime + ', ' + self.naslov


r = requests.get('https://www.ajpes.si/ObjaveVPOFiles%5CObjaveVPO.xml')
r.encoding = "utf-8"

neki = re.split(r'<PodatkiObjave>', r.text)
sez_dru = list()
for i, dr in enumerate(neki):
    znak = re.findall(r'<PodatekObjave ime=".+" opis=".+">.+</PodatekObjave>', dr)
    vmes = list()
    for lastnost in znak:
        lastnost = re.sub(r'<.*?>', '', lastnost)
        vmes.append(lastnost)
    if len(vmes) == 14:
        sez_dru.append(vmes)

# # Izpiše seznam vseh društev, ki imajo iskano vrednost
# vsa_dru = list()
# while True:
#     mesto = input('Ime mesta: ')  # za primer če iščeš samo mesta
#     if mesto == 'konec':
#         break
#     for i in range(len(sez_dru)):
#         if mesto in sez_dru[i]:
#             vsa_dru.append(sez_dru[i][1])
#     if len(vsa_dru) == 0:
#         print('Teh podatkov ni!')
#     else:
#         print(vsa_dru)
#         vsa_dru = list()

# ===============================================================
slovar = dict() # {mesto:{dejavnost:{imena}}}
vsa_dru = list()
for i in range(len(sez_dru)):
    firma = sez_dru[i][1]
    firma = drustvo(sez_dru[i])
    if firma.mesto in slovar:
        if firma.dejavnost in slovar[firma.mesto]:
            slovar[firma.mesto][firma.dejavnost] += 1
        else:
            slovar[firma.mesto][firma.dejavnost] = 1
    else:
        slovar[firma.mesto] = {firma.dejavnost: 1}


for mesto, slo2 in slovar.items():
    vsota_vseh = sum(slovar[mesto].values())
    slovar[mesto] = [slovar[mesto], vsota_vseh]
print(slovar)
# ======================================================