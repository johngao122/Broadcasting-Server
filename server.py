import asyncio
import websockets
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


CLIENTS = {}

async def server_handler(websocket, path):

    name = await websocket.recv()
    CLIENTS[websocket] = name
    logging.info(f"{name} connected")

    try:
        async for message in websocket:
            logging.info(f"Received message from {name}: {message}")
            broadcast_message = f"{name}: {message}"
            await asyncio.wait([client.send(broadcast_message) for client in CLIENTS if client.open])
    except websockets.exceptions.ConnectionClosed:
        logging.info(f"{name} connection closed")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        del CLIENTS[websocket]
        logging.info(f"{name} disconnected")

async def shutdown(server):
    logging.info("Shutting down server...")
    server.close()
    await server.wait_closed()
    logging.info("Server shut down cleanly")

async def main():
    server = await websockets.serve(server_handler, "localhost", 12345)
    logging.info(f"Server started at {server.sockets[0].getsockname()}")

    try:
        await asyncio.Future()
    except asyncio.CancelledError:
        pass
    finally:
        await shutdown(server)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("\nReceived exit signal, shutting down...")
