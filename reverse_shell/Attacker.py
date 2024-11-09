import socket
import sys

HOST = '127.0.0.1' 
PORT = 4450


client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_server.connect((HOST, PORT))

try:
    while True:
        
        command = input("Shell >>> ")

        
        if command.lower() == "exit":
            print(f"Bye {client_server}")
            client_server.send(command.encode())
            break

        
        client_server.send(command.encode())

        
        data = client_server.recv(4096).decode()
        print(data)  

except KeyboardInterrupt:
    print("\nDisconnected from server.")
finally:
    client_server.close()
    sys.exit()
