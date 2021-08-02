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