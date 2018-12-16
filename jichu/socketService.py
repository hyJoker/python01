import socket
import sys

# 创建socket对象
socketService = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取本地主机名
host = socket.gethostname()
port = 9999

socketService.bind((host, port))
socketService.listen(5)

while True:
    clientsocket, addr = socketService.accept()
    print('连接地址:%s' % str(addr))

    msg = '欢迎你!!!'
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
