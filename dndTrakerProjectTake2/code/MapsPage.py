from PyQt5.QtWidgets import *
from PySide6 import QtCore, QtWidgets, QtGui


class mapsPage(QtWidgets.QWidget):

    def __init__(self,mainFrame):
    # body of the constructor
        super().__init__()
        self.frame=mainFrame
        
        self.buildMapsList()
        self.buildImageArea()
        self.loadMapsFromDm()
        self.layOut = QtWidgets.QHBoxLayout()
        self.layOut.addLayout(self.listLayout,2)
        self.layOut.addWidget(self.imgHolder,4)
        self.setLayout(self.layOut)

    def buildImageArea(self):
        self.imgHolder = QtWidgets.QLabel()
        img = QtGui.QPixmap(None)
        Width = self.imgHolder.width()
        Height = self.imgHolder.height()
        self.imgHolder.setPixmap(img.scaled(Width, Height, QtCore.Qt.KeepAspectRatio))
        self.imgHolder.show()

    def buildMapsList(self):
        self.mapList = QtWidgets.QListWidget()
        self.listLayout = QtWidgets.QVBoxLayout()
        self.newMapBtn = QtWidgets.QPushButton("Add New Map")
        self.listLayout.addWidget(self.mapList)
        self.listLayout.addWidget(self.newMapBtn)
        self.mapList.clicked.connect(self.selectAndLoadMap)
        self.newMapBtn.clicked.connect(self.addToMapsList)

    def addToMapsList(self):
        #change location eventualy
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.frame,
        "Open Image", "/home/gus/Documents/SoftwareDevelpometFiles/00-Personal_Projects/dndTrakerProjectTake2/data", "Image Files (*.png *.jpg *.bmp)")
        name= fileName[0]
        pos=name.rfind("/")
        name = name[pos+1:]
        self.mapList.addItem(name)
        self.frame.getCurrentDm().addMaptoDmFolder(fileName[0],name)

    def selectAndLoadMap(self):
        selection=self.mapList.selectedItems()
        for E in self.frame.getCurrentDm().getCurrentAdv().getMapList():
            if(E[1]==selection[0].text()):
                img = QtGui.QPixmap(E[0])
                Width = self.imgHolder.width()
                Height = self.imgHolder.height()
                self.imgHolder.setPixmap(img.scaled( Width, Height, QtCore.Qt.KeepAspectRatio))
    def loadMapsFromDm(self):
        mapinfo = self.frame.getCurrentDm().getCurrentAdv().getMapList()
        for E in mapinfo:
            self.mapList.addItem(E[1])
