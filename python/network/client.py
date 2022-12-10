import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
message = input('Please enter your message:')
while len(message)>0:
    clientsocket.send(message.encode())