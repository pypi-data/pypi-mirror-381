import asyncio
import json
import queue
import threading
from time import sleep
from typing import AsyncIterator, Iterator

import websockets

from candela_kit.dtos import TraceEventDefinition, Session
from candela_kit.event import Event


class CandelaStreamClient:
    url_format = "wss://{}.lusid.com/candela/sessions/prompt"

    def __init__(self, token, domain):
        self.token = token
        self.url = self.url_format.format(domain)
        self.websocket = None
        self.authenticated = False
        self._response_queue = asyncio.Queue()
        self._listening_task = None

    async def connect(self):
        self.websocket = await websockets.connect(self.url)
        self._listening_task = asyncio.create_task(self.listen_for_messages())
        await self.initialise_connection()

    async def close_connection(self):
        self._listening_task.cancel()
        await self.websocket.close()

    async def initialise_connection(self):
        await self.send_message(protocol="json", version=1)

        await self.send_message(
            arguments=[self.token], invocationId="0", target="Authenticate", type=1
        )
        self.authenticated = True

    async def send_message(self, **kwargs):
        if self.websocket is None:
            raise ConnectionError("Candela Stream Client is not connected.")

        message_str = json.dumps(kwargs) + "\x1e"
        await self.websocket.send(message_str)

    async def listen_for_messages(self):
        _response_started = False

        async for message in self.websocket:
            if message.strip() == "":
                raise ValueError("Stream returned an empty message.")

            json_blobs = message.strip().split("\x1e")
            for blob in json_blobs:
                obj = json.loads(blob)
                if "type" not in obj:
                    continue

                if obj["type"] == 6:
                    continue

                if obj["type"] == 3 and not _response_started:
                    _response_started = True
                    continue

                await self._response_queue.put(obj)

                if obj["type"] == 3 and _response_started:
                    return

    async def stream(
        self, prompt: str, session: Session
    ) -> AsyncIterator[TraceEventDefinition]:
        if not self.authenticated:
            raise RuntimeError("Candela Stream Client is not Authenticated.")

        args = [prompt, session.scope, session.code, session.version, "pipeline"]
        await self.send_message(
            arguments=args, invocationId="0", target="Prompt", type=1
        )

        running = True
        while running:
            while not self._response_queue.empty():
                response = await self._response_queue.get()
                yield response
                if response["type"] == 3:
                    running = False
                    break
            await asyncio.sleep(0.1)


def sync_stream_prompt(
    token: str, domain: str, prompt: str, session: Session
) -> Iterator[Event]:
    result_queue = queue.Queue()

    def _run_async_generator():
        async def _async_runner():
            client = CandelaStreamClient(token, domain)
            try:
                await client.connect()
                async for data in client.stream(prompt=prompt, session=session):
                    if data["type"] == 3:
                        result_queue.put(("end_of_stream", None))
                    else:
                        result_queue.put(("data", data))

            except Exception as e:
                result_queue.put(("exception", e))
            finally:
                await client.close_connection()

        asyncio.run(_async_runner())

    thread = threading.Thread(target=_run_async_generator, daemon=True)
    thread.start()

    running = True
    while running:
        while not result_queue.empty():
            type_label, obj = result_queue.get(timeout=30)

            if type_label == "data":
                yield Event.model_validate_json(obj["arguments"][0])
            elif type_label == "end_of_stream":
                running = False
                break
            else:
                raise obj
        sleep(0.1)

    thread.join(timeout=5)
