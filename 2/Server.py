import socket 
import threading 
import datetime
from telnetlib import NOP 
import random
import os

host = '129.217.162.84'
port = 25000

#socket anlegen
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()
Clientliste = []
Benutzer ={}
cwd = os.path.dirname(os.path.abspath(__file__))
loc = os.path.join(cwd, 'chat_history.txt') 

def get_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"#{r:02x}{g:02x}{b:02x}"

def send_to_all(msg_str):
    for client_conn in Clientliste:
        client_conn.sendall(msg_str.encode())

# Funktion zum Anhängen einer Nachricht an die Chat-Historie-Datei
def append_to_chat_history(message):
    with open(loc, "a") as text_file:
        text_file.write(f"{message}\n")

# Funktion zum Laden der Chat-Historie aus der Datei
def load_chat_history():
    chat_history = []
    with open(loc, "r") as file:
        for line in file:
            chat_history.append(line + '<br>')
    print(chat_history)
    return chat_history


# Funktion für Client Thread
def client_thread(conn, addr):

        conn.send(b"\n Welcome to the Server.\n")

        Nickname = conn.recv(4096).decode()
        color = get_color()
        Benutzer[Nickname]={"Socket": conn, "Color": color, "AllowPrivateMessages": True}
        time = datetime.datetime.now()
        
        welcome_msg = '\n'+time.strftime("(%H:%M:%S): ") + Nickname + ' just joined the chat' + '\n'

        send_to_all(welcome_msg)

        # Load chat history from file
        chat_history = load_chat_history()

        # Send chat history to the client
        for message in chat_history:
            conn.sendall(message.encode())
        try:
            while True:
            
                Nachricht2 = conn.recv(4096)
                Nachricht2 = Nachricht2.decode()
                #print (Nachricht2)
                user_data = Benutzer.get(Nickname)
                color = user_data["Color"]
                #print (color)
                if Nachricht2.startswith("!§%&/()=€"):
                    if user_data['AllowPrivateMessages']:
                        Benutzer[Nickname] ['AllowPrivateMessages'] = False
                        conn.send(b"Der entsprechende Nutzer empfaengt nun keine Private Nachrichten mehr.\n")
                    else:
                        Benutzer[Nickname] ['AllowPrivateMessages'] = True
                        conn.send(b"Der entsprechende Nutzer erhaelt nun wieder Private Nachrichten.\n")
                elif Nachricht2.startswith("@"):
                    sentonickname = Nachricht2[1:Nachricht2.find('|')]
                    print (sentonickname)
                    if sentonickname in Benutzer:
                        client_data = Benutzer.get(sentonickname)
                        client_socket= client_data['Socket']
                        print(client_data)
                        if client_data['AllowPrivateMessages']:
                            Nachricht = Nachricht2[Nachricht2.find('|')+1:]
                            Zeit = datetime.datetime.now()
                            Zeit = Zeit.strftime('%H:%M:%S')
                            msg_with_color =   f"<span style='color:{color}'>Privat: ({Zeit}): {Nickname}: {Nachricht}</span>"
                            print (msg_with_color)
                            client_socket.sendall(msg_with_color.encode())
                            conn.send(msg_with_color.encode())
                        else:
                            conn.send(b"Der entsprechende Nutzer moechte keine Privaten Nachrichten erhalten.\n")
                    else:
                        conn.send(b"Der entsprechende Nutzer befindet sich nicht auf dem Server.\n")        
                else:
                    Zeit = datetime.datetime.now()
                    Zeit = Zeit.strftime('%H:%M:%S')
                    msg_with_color =   f"<span style='color:{color}'>({Zeit}): {Nickname}: {Nachricht2}</span>" 
                    print (msg_with_color)
                    append_to_chat_history(msg_with_color)
                    send_to_all(msg_with_color)
                    # Weiterleitung der Nachricht an alle anderen clients 
        except ConnectionResetError:
            print(f'Verbindung verloren {conn}')
            remove_user(Nickname)
            conn.close()


# Funktion zum Weiterleiten der Nachrichten an alle Clients
def send_to_all(msg_str):
    for client_conn in Clientliste:
        try:
            client_conn.fileno()  # Überprüfen, ob die Verbindung noch aktiv ist
            client_conn.sendall(msg_str.encode())
        except (OSError, ConnectionResetError):
            pass
    
    # Clientliste durchlaufen und msg_str senden

def remove_user(nickname):
    if nickname in Benutzer:
        del Benutzer[nickname]
        print(f"{nickname} wurde entfernt")
        send_to_all(f"{nickname} hat den Chat verlassen\n")
    else:
        print(f"{nickname} nicht gefunden")
    







while True: 
    print('bereit für neue verbindung:')
    conn, addr = server_socket.accept()
    Clientliste.append(conn)


    # Client Liste erweitern
    ...
    threading.Thread(target = client_thread ,args = (conn, addr)).start()
    # Starten des Client Threads
    ...
