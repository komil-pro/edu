import socket

HOST = "localhost"  # Standard loopback interface address (localhost)
PORT = 8899  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data:
                f = open("server_log.txt", "a")
                f.write(data.decode('utf-8'))
                f.close()
            #conn.sendall(data)
            