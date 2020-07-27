"""."""
import asyncio
import json
import datetime

from event import Event


class Websocket(Event):
    """."""

    def __init__(self):
        """."""
        self.consumers = set()

        Event.__init__(self)

    async def connect(self, consumer):
        """."""
        self.consumers.add(consumer)

    async def close(self, consumer):
        """."""
        self.consumers.remove(consumer)

    async def send(self):
        """."""
        if self.consumers:

            await asyncio.wait(
                [i.send(self.get_event()) for i in self.consumers])

    async def chat(self, consumer, path):
        """."""
        await self.connect(consumer)

        await consumer.send(self.get_event())

        try:

            async for i in consumer:

                data = json.loads(i)

                time = datetime.datetime.now()

                self.time = time.strftime("%d %b %Y, %H:%M")

                self.message = data["message"]

                await self.send()
        finally:
            await self.close(consumer)
