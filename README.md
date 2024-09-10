# Broadcast Server

Broadcast Server is a simple WebSocket-based chat application that allows multiple clients to connect and communicate in real-time. It consists of a server component that handles connections and message broadcasting, and a client component for users to interact with the chat.

## Features

- Real-time message broadcasting to all connected clients
- Support for multiple simultaneous connections
- Simple command-line interface for clients
- Logging of server events and messages

## Requirements

- Python 3.7 or higher
- `websockets` library
- `aioconsole` library (for the client)

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies:

```
pip install websockets aioconsole
```

## Usage

### Starting the Server

1. Navigate to the project directory.
2. Run the server script:

```
python server.py
```

The server will start and listen for connections on `localhost:12345`.

### Connecting Clients

1. In a new terminal window, navigate to the project directory.
2. Run the client script:

```
python chat_client.py
```

3. Enter your name when prompted.
4. Start chatting! Type your messages and press Enter to send.
5. To exit, type 'quit' and press Enter.

## Server Configuration

The server is configured to run on `localhost` (127.0.0.1) and port `12345`. If you need to change these settings, modify the following line in `server.py`:

```python
server = await websockets.serve(server_handler, "localhost", 12345)
```

## Client Configuration

The client is set to connect to `ws://localhost:12345`. If you've changed the server address or port, update the `uri` variable in `chat_client.py`:

```python
uri = "ws://localhost:12345"
```

## Logging

The server logs connection events and received messages. Logs are printed to the console with timestamps.

## Shutting Down

- To stop the server, press Ctrl+C in the terminal where it's running.
- To exit a client, type 'quit' in the chat interface.



## Acknowledgments

- This project uses the `websockets` library for WebSocket communication.
- The client uses `aioconsole` for asynchronous console I/O.