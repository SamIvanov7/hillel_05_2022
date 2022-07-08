import asyncio
import random
import time

import aiohttp
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MAX_POKEMON = 100
SIZE = 1000
start_time = time.time()
print("=" * 70)


def get_pokemon_sync(id_: str) -> str:
    url = BASE_URL + id_
    response = requests.get(url)

    return response.json()["name"]


def get_random_id() -> str:
    random_id = random.randint(1, MAX_POKEMON + 1)
    return str(random_id)


def get_random_pokemon() -> str:
    random_id = get_random_id()
    return get_pokemon_sync(random_id)


def get_random_pokemon_url() -> str:
    random_id = get_random_id()
    return BASE_URL + str(random_id)


async def get_pokemon(my_session, get_random_pokemon_url):
    async with my_session.get(get_random_pokemon_url) as response:
        pokemon = await response.json()
        return pokemon["name"]


async def main():

    async with aiohttp.ClientSession() as my_session:

        tasks = []
        for _ in range(1, 50):
            pokemon_url = get_random_pokemon_url()
            tasks.append(asyncio.create_task(get_pokemon(my_session, pokemon_url)))

        pokemons = await asyncio.gather(*tasks)
    print(f"Our pokemons: {pokemons}")


asyncio.run(main())
print("--------- %s seconds ----------" % (time.time() - start_time))
