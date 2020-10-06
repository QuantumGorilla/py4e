#import socket as so
#socket = so.socket(so.AF_INET,so.SOCK_STREAM)
#socket.connect('URL', 80)
#cmd = 'GET {URL} HTTP/1.0\n\n'.encode()
#socket.send(cmd)

#while True:
#    data = socket.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode())
#socket.close()
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()