from socket import *

HOST = '10.0.10.100'
PORT = 61234
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZE)
    if not data:
        break
    print data
udpCliSock.close()