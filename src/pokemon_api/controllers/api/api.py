import requests

def GETApiPokemon():
  REQUESTS = 2 #de momento 2 por que osino me acabo el internet xd
  pokemons = []
  for id in range(1, REQUESTS + 1):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    pokemon_data = response.json()
    pokemons.append(pokemon_data)
  return pokemons



def GETApiType():
  response = requests.get('https://pokeapi.co/api/v2/type')
  types_data = response.json()
  return types_data
