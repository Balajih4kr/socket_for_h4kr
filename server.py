import socket as s
import sys
import select as sel

HOST = '127.0.0.1'
PORT = 8087

SOCLIST = []

server_socket = s.socket(s.AF_INET,s.SOCK_STREAM)

server_socket.bind((HOST,PORT))
server_socket.listen(5)

SOCLIST.append(server_socket)

print("[+] Server started ....")
while True:
    

    ready_read,ready_write,error = sel.select(SOCLIST,[],[],0)

    for sock in ready_read:
        if sock == server_socket:
            client_socket,client_addr = server_socket.accept()
            SOCLIST.append(client_socket)
            print(f"New Client {client_addr} Connected")


        else:
            data = sock.recv(1028).decode()
            if data:    
                print(f">>> {data}")
            else:
                print("Client Disconnected")
                sys.exit()
                
    
server_socket.close()

client_socket.close()

