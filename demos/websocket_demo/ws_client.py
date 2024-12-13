# coding: utf-8
"""
    :date: 2023-12-29
    :author: linshukai
    :description: Websockets client
"""

from websockets.client import connect
from socket import socket, AF_INET, SOCK_STREAM
import aioconsole
import asyncio


async def receive_messages(websocket):
    while True:
        msg = await websocket.recv()
        print("Received Msg: ", str(msg))


async def send_messages(websocket):
    while True:
        msg = await aioconsole.ainput("you:\n")
        await websocket.send(msg.encode("utf-8"))


async def main():
    async with connect("ws://127.0.0.1:80") as ws:
        await asyncio.gather(receive_messages(ws), send_messages(ws))


if __name__ == "__main__":
    asyncio.run(main())
