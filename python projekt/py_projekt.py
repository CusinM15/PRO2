
import requests
import re

'Kvakavajo žabe'

"""
p2.3 - Game of Thrones characters
"""

chars = [re.sub(r'<.*?>', '', re.sub(r'<sup>\d</sup>', '', char)) for char in re.findall(r'<td><a href="/wiki/.+" title=".+">.+</a>.*</td>', re.split(r'<span class="mw-headline" id="Recurring_/_Guest_cast">Recurring / Guest cast</span>', requests.get('https://en.wikipedia.org/wiki/List_of_Game_of_Thrones_characters').text)[0])]

print("{0:>30s} | {1:s}".format('Character', 'Actor/Actress'))
for i in range(0, len(chars), 2):
  print("{0:>30s} | {1:s}".format("'" + chars[i + 1] + "'", "'" + chars[i] + "'"))
print()

"""
p2.4 - Movies and OMDb API
"""

OMBD_KEY = 'cd9ba7d7'

def omdb(tit):
  movie = requests.get('http://www.omdbapi.com/?t=' + re.sub(r'\s', '+', tit) + '&apikey=' + OMBD_KEY).json()
  print("{0:>12s} | '{1:s}' ({2:d})".format('Title', movie['Title'], int(movie['Year'])))
  print("{0:>12s} | '{1:s}'".format('Genre', movie['Genre']))
  print("{0:>12s} | {1:.1f} ({2:,d} votes)".format('IMDb', float(movie['imdbRating']), int(movie['imdbVotes'].replace(',', ''))))
  print("{0:>12s} | '{1:s}'".format('Language', movie['Language']))
  print("{0:>12s} | '{1:s}'".format('Country', movie['Country']))
  print("{0:>12s} | {1:s}\n".format('Runtime', movie['Runtime']))

omdb('Bohemian Rhapsody')
omdb('Guardians of the Galaxy')
omdb('The Godfather')