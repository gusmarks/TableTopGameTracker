from cProfile import label
#import PySide6.QtCore
import sys
#import random
import os
import mariadb
import pathlib
from code.DM import *
from code.AdventureSelectionDialog import *
from PySide6 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QInputDialog, QWidget
import PySide6

class DMLogin(QtWidgets.QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.currentDm =""
        

        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel("DM Login")
        self.label2 = QtWidgets.QLabel("")
        self.Username = QtWidgets.QLineEdit(self)

        self.password =QtWidgets.QLineEdit(self)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)

        self.newDmBTN =QtWidgets.QPushButton("New DM+")
        self.loginBTN =QtWidgets.QPushButton("log in")

        self.newDmBTN.setCursor(PySide6.QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBTN.setCursor(PySide6.QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.Username)
        self.layout.addWidget(self.password)
        
        self.layout.addWidget(self.loginBTN)
        self.layout.addWidget(self.newDmBTN)

        self.newDmBTN.clicked.connect(self.NewDM)
        self.loginBTN.clicked.connect(self.login)
        self.path = ""
        


    def getDm(self):
        if(self.currentDm==None):
            return None
        return self.currentDm
#creates a new dm inside the database
    def NewDM(self):
         #Connect to MariaDB Platform
        try:
            conn = mariadb.connect(
                user="Gus",
                password="",
                host="localhost",
                port=3306,
                database="DnDAdventures"
                

             )
        except mariadb.Error as e:
          print(f"Error connecting to MariaDB Platform: {e}")
          sys.exit(1)

        cur = conn.cursor()

        self.path = str(pathlib.Path(__file__).parent.resolve())
        self.path=self.path.replace("/code","/data")

        self.path = self.path +"/DMs/"+ self.Username.text()
        try:
            sql = "INSERT INTO DMs (DmName, Password, Path) VALUES (%s, %s, %s)"
            val = (self.Username.text(), self.password.text(),self.path)
            cur.execute(sql, val)  
            conn.commit()
        except mariadb.Error as e:
            self.label2.setText("Dm Already Exists. please choose a diferant DM Name")
        else:
            self.makeNewDmFoldersAndFiles()
            #self.currentDm= DM(self.Username.text(),self.path)
        
    #end of new dmd method
    def makeNewDmFoldersAndFiles(self):
        
       
        if not os.path.exists(self.path):
            os.mkdir(self.path,7)
            os.mkdir(self.path+"/Adventures",7)
        open(self.path+"/"+"Adventures.txt", 'a')
        
        self.label2.setText("New DM:"+ self.Username.text() + " created.")
        self.Username.clear()
        self.password.clear()
    
    def login(self):
        try:
            conn = mariadb.connect(
                user="Gus",
                password="",
                host="localhost",
                port=3306,
                database="DnDAdventures"
            )
        except mariadb.Error as e:
          print(f"Error connecting to MariaDB Platform: {e}")
          sys.exit(1)

        cur = conn.cursor()


        bool = False
        cur.execute("SELECT DmName,Path FROM DMs")  
        DMNames = cur.fetchall()
        for x in DMNames:
            if(self.Username.text()==x[0]):
                bool=True
                self.path = x[1]
        
        if(bool == True):
            cur.execute("SELECT Password FROM DMs WHERE DmName ='"+self.Username.text()+"'")
            DMpassword = cur.fetchall()
            if(self.password.text()==DMpassword[0][0]):
                self.label2.setText("Log in Sucsessful")
                #password confirmed as well as user existance
                self.currentDm= DM(self.Username.text(),self.path)
                self.done(0)

            else:
                self.label2.setText("Login failed. Password incorect.")

        else:
            self.label2.setText("Login failed. Username not found.")
