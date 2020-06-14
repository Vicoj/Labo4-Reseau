import socket
#print(socket.gethostbyaddr('172.17.0.99'))

s = socket.socket()
s.connect(('www.google.com',80))
#print(s.getsockname())

s.bind((socket.gethostname(),6000))

s=socket.socket(type=socket.SOCK_DGRAM)
data="Hello World!".encode()
sent=s.sendto(data,('localhost',5000))
if sent==len(data):
    print("Envoi complet")
