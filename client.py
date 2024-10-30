import deslib
import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            # Receive and decrypt message
            encrypted_message = client_socket.recv(1024)
            print('New message!')
            secret_key = input("Secret key: ")
            message = deslib.decrypt(encrypted_message, deslib.make_rk(secret_key))
            print(f'Received: {deslib.hex2text(deslib.bin2hex(message))}')
        except:
            print("Error! Disconnected from the server.")
            client_socket.close()
            break

def send_messages():
    while True:
        message = input("You: ")
        secret_key = input("Secret key: ")
        encrypted_message = deslib.encrypt(message, deslib.make_rk(secret_key))
        client_socket.send(encrypted_message)

# Start threads for receiving and sending messages
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()