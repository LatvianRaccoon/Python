
import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://pokemondb.net/pokedex/all'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

pokemon_table = soup.find('table', id = 'pokedex')
row_data = []

for row in pokemon_table.find_all('tr'):
    col = row.find_all('td')
    col = [element.text.strip() for element in col]
    row_data.append(col)
df = pd.DataFrame(row_data)
print(df)
