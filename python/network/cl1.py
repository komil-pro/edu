import socket

HOST = "localhost"  # The server's hostname or IP address
PORT = 8899  # The port used by the server

msg = input('Please enter your message:')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg.encode())
    #data = s.recv(1024)

#print(f"Received {data!r}")