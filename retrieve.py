import requests
import concurrent.futures

def retrieve_all():
    urls = [
        f'https://pokeapi.co/api/v2/pokemon/{i}' for i in range(1, 800)
    ]

    session = requests.Session()
    def get_url(url):
        response = session.get(url)
        return response.json()

    pokemons = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(get_url, url) for url in urls]

        for future in concurrent.futures.as_completed(results):
            data = future.result()
            pokemons[data['forms'][0]['name']] = [data['sprites']['other']['official-artwork']['front_default'], data['types'][0]['type']['name']]

    return pokemons
