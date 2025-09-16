import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define host and port
host = 'localhost'
port = 12345

server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server is listening on {host}:{port}...")

#accept a client connection
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

#receive data from the client
data = conn.recv(1024).decode('utf-8')
print(f"Received from client: {data}")

#send acknowledgement to the client
ack_message = "Message received"
conn.sendall(ack_message.encode())

#close the connection
conn.close()