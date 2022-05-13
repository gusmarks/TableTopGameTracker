#from PyQt5.QtGui import *
from PyQt5.QtWidgets import  *
from code.AdventureClass import * 
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6

class AdventureIcon(QtWidgets.QWidget):
    def __init__(self,advName,advpath,advType,parrent):
        super().__init__()
        self.adventureLabel = QtWidgets.QLabel(advName)
        self.path = advpath
        self.type = advType
        self.Parrent=parrent
        self.Adventure= None
        
        self.adventureImage = QtWidgets.QLabel()
        img = QtGui.QPixmap(self.path+"/"+self.type+".png")
        Width = 50
        Height = 50
        self.adventureImage.setPixmap(img.scaled(Width,Height, QtCore.Qt.KeepAspectRatio))
        self.adventureImage.show()
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.adventureLabel)
        layout.addWidget(self.adventureImage)
        self.setLayout(layout)
        self.Adventure= Adventure(self.adventureLabel.text(),self.path,self.type)
        self.setCursor(PySide6.QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.Parrent.setAdv(self.Adventure)
        self.Parrent.getParent().done(0) 
        return super().mouseDoubleClickEvent(event)

    def getName(self):
        return self.adventureLabel.text()
    def getAdv(self):
        return self.Adventure
