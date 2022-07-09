import  shutil
from PyQt5.QtCore import Qt
from PySide6 import  QtWidgets,QtGui,QtCore
import mariadb
import os
from DM import * 
from AdventureIcon import *
from AdventureClass import *
class AdventureCreatorWidget(QtWidgets.QWidget):
    def __init__(self,dm,parent):
        super().__init__()
        self.currentDm = dm
        self.Adventure = None
        self.Parent=parent
        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel("Adventure Creation")

        self.AdventureName = QtWidgets.QLineEdit(self)
        self.AdventureType = QtWidgets.QComboBox(self)
        self.AdventureType.addItem("DND")
        self.AdventureType.addItem("COC")
        self.AdventureType.addItem("TNG")
        self.newAdventBttn =QtWidgets.QPushButton("New Adventure")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.AdventureName)
        self.layout.addWidget(self.AdventureType)
        self.layout.addWidget(self.newAdventBttn)
        self.newAdventBttn.clicked.connect(self.createAdventure)

    #create a new Adventure: make an entry into the Adventures table of the Database, then make the Folders needed
    def createAdventure(self):
        
        AdventurePath= "/Adventures"
        AdventurePath = AdventurePath + "/"+self.AdventureName.text()
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

        cur = conn.cursor()
        sql = "SELECT Name FROM Adventures"
        data = ""
        cur.execute(sql,data)
        for name in cur:
            if(name == self.AdventureName.text()):
                return

        tmpPath= self.currentDm.getPath()
        tmpPathindex = tmpPath.rfind("/")
        tmpPath= tmpPath[0:tmpPathindex]
        tmpPathindex = tmpPath.rfind("/")
        tmpPath= tmpPath[0:tmpPathindex]
        
        sql = "INSERT INTO Adventures (Name, DmName, Path,AdventType) VALUES (%s, %s, %s,%s)"
        val = (self.AdventureName.text(), self.currentDm.name,AdventurePath,self.AdventureType.currentText())
        cur.execute(sql, val)  
        conn.commit() 

        Foldernames = ["Maps","Story","Characters","Enemies","Notes"]
        for E in Foldernames:
            os.makedirs(self.currentDm.getPath()+AdventurePath  +"/"+ E)
        
        shutil.copy2(tmpPath+"/"+self.AdventureType.currentText() +".png",self.currentDm.getPath()+AdventurePath+"/"+self.AdventureType.currentText() +".png")
        self.Adventure= Adventure(self.AdventureName.text(),self.currentDm.getPath()+AdventurePath,self.AdventureType)
        if(self.Adventure!= None):
           self.setAdv(self.Adventure)
           self.Parent.done(0)
    def getAdv(self):
        return self.Adventure
    def getParent(self):
        return self.Parent
    def setAdv(self,Adv):
        self.adventure=Adv
        self.setDmAdventure(self.adventure)

    def setDmAdventure(self,adv):
        self.currentDm.setCurrentAdv(adv)


class AdventureSelectorWidget(QtWidgets.QWidget):
    def __init__(self,dm,parent):
        super().__init__()
        self.currentDm = dm
        self.Adventurewidgets = []
        self.AdventurewidgetsInfo = []
        self.adventure = None
        self.Parent=parent
        self.layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel("Adventure Selection")
        self.Gridlayout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.Gridlayout)
        self.loadAdventures()
        self.setupAdventureWidgets(self.AdventurewidgetsInfo)
        
    
    def getParent(self):
        return self.Parent

    def setupAdventureWidgets(self,AdventurewidgetsInfo):
        row=0
        col=0
        for entry in AdventurewidgetsInfo:
            tempAdv = Adventure(entry[0],self.currentDm.getPath()+entry[2],entry[3])
            tempwidget=AdventureIcon(tempAdv,self)

            self.Adventurewidgets.append(tempwidget)
            self.Gridlayout.addWidget(tempwidget,row,col,QtCore.Qt.AlignLeft)
            
            col=col+1

            if(col>3):
                col=col=0
                row=row+1
    def loadAdventures(self):
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
        cur = conn.cursor()
        sql = "SELECT * FROM Adventures WHERE DMname = %s"
        data = (self.currentDm.getName(),)
        cur.execute(sql,data)
        for E in cur:
            self.AdventurewidgetsInfo.append(E)



       
        #add loaded data to AdventureWidgetsInfo and pass to setupAdventureWidgets

    def getAdv(self):
        return self.adventure
    def setAdv(self,Adv):
        self.adventure=Adv
        self.setDmAdventure(self.adventure)

    def setDmAdventure(self,adv):
        self.currentDm.setCurrentAdv(adv)
    



