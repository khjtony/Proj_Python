import socket

def tcpClient():
    dat=1
    clisock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clisock.connect(('localhost', 9527))
    
    #I/O on this clisock
    #clisock.send("")
    while dat:
        dat = clisock.recv(512)
     
    
        print dat
    
if __name__ == "__main__":
    tcpClient()
