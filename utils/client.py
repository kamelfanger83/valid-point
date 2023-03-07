import socket
import json
import windows.gamewindow
from threading import Thread

class Client:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

        self.connected = False
        self.listening = False
        self.socket = None

    def startConnection(self):
        if self.connected == False:
            self.socket = socket.socket()

            s = self.socket
            s.connect((self.ip, self.port))

            self.connected = True

    def stopConnection(self):
        if self.connected == True and self.listening == False:
            self.socket.close()
            self.connected = False

    def __listen(self, s):
        while self.listening == True:
            data_encoded = s.recv(102400)
            data_string = data_encoded.decode(encoding="utf-8")
            data = json.loads(data_string)

            print(data)

            if(data["packet"]=="WorldPacket"):
                del data["packet"]
                windows.gamewindow.setGrid(data)

    def startListening(self):
        if self.connected == True:
            self.listening = True
            s = self.socket

            t = Thread(target=self.__listen, args=(s,))
            t.daemon = True
            t.start()

    def stopListening(self):
        if self.listening == True:
            self.listening = False