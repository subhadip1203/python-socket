import threading
import socket

host = '127.0.0.1' # localhost
port = 8090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM_)
server.bind(host,port)
server.listen()

clients =[]
nick_names=[]


def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nickname= nick_names[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nick_names.remove(nickname)
            break
def receive():
    while True:
        client,address = server.accept
        print(f'connected client is {address}')
        client.send("Nickname".encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        clients.append(client)
