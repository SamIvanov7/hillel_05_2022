import asyncio
import time

import aiohttp

start_time = time.time()
print("=" * 70)


async def get_pokemon(my_session, pokemon_url):
    async with my_session.get(pokemon_url) as response:
        pokemon = await response.json()
        return pokemon["name"]


async def main():

    async with aiohttp.ClientSession() as my_session:

        tasks = []
        for pokemon_number in range(1, 50):
            pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
            tasks.append(asyncio.create_task(get_pokemon(my_session, pokemon_url)))

        pokemons = await asyncio.gather(*tasks)
    print(f"Our pokemons: {pokemons}")


asyncio.run(main())
print("--------- %s seconds ----------" % (time.time() - start_time))
