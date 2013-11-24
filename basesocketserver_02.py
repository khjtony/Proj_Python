import socket
def tcpServer():
    srvsock = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    srvsock.bind(('localhost', 9527))
    srvsock.listen(5)

    while True:
        clisock, (remoteHost, remotePort) = srvsock.accept()
        print "[%s:%s] connected" % (remoteHost, remotePort)
        #do something on the clisock
        clisock.send('This msg was send from server')
        fpr=open('story.txt','r')
        for line in fpr.readlines():
            clisock.send(line)
        clisock.close()
        fpr.close()

if __name__ == "__main__":
    tcpServer()
