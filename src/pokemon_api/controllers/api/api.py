import requests

def GETApiPokemon():
  REQUESTS = 2 #de momento 2 por que osino me acabo el internet xd
  pokemons = []
  for id in range(1, REQUESTS + 1):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    pokemon_data = response.json()
    pokemons.append(pokemon_data)
  return pokemons


test =  GETApiPokemon()
print(test)

# import requests

# def get_api_pokemon():
#     requests = 500  # Los Pokémon llegan por ID; actualmente estoy trayendo solo 500
#     pokemons = []
#     for id in range(1, requests + 1):
#         response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
#         pokemon_data = response.json()
#         pokemons.append(pokemon_data)
#     return pokemons

# def get_api_type():
#     response = requests.get('https://pokeapi.co/api/v2/type')
#     types_data = response.json()
#     return types_data



# const fetch = require("node-fetch");

# const GETApiPokemon = async () => {
#   const Requests = 500; // los pokemos llegan por ID actualmente estoy trayendo solo 500
#   const Pokemons = [];  
#   for (let id = 1; id <= Requests; id++) {
#     const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
#     .then(response => response.json());
#     Pokemons.push(response);
#   }
#   return Pokemons;
# };

# const GETApiType = async () => {
#   const Types = await fetch(
#     'https://pokeapi.co/api/v2/type'
#   ).then((response) => response.json());
#   return Types;
# };

# module.exports = { 
#   GETApiPokemon,
#   GETApiType
# };