from MeinDesignAlsPythonDatei import Ui_Dialog
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import socket
import threading
from os import system
import datetime
import os
from PyQt5 import QtWidgets, QtCore  # Erforderliche QT Bibliotheken werden importiert!
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QCoreApplication

# GraphicalUserInterface erbt von dem Designer Ergebnis und von einer QT Klasse
class GraphicalUserInterface(QtWidgets.QMainWindow, Ui_Dialog): 

    def __init__(self, parent = None):

        super(GraphicalUserInterface, self).__init__(parent)                      # Ausführen der __init__ der Elternklasse
        self.setupUi(self)                                              # Initialisierung des User Interface
        self.client_socket = socket.socket()

        # Signals and Slots der einzelnen Elemente verbinden (Ein guter Anfang sind eine Sendebox und eine Anzeige für das Chatprotokoll)
        self.LogIn.clicked.connect(self.on_connectButtonClicked)
        self.SendenGruppenmsg.clicked.connect(self.on_sendButtonClicked)
        self.SendenPrivatmsg.clicked.connect(self.on_sendToButtonClicked)
        self.Beenden.clicked.connect(self.on_exitButtonClicked)
        #self.Message_lineEdit.returnPressed.connect(self.on_sendButtonClicked)
        self.Gruppenchat.returnPressed.connect(self.on_sendButtonClicked)
        self.PNaktideakti.clicked.connect(self.on_PNaktideaktiClicked)
        
    def on_connectButtonClicked(self):
        """
        Diese Funktion wird aufgerufen, sobald der Verbindenknopf gedrückt wird.

        """

        # Verbidnung mit dem Server aufbauen (Auslesen der Eingaben der Informationen über host und port)
        try:
            host = self.IPAdresse.text()
            port = int(self.Port.text())
            self.client_socket.connect((host, int(port)))
            nickname = self.Nutzername.text()
            threading.Thread(target = self._receiving_thread).start()
            self.client_socket.send(nickname.encode())
        except Exception as e: 
            print(e)
            color = '#FF0000'
            line = "\n Ein Fehler ist aufgetreten \n"
            self.Display.append(f"<span style='color:{color}'>{line}</span><br>")

        #Starten eines neuen Threads für den kontinuierlichen Empfang von Signalen. 

        


    def on_sendButtonClicked(self):
        """
        Diese Funktion wird aufgerufen, sobald der Sendeknopf gedrückt wird.

        """
        # Einlesen, der z.B. im TextBrowser Objekt eingegebenen Nachricht
        msg = self.Gruppenchat.text()
        #print(msg)

        #Senden der eingegebenen Daten an den Server
        self.client_socket.send(msg.encode())
        self.Gruppenchat.clear()

    def on_sendToButtonClicked(self):
        msg = "@" + self.Anderernutzer.text() + "|" + self.Privatnachricht.text()
        self.client_socket.send(msg.encode())
        self.Anderernutzer.clear()
        self.Privatnachricht.clear()

    def on_PNaktideaktiClicked(self):
        msg = "!§%&/()=€"
        self.client_socket.send(msg.encode())

    def _receiving_thread(self):
        # Laden des Chatverlaufs aus der Textdatei
        
            

        print('Receiving started')
        self.Display.ensureCursorVisible()
        while True:
            server_msg = self.client_socket.recv(4096)
            message = server_msg.decode()
            
            #print(message)
            try:
                if message.startswith("<span") or message.startswith("<br>") and message.endswith("</span>") or message.endswith("<br>"):
                    start_index = message.find(">", 4,-1)
                    end_index = message.rfind("<")
                    formatted_text = message[start_index + 1 : end_index]

                    style_start_index = message.find("color:")
                    style_end_index = message.find("'", style_start_index)
                    color = message[style_start_index + 6 : style_end_index]
                
                    if type (formatted_text) is list:
                        print ('formatted text is list')
                        for line in formatted_text:
                            self.Display.append(f"<span style='color:{color}'>{line}</span><br>")
                    else:
                        self.Display.append(f"<span style='color:{color}'>{formatted_text}</span>")
                        print ('formatted text is not list')
                        print ("das ist im ersten else: " + formatted_text)
                elif type (message) is list:
                    print('Liste detektiert')
                else:
                    self.Display.append(message)
                    print ("das ist im else: " + message)
                    print('datentyptype' , type (message))
            except:
                self.Display.append("Der Chatlog konnte nicht geladen werden.")
    def on_exitButtonClicked(self):
        # Code für den Disconnect vom Server
        
        self.disconnect()
        # Beenden des Programms
        QtWidgets.QApplication.quit()
        QCoreApplication.instance().quit()     

    def closeEvent(self, event):
        """
        Diese Methode wird aufgerufen, wenn das Fenster geschlossen wird.
        """
        self.on_exitButtonClicked()  # Methode zum Beenden des Programms aufrufen
        event.accept()  # Das Schließen des Fensters erlauben
    
    def disconnect(self):
        self.connected = False
        if self.client_socket and self.client_socket.fileno() != -1:  # Überprüfe, ob der Socket geöffnet ist
            self.client_socket.close()



# main Funktion
def main():
    app = QtWidgets.QApplication(sys.argv)

     

    form = GraphicalUserInterface()
    form.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()
