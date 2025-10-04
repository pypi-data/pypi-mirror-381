import asyncio
from websockets.asyncio.client import connect
async def hello():

    client = wait async with connect("ws://127.0.0.1:9080") as websocket:
        client = websocket
        # await websocket.send("Hello world!")
        # message = await websocket.recv()
        # print(message)
    await client.send('Hello world')

if __name__ == "__main__":
    asyncio.run(hello())