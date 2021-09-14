# Importation des librairies 
import socket
import 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("google.fr",80))
command = 'GET / HTTP/1.1\r\n'
command+= 'Host: www.google.fr\r\n'
command+= 'Connection: Close\r\n\r\n'

# envoi puis reception de la reponse

request = bytes(command, 'utf-8')
s.send(request)
data = s.recv(15)
print(data.decode('utf-8')) 