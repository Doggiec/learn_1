from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 10086
ADDR = (HOST, PORT)


class ServerRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))


tcpServ = TCP(ADDR, ServerRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
