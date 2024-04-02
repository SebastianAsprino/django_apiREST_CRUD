import requests
from pokemon_api.models import Pokemon, Type
from django.http import JsonResponse
from pokemon_api.controllers.api.api import GETApiPokemon




#esto no funciona es solo guia
def fetch_and_create_pokemons(request):
    if not Pokemon.objects.exists():  # Comprueba si ya hay Pokémon en la base de datos
        for id in range(1, 501):  # Asumiendo que quieres traer 500 Pokémon como en tu ejemplo
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}').json()
            pokemon, created = Pokemon.objects.get_or_create(
                id=response['id'],
                name=response['name'],
                imagen=response['sprites']['other']['official-artwork']['front_default'],
                hp=next(item for item in response['stats'] if item["stat"]["name"] == "hp")['base_stat'],
                attack=next(item for item in response['stats'] if item["stat"]["name"] == "attack")['base_stat'],
                defense=next(item for item in response['stats'] if item["stat"]["name"] == "defense")['base_stat'],
                speed=next(item for item in response['stats'] if item["stat"]["name"] == "speed")['base_stat'],
                height=response['height'],
                weight=response['weight'],
                createdByDB=False,
            )
            for type_info in response['types']:
                type_name = type_info['type']['name']
                type_obj, _ = Type.objects.get_or_create(name=type_name)
                pokemon.types.add(type_obj)
    return JsonResponse({'status': 'Completed'})



def get_pokemons(request):
    return 0





# const { Pokemon, Type } = require("../db");
# const { GETApiPokemon } = require("./api");
# const { getDBInfoPokemon } = require("./DBinfo");
# const { GETType } = require("./type");

# const GETPokemon = async () => {
#   let AllPokemons = await getDBInfoPokemon();
#   if (!AllPokemons.length) {
#     const apiResponse = await GETApiPokemon();
#     const apiPokemon = apiResponse.map((pokemon) => {
#       return {
#         id: pokemon.id,
#         name: pokemon.name,
#         imagen: pokemon.sprites.other['official-artwork'].front_default,
#         hp: pokemon.stats.find(stat => stat.stat.name === "hp")?.base_stat ?? 0,
#         attack: pokemon.stats.find(stat => stat.stat.name === "attack")?.base_stat ?? 0,
#         defense: pokemon.stats.find(stat => stat.stat.name === "defense")?.base_stat ?? 0,
#         speed: pokemon.stats.find(stat => stat.stat.name === "speed")?.base_stat ?? 0,
#         height: pokemon.height,
#         weight: pokemon.weight,
#         createdByDB: false
#       };
#     });
#     await Pokemon.bulkCreate(apiPokemon);
#     const createdPokemons = await Pokemon.findAll();
#     const AllTypes = await GETType();
#     for (const createdPokemon of createdPokemons) {
#       const typesFromAPI = apiResponse.find(pokemon => pokemon.id === createdPokemon.id).types;
#       const associatedTypes = typesFromAPI.map(type => AllTypes.find(dbType => dbType.name === type.type.name));
#       const typeNames = associatedTypes.map(type => type.name);
#       let Arraytype = await Type.findAll({
#         where: {name: typeNames},
#       });
#       await createdPokemon.addType(Arraytype);
#     }
#     AllPokemons = await getDBInfoPokemon();
#   }
#   return AllPokemons;
# };

# module.exports = {
#   GETPokemon
# };