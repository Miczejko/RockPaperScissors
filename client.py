import socket

PORT = 6789
HOST = "192.168.122.107"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:
    if(s.recv(16).decode("utf-8") == "connected"):
        print("connected succesfully")
        while True:
            msg = s.recv(16).decode("utf-8")
            print("starting game ...")
            break
        if(msg == "wait"):
            print("wait for ur turn!")
            while True:
                msg = s.recv(16).decode("utf-8")
                break
        if(msg == "start"):
            print("Ur Turn")
            input = input("rock|paper|sciz ???")
            s.send(bytes(input,"utf-8"))
        while True:
            msg = s.recv(24).decode("utf-8")
            print(msg)
            while True:
                msg = s.recv(16).decode("utf-8")
                print(msg)
                break
            break
        break
    break

# while True:
#     full_msg = ''
#     new_msg = True
#     while True:
#         msg = s.recv(16)
#         if new_msg:
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False
#
#         full_msg += msg.decode("utf-8")
#
#         if len(full_msg) - HEADERSIZE == msglen:
#             print("full msg recvd")
#             print(full_msg[HEADERSIZE:])
#             new_msg = True
#             full_msg = ""

