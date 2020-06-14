import socket
##UTILISATION DE BASE
#Nom d'hôte
print ( socket . getfqdn ('www . google .be ')) # Fully Qualified Domain Name
print ( socket . gethostname ()) # Nom d'hôte de la machine
print ( socket . gethostbyname ('www . google .be ')) # Hôte à partir du nom
print ( socket . gethostbyaddr (' 213.186.33.2 ')) # Hôte à partir de l'adresse

#Création d'un socket
s = socket.socket()
print (s. getsockname())
t = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM )
print (t.getsockname())

#Connexion
s.connect(('www.python.org',80))
print (s. getsockname ())

#Binding
s.bind((socket.gethostname(),6000))
print(s.getsockname())

#Fermeture de la connexion
s. close ()

##PROTOCOLES
#Envoi UDP
s = socket . socket ( type = socket . SOCK_DGRAM )
data = " Hello World !". encode ()
sent = s. sendto (data , ('localhost ', 5000) )
if sent == len ( data ):
    print (" Envoi complet ")
#boucle envoi UDP
s = socket . socket ( type = socket . SOCK_DGRAM )
address = ('localhost ', 5000)
message = " Hello World !". encode ()
totalsent = 0
while totalsent < len ( message ):
    sent = s. sendto ( message[ totalsent :], address )
    totalsent += sent

#Réception de données (UDP)
s = socket . socket ( type = socket . SOCK_DGRAM )
s. bind (( socket . gethostname () , 5000) )
data = s. recvfrom (512) . decode ()
print (’Reçu ’, len ( data ), ’octets :’)
print ( data )

##Création d’une classe Chat
import socket
import sys
import threading
class Chat() :
    def __init__ (self , host = socket.gethostname(),port=5000):
        s=socket.socket( type = socket.SOCK_DGRAM)
        s.settimeout(0.5)
        s.bind((host,port))
        self.__s=s
    def _exit(self):
        self.__running = False
        self. __address = None
        self. __s.close()

    def _quit(self):
        self.__address = None

    def _join(self,param):
        tokens = param.split(' ')
        if len(tokens)==2:
            self.__address=(socket.gethostbyaddr(tokens[0])[0],int(tokens[1]))

    def _send(self,param):
        if self.__address is not None :
            message=param.encode()
            totalsent = 0
            while totalsent<len(message):
                sent = self.__s.sendto(message[totalsent:],self.__address)
                totalsent+=sent

    def _receive(self):
        while self.__running:
            try:
                data,address=self.__s.recvfrom(1024)
                print( data.decode())
            except socket.timeout :
                pass

    def run(self):
        handlers={
            '/exit': self._exit,
            '/quit': self._quit,
            '/join': self._join,
            '/send': self._send
        }
        self.__running = True
        self.__address = None
        threading.Thread(target=self._receive).start()
        while self.__running :
            line = sys.stdin.readline().rstrip()+' '
            command=line[:line.index(' ')]
            param=line[line.index(' ')+1:].rstrip()
            if command in handlers :
                handlers[command]()if param==''else handlers[command](param)
            else :
                print('Unknown command :',command)

port = int(sys.argv[1])
Chat(port=port).run()

##Protocole Serveur/Client TCP
#Serveur ecoute
s = socket . socket ()
s. bind (( socket . gethostname () , 6000) )
s. listen ()
client , addr = s. accept ()

#Creation Client
s = socket . socket ()
s. connect (( socket . gethostname () , 6000) )
#+envoi de donnée 
s = socket . socket ()
s. connect (( socket . gethostname () , 6000) )
s = socket . socket ()
s. connect (( ’www . google .be ’, 80) )
data = " Hello World !". encode ()
sent = s. send ( data )
if sent == len ( data ):
    print (" Envoi complet ")
#+Boucle d’envoi (TCP)
s = socket . socket ()
s. connect (( ’www . google .be ’, 80) )
msg = " Hello World !". encode ()
totalsent = 0
while totalsent < len ( msg ):
    sent = s. send ( msg [ totalsent :])
    totalsent += sent
#Reception de donnnées(TCP)
s = socket . socket ()
s. connect (( ’www . google .be ’, 80) )
s. send (b’GET / HTTP /1.0\ n\n’)
data = s. recv (512) . decode ()
print (’Reçu ’, len ( data ), ’octets :’)
print ( data )
#Boucle de réception (TCP)
s = socket . socket ()
s. connect (( ’www . google .be ’, 80) )
s. send (b’GET / HTTP /1.0\ n\n’)
chunks = []
finished = False
while not finished :
    data = client . recv (1024)
    chunks . append ( data )
    finished = data == b’’
print (b’’. join ( chunks ). decode ())

#Serveur Echo 