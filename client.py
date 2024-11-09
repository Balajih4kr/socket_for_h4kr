import socket as s
import sys
# Initialize the Socket with ipv4 and TCP connection 

client_server = s.socket(s.AF_INET,s.SOCK_STREAM)


HOST = '127.0.0.1'
PORT = 8087


client_server.connect((HOST,PORT))

while True:
    message = input()
    client_server.sendall(message.encode())
    
    if message.lower() == "exit":
        print(f"Bye {client_server}")
        sys.exit()
    else:
        print(f">>> {message}")

client_server.close()
