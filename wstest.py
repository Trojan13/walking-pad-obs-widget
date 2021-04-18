import asyncio
import websockets
import configparser
import datetime
import random
import json

parser = configparser.ConfigParser()
parser.read_file(open(r'config.txt'))
CONFIG_TOKEN = parser.get('walking-pad-twitch', 'token')
CONFIG_IP = parser.get('walking-pad-twitch', 'ip')
print(CONFIG_TOKEN)
print(CONFIG_IP)


async def getSimulateNum(v):
    print(v)
    v['sp'] = random.uniform(4, 5)
    v['step'] = v['step'] + 1
    v['cal'] = v['cal'] + 1
    v['time'] = v['time'] + 1
    v['dist'] = v['dist'] + 0.01
    return v


async def time(websocket, path):
    values = {
        'sp': 5.0,
        'step': 2400,
        'cal': 500,
        'time': 12,
        'dist': 0.5,
        'mode': 'walk',
    }
    while True:
        values = await getSimulateNum(values)
        await websocket.send(str(json.dumps(values)))
        await asyncio.sleep(1)

start_server = websockets.serve(time, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
