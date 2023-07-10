import socket 
import threading
# socket anlegen
host = '129.217.162.164'
port = 25000



client_socket = socket.socket()
client_socket.connect((host, port))

# Empfangen und Ausgabe der ersten Nachrichten des Servers (Willkommen, Beitrittsinfo)
Nachricht = client_socket.recv(4096)
print('Servernachricht:' +str(Nachricht.decode()))

def receive_thread_def(client_socket):
    while True: 
        server_msg = client_socket.recv(4096)
        print('Servernachricht:', server_msg.decode())
        


threading.Thread(target = receive_thread_def ,args = (client_socket,)).start()


while True: 
    

    # Eingabe von Nachrichten mithilfe von input()
    msg = input('Deine Eingabe :')
    

    # Senden der eingegebenen Daten an den Server
    client_socket.send(msg.encode())
    ...
