import socket
import json
from threading import Thread

class Server:
    def __init__(self, grid, port, players, entities):
        self.grid = grid
        self.players = players
        self.entities = entities

        self.online = False
        self.listening = False

        hostname = socket.gethostname()
        ip = socket.gethostbyname(socket.gethostname())

        self.ip = ip
        self.port = port
        self.socket = None
        self.clients = set()

    def startServer(self):
        if self.online == False:
            self.online = True

            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.ip, self.port))

            self.socket = s

    def stopServer(self):
        if self.listening == False:
            self.socket.close()

    def __handleClient(self, client):
        while self.listening:
            try:
                msg = client.recv(102400).decode()
            except Exception as e:
                print(f"[!] Player Leave: {e}")
                self.clients.remove(client)
            else:
                print(msg)

    def __listen(self, s):
        while self.listening == True:
            client_socket, client_address = s.accept()
            print(f"[+] Der Spieler mit der IP {client_address} hat das Spiel betreten.")

            self.clients.add(client_socket)
            self.grid.packet = "WorldPacket"

            packet = json.dumps(vars(self.grid))
            client_socket.send(packet.encode(encoding="utf-8"))

            t = Thread(target=self.__handleClient, args=(client_socket,))
            t.daemon = True
            t.start()

    def startListening(self):
        if self.online == True:
            s = self.socket
            s.listen(5)

            self.listening = True

            t = Thread(target=self.__listen, args=(s,))
            t.daemon = True
            t.start()

    def stopListening(self):
        if self.listening == True:
            for client in self.clients:
                client.close()

            self.clients = set()
            self.listening = False

    def getIP(self):
        return self.ip