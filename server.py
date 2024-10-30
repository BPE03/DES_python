import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}')

clients = []

def handle_client(client_socket):
    while True:
        try:
            # Receive and decrypt message
            encrypted_message = client_socket.recv(1024)
            print('Received message')
            # message = custom_des.decrypt(encrypted_message.decode(), SECRET_KEY)
            # print(f'Received: {message}')
            broadcast(encrypted_message, client_socket)
            print('Broadcasted message')
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(encrypted_message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(encrypted_message)

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Connected to {client_address}')
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()