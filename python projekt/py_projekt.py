import requests
import re


r = requests.get('https://www.ajpes.si/ObjaveVPOFiles%5CObjaveVPO.xml')
r.encoding = "utf-8"

neki = re.split(r'<PodatkiObjave>',r.text)

for i, dr in enumerate(neki):
  znak = re.findall(r'<PodatekObjave ime=".+" opis=".+">.+</PodatekObjave>', dr)
  for lastnost in znak:
    lastnost = re.sub(r'<.*?>', '', lastnost)
    print(lastnost)
  if i > 10:
    break