from socket import *

HOST = 'localhost'
PORT = 10086
ADDR = (HOST, PORT)
BUFSIZE = 1024

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send('%s\r\n' % data)
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data.strip()
    tcpCliSock.close()
