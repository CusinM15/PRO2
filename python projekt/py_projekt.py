
import requests
import re

neki = re.split(r'<PodatkiObjave>',requests.get('https://www.ajpes.si/ObjaveVPOFiles%5CObjaveVPO.xml').text)

for i, dr in enumerate(neki):
  znak = re.findall(r'<PodatekObjave ime=".+" opis=".+">.+</PodatekObjave>', dr)
  for aa in znak:
    aa = re.sub(r'<.*?>', '', aa)
    print(aa)
  if i > 10:
    break