"""."""
import asyncio
import logging
import websockets

from websocket import Websocket

ws = Websocket()

logging.basicConfig()


server = websockets.serve(ws.chat, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(server)
asyncio.get_event_loop().run_forever()
