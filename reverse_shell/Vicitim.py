import socket
import subprocess as sub

HOST = '127.0.0.1'
PORT = 4448

# Set up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("[+] Server started and listening for connections...")


client_socket, client_addr = server_socket.accept()
print(f"[+] New client {client_addr} connected.")

try:
    while True:
        command = client_socket.recv(1024).decode()

        
        if command.lower() == "exit":
            print("[-] Client requested exit.")
            break

        
        result = sub.run(command, capture_output=True, shell=True, text=True)

        
        if result.stdout:
            client_socket.send(result.stdout.encode())
        elif result.stderr:
            client_socket.send(result.stderr.encode())
        else:
            client_socket.send("Command executed with no output.".encode())

except KeyboardInterrupt:
    print("\nServer shutting down.")
finally:
    client_socket.close()
    server_socket.close()
