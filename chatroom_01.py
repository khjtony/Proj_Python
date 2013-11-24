# Filename: ChatRoomServer.py

#This is a simple chatroom program based on socket protocol.

import threading
import datetime
import socket

# a simple log function
def log(lg):
    print(lg)

# Chat room server listen thread class, this class is use for listening client login
# when a client request to connect server, this class will start a connect thread
class ServerListenThread(threading.Thread):                                     #This is ServerListenThread class. This class is used to listen income connection request
    def __init__(self, hostname, port, accept):                                   #initiation method/construct method	          
        threading.Thread.__init__(self)
        self.hostname = hostname
        self.port = port
        self.accept = accept
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((hostname, port))
        self.sock.listen(0)
        log('ServerIp:%s ServerPort:%s  waiting for client...'%self.sock.getsockname())
    def run(self):  #kiss my ass babe
        clientid = 1
        while True:
            client, cltadd = self.sock.accept()
            log('a request from Id=%s%s'%('%d Address:'%clientid , cltadd))
            if self.accept(clientid, client):
                clientid = clientid + 1

# Connect thread class, this class is use for connecting with client and receiving client's message
class ServerConnectThread(threading.Thread):
    def __init__(self, clientid, client, encoding, receive, disconnect):
        threading.Thread.__init__(self)
        self.client = client
        self.clientid = clientid
        self.encoding = encoding
        self.receive = receive
        self.disconnect = disconnect
        self.clientname = None
        self.inputs = self.client.makefile('rb', 0)
        self.outputs = self.client.makefile('wb', 0)
    
    def run(self):
        self.sendstring('Input your name:')
        while True:
            string = self.readline()
            if string:
                string = string.lstrip()
                if len(string)>0:
                    self.receive(self, string)
            else:
                self.inputs.close()
                self.outputs.close()
                break
        if self.clientname:
            self.disconnect(self)
    def sendstring(self, string):
        self.sendbytes(bytes(string, self.encoding))
    def sendbytes(self, bts):
        self.outputs.write(bts)
    def readline(self):
        rec = self.inputs.readline()
        if rec:
            string = bytes.decode(rec, self.encoding)
            if len(string)>2:
                string = string[0:-2]
            else:
                string = ' '
        else:
            string = False
        return string


# Chat room server class, this class is constitute of a listen thread and many connect thread
class ChatRoomServer:
    def __init__(self, ip='0.0.0.0', port=9113, encoding='utf-8'):
        self.hostname = ip
        self.encoding = encoding
        self.port = port
        self.clients = {}
        self.clientnames = {}
    def whenconnect(self, clientid, client):
        log('a connect with Id=%s%s'%('%d Address:'%clientid , client.getpeername()))
        connect = ServerConnectThread(clientid, client, self.encoding, self.whenreceive, self.whenexit) 
        connect.start()
        return True

    def whenreceive(self, client, string):
        log('frome %d, receive:%s (%d)'%(client.clientid, string, len(string)))
        if client.clientname:
            if string[0]=='.':
                self.handlecmd(client, string[1:])
            else:
                now = datetime.datetime.now()
                sendstring = '%s %s\r\n  %s\r\n'%(now, client.clientname, string)
                self.sendtoall(sendstring, client)
        else:
            if self.clientnames.__contains__(string):
                client.sendstring('%s is exited!!!\r\n'%string)
            else:
                client.clientname = string
                client.sendstring('Hell, %s!!!\r\n'%client.clientname)
                self.addclient(client)
        return True

    def whenexit(self, client):
        self.delclient(client)
        return True
    
    def handlecmd(self, client, cmd):
        log('cmd: %s'%cmd)
        if cmd=='user':
            client.sendstring('User list(%d):\r\n'%len(self.clients))
            for i in self.clients:
                clt = self.clients[i]
                client.sendstring(' %d\t%s\r\n'%(clt.clientid, clt.clientname))
        else:
            client.sendstring('Unknow command: %s:\r\n'%cmd)
    
    def start(self):
        serverlisten = ServerListenThread(self.hostname, self.port, self.whenconnect)
        serverlisten.start()
    
    def sendtoall(self, string, notfor):
        sends = bytes(string, self.encoding)
        for i in self.clients:
            if not(notfor and notfor.clientid==i):
                self.clients[i].sendbytes(sends)
    
    def addclient(self, client):
        self.sendtoall('%s logined!!!\r\n'%client.clientname, client)
        self.clients[client.clientid] = client
        self.clientnames[client.clientname] = client.clientid

    def delclient(self, client):
        self.sendtoall('%s logouted!!!\r\n'%client.clientname, client)
        del self.clients[client.clientid]
        del self.clientnames[client.clientname]

# start a chat room server
ChatRoomServer().start()

