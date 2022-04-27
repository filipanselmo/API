import requests
from pprint import pprint
# response = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
# print(response.status_code)
# pprint(response.json())

class Hero():
    def __init__ (self,hero_name):
        self.hero_name = hero_name
heroes = [
Hero("Hulk"),
Hero("Captain America"),
Hero("Thanos")
]

def output_intelligence(heroes):
    intel_hero=[]
    for hero in heroes:
     response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero.hero_name}')
     intel_hero.append(int(response.json()['results'][0]["powerstats"]["intelligence"]))

    return intel_hero

def compare_intelligence(intelligences):
    max_iq = 0
    iq_hero = zip(intelligences, heroes)
    for intel, hero in iq_hero:
        if intel > max_iq:
            max_iq = intel
    return f'Самый умный герой это {hero.hero_name}, его интелект равен {max_iq}'
print(compare_intelligence(output_intelligence(heroes)))