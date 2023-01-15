import requests

class Pokemon:
    def __init__(self, url):
        self.url = url

    def name(self):
        req = requests.get(self.url)
        data = req.json()
        pokemon_name = data['forms'][0]['name']
        return pokemon_name
    
    def sprite(self):
        req = requests.get(self.url)
        data = req.json()
        pokemon_sprite = data['sprites']['other']['official-artwork']['front_default']
        return pokemon_sprite

    def shiny_sprite(self):
        req = requests.get(self.url)
        data = req.json()
        pokemon_sprite = data['sprites']['other']['official-artwork']['front_shiny']
        return pokemon_sprite

    def abilities(self):
        req = requests.get(self.url)
        data = req.json()
        pokemon_abilities = data['abilities']
        abilities_list = []
        for i in range(len(pokemon_abilities)):
            abilities_list.append(pokemon_abilities[i]['ability']['name'])
        return abilities_list

pokemon = Pokemon('https://pokeapi.co/api/v2/pokemon/ditto')



    
