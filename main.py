# https://bungie-net.github.io/multi/index.html
# https://bungie-net.github.io/multi/schema_Destiny-DestinyComponentType.html
# https://github.com/Bungie-net/api/wiki/OAuth-Documentation
# https://www.bungie.net/en/Application/Detail/49952
# https://github.com/jgayfer/pydest
# https://discord.com/developers/docs/intro

import pydest
import asyncio
import json

#import .env file
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv('API_KEY')

async def main():
    """You will need to add your api key!"""
    destiny = pydest.Pydest(api_key)

    data = await destiny.api.get_character(2, '4611686018428865770',2305843009266360807,[201])

    print(json.dumps(data, indent=4, sort_keys=True))

    # #Fuction that saves the data to a json file
    # def save_json(data, filename):
    #     with open(filename, 'w') as f:
    #         json.dump(data, f, indent=4, sort_keys=True)

    # #Save the data to a json file
    # save_json(data, 'character1.json')

    await destiny.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()