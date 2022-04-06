import socket

PORT = 6789
HOST = "192.168.122.107"


class Player:
    def __init__(self, socket, address):
        self.socket = socket
        self.address = address

def RPS(p1,p2):    # Rock Paper Scizors api, returns who win
    if(p1=="rock" and p2=="sciz"
    or p1 == "sciz" and p2=="paper"
    or p1 == "paper" and p2=="rock"):
        return 1
    if(p2=="rock" and p1=="sciz"
    or p2 == "sciz" and p1=="paper"
    or p2 == "paper" and p1=="rock"):
        return 2
    return 0

player1 = ""
player2 = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(5)
print(socket.gethostname())

while True:
    clientSocket, address = s.accept()
    print(f"connection from {address}")
    if player1 == "":
        player1 = Player(clientSocket, address)
        player1.socket.send(bytes("connected", "utf-8"))
    else:
        player2 = Player(clientSocket, address)
        player2.socket.send(bytes("connected", "utf-8"))

        player1.socket.send(bytes("start", "utf-8"))
        print("player1 turn...")
        player2.socket.send(bytes("wait", "utf-8"))
        while True:
            p1Value = player1.socket.recv(16).decode("utf-8")
            player2.socket.send(bytes("start", "utf-8"))
            print("player2 turn...")
            while True:
                p2Value = player2.socket.recv(16).decode("utf-8")
                break
            break
        msg = f"{p1Value} vs {p2Value}"
        player1.socket.send(bytes(msg,"utf-8"))
        player2.socket.send(bytes(msg,"utf-8"))

        winner = RPS(p1Value,p2Value)
        if(winner==1):
            msg1 = "U win"
            msg2 = "U lose"
            print("player 1 wins")
        elif(winner==2):
            msg1 = "U lose"
            msg2 = "U win"
            print("player 2 wins")
        else:
            msg1 = "Draw"
            msg2 = "Draw"
            print("draw")

        player1.socket.send(bytes(msg1,"utf-8"))
        player2.socket.send(bytes(msg2,"utf-8"))

        player1.socket.close()
        player2.socket.close()
        player1 = ""
        player2 = ""
        print("players disconnected!")



