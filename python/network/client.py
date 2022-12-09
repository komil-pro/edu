import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
message = input('Please enter your message:')
clientsocket.send(message.encode())