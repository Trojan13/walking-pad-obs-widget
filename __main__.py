# Standard library imports
import json
import random
import datetime
import websockets
import asyncio
import configparser
import functools
import sys
import miio
# Reader imports
from miio import Walkingpad, DeviceException
from miio.walkingpad import (
    OperationMode,
    OperationSensitivity,
    WalkingpadException,
    WalkingpadStatus,
)


async def getWalkingPadState(walkingpad):
    state = walkingpad.status()
    v['sp'] = state.speed
    v['step'] = state.step_count
    v['cal'] = state.calories
    v['time'] = state.walking_time
    v['dist'] = state.distance
    return v


async def mainLoop(websocket, path, walkingpad):
    while True:
        values = await getWalkingPadState(walkingpad)
        await websocket.send(str(json.dumps(values)))
        await asyncio.sleep(1)


def main():
    parser = configparser.ConfigParser()
    parser.read_file(open(r'config.txt'))
    CONFIG_TOKEN = parser.get('walking-pad-twitch', 'token')
    CONFIG_IP = parser.get('walking-pad-twitch', 'ip')
    print("Config loaded...")
    print("Walkingpad connecting...")
    walkingpad = Walkingpad(CONFIG_IP, CONFIG_TOKEN)
    main_loop_handler = functools.partial(mainLoop, walkingpad=walkingpad)
    start_server = websockets.serve(main_loop_handler, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    print("Websocket Server started...")


if __name__ == "__main__":
    main()
