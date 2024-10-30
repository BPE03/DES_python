import socket
import threading
import deslib

HOST = '127.0.0.1'
PORT = 65432

secret_key = '1234567890ABCDEF'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f'Server listening on {HOST}:{PORT}')

clients = []

def handle_client(client_socket):
    while True:
        try:
            # Receive and decrypt message
            encrypted_message = client_socket.recv(1024).decode('latin-1')
            cipher_message = deslib.bin2text(encrypted_message)
            print(f'New message! {cipher_message}')
            message = deslib.decrypt(cipher_message, deslib.make_rk(secret_key))
            print(f'Received: {message}')
            broadcast(encrypted_message, client_socket)
            print('Broadcasted message')
        except:
            clients.remove(client_socket)
            client_socket.close()
            break

def broadcast(encrypted_message, client_socket):
    for client in clients:
        if client != client_socket:
            client.send(encrypted_message.encode('latin-1'))

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Connected to {client_address}')
    clients.append(client_socket)
    threading.Thread(target=handle_client, args=(client_socket,)).start()