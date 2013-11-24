import socket
s=socket.socket()
host=socket.gethostname()
port=2545

s.connect((host,port))
print(s.recv(1024))
