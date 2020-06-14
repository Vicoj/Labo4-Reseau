import socket

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind((socket.gethostname(),5000))
data=s.recvfrom(512)[0].decode()

print('Reçu',len(data),'octets :')
print(data)