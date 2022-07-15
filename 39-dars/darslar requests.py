import requests
from pprint import pprint

sahifa = "https://kun.uz/ru"
r = requests.get(sahifa)
pprint(r.text)

country = "Uzbekistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json['capital'])    
