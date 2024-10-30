import deslib
import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

secret_key = '1234567890ABCDEF'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            # Receive and decrypt message
            encrypted_message = client_socket.recv(1024).decode('latin-1')
            encrypted_message = deslib.bin2text(encrypted_message)
            print('New message!')
          #  secret_key = input("Secret key: ")
            message = deslib.decrypt(encrypted_message, deslib.make_rk(secret_key))
            print('Received: ' + message)
        except:
            print("Error! Disconnected from the server.")
            client_socket.close()
            return

def send_messages():
    while True:
        message = input("You: ")
      #  secret_key = input("Secret key: ")
        encrypted_message = deslib.encrypt(message, deslib.make_rk(secret_key))
        client_socket.send(encrypted_message.encode('latin-1'))

# Start threads for receiving and sending messages
threading.Thread(target=receive_messages).start()
threading.Thread(target=send_messages).start()