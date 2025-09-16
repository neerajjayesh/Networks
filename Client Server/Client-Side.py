import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define host and port
host = 'localhost'
port = 12345

#connect to the server
client_socket.connect((host, port))

#send data to the server
message = "Hello"
client_socket.sendall(message.encode())

#receive acknowledgement from the server
ack_message = client_socket.recv(1024).decode()
print(f"Received from server: {ack_message}")

#close the connection
client_socket.close()