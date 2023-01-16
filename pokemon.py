import requests

class Pokemon:
    def __init__(self, url):
        self.url = url
        self.req = requests.get(self.url)
        self.data = self.req.json()

    def name(self):
        pokemon_name = self.data['forms'][0]['name']
        return pokemon_name
    
    def sprite(self):
        pokemon_sprite = self.data['sprites']['other']['official-artwork']['front_default']
        return pokemon_sprite

    def shiny_sprite(self):
        pokemon_sprite = self.data['sprites']['other']['official-artwork']['front_shiny']
        return pokemon_sprite

    def abilities(self):
        pokemon_abilities = self.data['abilities']
        abilities_list = []
        for i in range(len(pokemon_abilities)):
            abilities_list.append(pokemon_abilities[i]['ability']['name'])
        return abilities_list

    def type(self):
        pokemon_type = self.data['types'][0]['type']['name']
        return pokemon_type
