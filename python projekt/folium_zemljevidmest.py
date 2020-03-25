import requests
import re
from opencage.geocoder import OpenCageGeocode
import folium

key = '604f31fcadd74b4dbd1b90852d27606c' 

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

neki = re.split(r'<PodatkiObjave>',r.text)
sez_dru = list()
for i, dr in enumerate(neki):
    znak = re.findall(r'<PodatekObjave ime=".+" opis=".+">.+</PodatekObjave>', dr)
    vmes = list()
    for lastnost in znak:
        lastnost = re.sub(r'<.*?>', '', lastnost)
        vmes.append(lastnost)
    if len(vmes) == 14:
        sez_dru.append(vmes)

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
    vsa_dru.append((vsota_vseh, mesto))
vsa_dru.sort()
vsa_dru = vsa_dru[::-1]
 # ===============================================================

# izpisovanje lokacij na mapi prvih 10 mest
geocoder = OpenCageGeocode(key)
map = folium.Map(location = [46.119944, 14.815333], zoom_start = 9)
for stevilo, mesto in vsa_dru[:10]:
    koord = geocoder.geocode(mesto)
    lat = koord[0]['geometry']['lat']
    lon = koord[0]['geometry']['lng']
    folium.Circle(
        location = [lat, lon],
        clustered_marker = True,
        fill = True,
        popup = "{} \n {}".format(mesto, stevilo),
        radius = stevilo * 30,
        color = '#FF7912'
        ).add_to(map)


map.save('Zemljevid mest.html')
print('KONČANO!')
