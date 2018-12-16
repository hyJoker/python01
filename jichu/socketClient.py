import socket
import sys

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

socketClient.connect((host, port))
msg = socketClient.recv(1024)

socketClient.close()
print(msg.decode('utf-8'))
