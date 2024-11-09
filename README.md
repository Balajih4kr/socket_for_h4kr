# socket_for_h4kr

<h4 align="center">A chat server that accept multiple client and make them communication </h4>

#### command in linux 
    - python3 server.py
    - python3 client.py 
    
#### command in linux 
    - python server.py
    - python client.py

# Python Socket Client Application

# Multi-Client Server in Python

This Python application is a simple multi-client server that accepts multiple client connections over TCP using the `socket` library. It listens on a specified IP and port, allowing clients to send messages to the server, which are then displayed on the server’s console.

## Features

- Accepts multiple client connections.
- Uses `select` for non-blocking I/O to handle multiple clients without threads.
- Displays incoming messages from clients.
- Detects client disconnection.

## Prerequisites

- Python 3.x

## How to Run

1. **Start the Server:**
   ```bash
   python server.py





This is a Python script for a socket-based client application that connects to a server via TCP/IP, allowing bidirectional communication. It uses IPv4 and establishes a TCP connection to a specified host and port.

## Features

- Connects to a server at a specified IP address and port.
- Sends user-input messages to the server.
- Terminates the connection when the user enters "exit".

## Requirements

- Python 3.x

## Usage

1. Ensure you have a server running and listening on the specified IP address and port (`127.0.0.1:8087` in this case).
2. Run the client script, which will connect to the server and allow you to send messages.

### Installation

1. Clone this repository or copy the code to your local machine.
2. Open a terminal and navigate to the directory containing the script.

### Running the Client

1. Start the client by executing the following command:
   ```bash
   python client.py


