import asyncio
import websockets
import aioconsole  

async def listen_for_messages(websocket):
    while True:
        try:
            response = await websocket.recv()

            
            print(f"\n{response}")
            
            print("Enter message to send (type 'quit' to exit): ", end="", flush=True)
        except websockets.exceptions.ConnectionClosed:
            print("Server connection closed")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

async def send_message(websocket):
    while True:
        message = await aioconsole.ainput("Enter message to send (type 'quit' to exit): ")
        if message.lower() == 'quit':
            break
        await websocket.send(message)

async def client():
    uri = "ws://localhost:12345"
    async with websockets.connect(uri) as websocket:
        
        name = await aioconsole.ainput("Enter your name: ")
        await websocket.send(name)  

        print(f"Connected to the server as {name}.")

        
        await asyncio.gather(
            listen_for_messages(websocket),
            send_message(websocket)
        )

asyncio.run(client())
