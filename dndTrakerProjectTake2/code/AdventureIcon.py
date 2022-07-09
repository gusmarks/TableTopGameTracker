from PyQt5.QtWidgets import  *
from AdventureClass import * 
from PySide6 import QtCore, QtWidgets, QtGui
import PySide6

class AdventureIcon(QtWidgets.QWidget):
    def __init__(self,Advent,parrent):
        super().__init__()
        self.Adventure= Advent
        self.adventureLabel = QtWidgets.QLabel(self.Adventure.getName())
        self.path = self.Adventure.getPath()
        self.type = self.Adventure.getType()
        self.Parrent=parrent
        
        self.adventureImage = QtWidgets.QLabel()
        img = QtGui.QPixmap(self.path+"/"+self.type+".png")
        Width = 60
        Height = 60
        self.adventureImage.setPixmap(img.scaled(Width,Height, QtCore.Qt.KeepAspectRatio))
        self.adventureImage.show()
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.adventureLabel)
        layout.addWidget(self.adventureImage)
        self.setLayout(layout)
        
        self.setCursor(PySide6.QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def mouseDoubleClickEvent(self, event: PySide6.QtGui.QMouseEvent) -> None:
        self.Parrent.setAdv(self.Adventure)
        self.Parrent.getParent().done(0) 
        return super().mouseDoubleClickEvent(event)

    def getName(self):
        return self.adventureLabel.text()
    def getAdv(self):
        return self.Adventure
