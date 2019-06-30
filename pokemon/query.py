# Import requests and Python's core JSON library.
import requests
import json

BASE_URL = 'http://pokeapi.co'

def query_pokeapi(resource_url):
    url = '{0}{1}'.format(BASE_URL, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None

def pokedex_description(pokemon_species):
    url = '{0}{1}'.format(BASE_URL, pokemon_species)
    response_two = requests.get(url)

    if response_two.status_code == 200:
        return json.loads(response_two.text)
    return None

charizard = query_pokeapi('/api/v1/pokemon/charizard/')
charizard_description = pokedex_description('/api/v2/pokemon-species/6/')

description = charizard_description['flavor_text_entries'][1]['flavor_text']
name = charizard['name']
sprite = charizard['sprites']['front_default']

# sprite = query_pokeapi(sprite_uri)
# print (sprite)
print (charizard['game_indices'][0]['game_index'])

# Create url containing url to the PokeAPI
# Make HTTP Request using requests' get() function
# Store results in a variable called response
# url = 'http://pokeapi.co/api/v1/pokemon/charizard/'
# url_two = 'https://pokeapi.co/api/v2/pokemon-species/6/'
# response = requests.get(url)

# response_two = requests.get(url_two)
# if response.status_code == 200:
#     data = json.loads(response.text)
#     data_two = json.loads(response_two.text)
#     print (data['name'])
#     print (data_two['flavor_text_entries'][1]['flavor_text'])
#     print (data['sprites']['front_default'])
#     print (data['game_indices'][0]['game_index'])
# else:
#     print ('An error occurred querying the API')

