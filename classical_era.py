import random as rand
import requests
import pprint
import json

def get_composers(epoch: str):
    url = f"https://api.openopus.org/composer/list/epoch/{epoch}.json"
    response = requests.get(url)
    composers_dict = response.json()
    # pprint.pp(composers_dict)
    return composers_dict

eras = ["Medieval", "Renaissance","Baroque","Classical","Early Romantic","Romantic","20th Century","Post-War","21st Century"]

composers_by_era_with_years = {}

for era in eras:
    data = get_composers(era)
    for composer in data.get("composers", []):
        name = composer['complete_name']
        composers_by_era_with_years[f'{name}'] = {
            'epoch / genre': era,
        }

with open('classical_artists_with_eras.json', 'w') as f:
    json.dump(composers_by_era_with_years,f, ensure_ascii=False, indent = 2)


