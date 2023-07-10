# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MeinDesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1123, 890)
        self.SendenGruppenmsg = QtWidgets.QPushButton(Dialog)
        self.SendenGruppenmsg.setGeometry(QtCore.QRect(620, 770, 75, 23))
        self.SendenGruppenmsg.setObjectName("SendenGruppenmsg")
        self.Gruppenchat = QtWidgets.QLineEdit(Dialog)
        self.Gruppenchat.setGeometry(QtCore.QRect(230, 770, 331, 21))
        self.Gruppenchat.setObjectName("Gruppenchat")
        self.IPAdresse = QtWidgets.QLineEdit(Dialog)
        self.IPAdresse.setGeometry(QtCore.QRect(230, 100, 113, 20))
        self.IPAdresse.setObjectName("IPAdresse")
        self.Port = QtWidgets.QLineEdit(Dialog)
        self.Port.setGeometry(QtCore.QRect(370, 100, 113, 20))
        self.Port.setObjectName("Port")
        self.Display = QtWidgets.QTextBrowser(Dialog)
        self.Display.setGeometry(QtCore.QRect(230, 130, 611, 611))
        self.Display.setObjectName("Display")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 80, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(410, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.LogIn = QtWidgets.QPushButton(Dialog)
        self.LogIn.setGeometry(QtCore.QRect(510, 100, 75, 23))
        self.LogIn.setObjectName("LogIn")
        self.Beenden = QtWidgets.QPushButton(Dialog)
        self.Beenden.setGeometry(QtCore.QRect(620, 100, 75, 23))
        self.Beenden.setObjectName("Beenden")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 750, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(230, 800, 161, 16))
        self.label_4.setObjectName("label_4")
        self.Anderernutzer = QtWidgets.QLineEdit(Dialog)
        self.Anderernutzer.setGeometry(QtCore.QRect(250, 820, 71, 20))
        self.Anderernutzer.setText("")
        self.Anderernutzer.setObjectName("Anderernutzer")
        self.Privatnachricht = QtWidgets.QLineEdit(Dialog)
        self.Privatnachricht.setGeometry(QtCore.QRect(330, 820, 251, 20))
        self.Privatnachricht.setObjectName("Privatnachricht")
        self.SendenPrivatmsg = QtWidgets.QPushButton(Dialog)
        self.SendenPrivatmsg.setGeometry(QtCore.QRect(620, 820, 75, 23))
        self.SendenPrivatmsg.setObjectName("SendenPrivatmsg")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 820, 21, 16))
        self.label_5.setObjectName("label_5")
        self.Nutzername = QtWidgets.QLineEdit(Dialog)
        self.Nutzername.setGeometry(QtCore.QRect(730, 100, 113, 20))
        self.Nutzername.setObjectName("Nutzername")
        self.PNaktideakti = QtWidgets.QPushButton(Dialog)
        self.PNaktideakti.setGeometry(QtCore.QRect(330, 850, 251, 23))
        self.PNaktideakti.setObjectName("PNaktideakti")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SendenGruppenmsg.setText(_translate("Dialog", "Senden"))
        self.label.setText(_translate("Dialog", "IP-Adresse"))
        self.label_2.setText(_translate("Dialog", "Port"))
        self.LogIn.setText(_translate("Dialog", "Log In"))
        self.Beenden.setText(_translate("Dialog", "Beenden"))
        self.label_3.setText(_translate("Dialog", "Gruppennachricht verfassen:"))
        self.label_4.setText(_translate("Dialog", "Private Chatnachricht verfassen:"))
        self.SendenPrivatmsg.setText(_translate("Dialog", "Senden"))
        self.label_5.setText(_translate("Dialog", "An:"))
        self.Nutzername.setText(_translate("Dialog", "Nutzername"))
        self.PNaktideakti.setText(_translate("Dialog", "Private Nachrichten aktivieren/deaktivieren"))

