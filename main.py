from flask import Flask, render_template, request
from pokemon import Pokemon
from retrieve import retrieve_all


app = Flask(__name__)

@app.route('/')
def index():
    pokemons = retrieve_all()
    return render_template(['index.html', 'gallery.html'], pokemons=pokemons)

@app.route('/', methods=['POST'])
def index_post():
    pokemon_request = request.form.get('pokemonName')
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_request}'
    pokemon = Pokemon(url)
    return render_template('index.html', pokemon_name=pokemon.name(), pokemon_sprite=pokemon.sprite())

@app.route('/<pokemon_name>')
def pokemon_details(pokemon_name):
    pokemon = Pokemon(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    pokemonName = pokemon.name()
    pokemonSprite = pokemon.sprite()
    pokemonShinySprite = pokemon.shiny_sprite()
    pokemonAbilities = pokemon.abilities()
    pokemonType = pokemon.type()
    return render_template('pokemon.html', pokemonName=pokemonName, pokemonSprite=pokemonSprite, pokemonShinySprite=pokemonShinySprite, pokemonAbilities=pokemonAbilities, pokemonType=pokemonType)

if __name__ == '__main__':
    app.run(debug=True)
