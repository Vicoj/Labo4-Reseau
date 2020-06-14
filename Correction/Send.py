import socket
s = socket.socket(type=socket.SOCK_DGRAM)
address = ('localhost', 5000)
message = " Hello World !".encode ()

totalsent = 0
while totalsent < len (message):
    sent=s.sendto(message[totalsent:],address)
    totalsent+=sent