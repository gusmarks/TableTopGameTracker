from cProfile import label
from PyQt5.QtGui import QImage, QPainter, QPicture, QPixmap, QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QTextEdit, QVBoxLayout, QWidget
from PySide6 import QtCore, QtWidgets, QtGui
import sys
from code.EnemyWidget import *
from code.DmLogin import *
from code.AdventureSelectionDialog import *


class MainFrame(QtWidgets.QMainWindow):
    def getCurrentDm(self):
        return self.currentdm
    def BuildStatusAndMenuBars(self):

        self.menu = QtWidgets.QMenuBar(self)
        self.menu.addAction("Login", self.openDmLogin)
        self.menu.addAction("adventure Selection", self.openAdvSelect)
        self.setMenuBar(self.menu)

        self.statusbar = QtWidgets.QStatusBar()
        self.stat1= QtWidgets.QStatusBar()
        if(self.currentdm !=None):
            self.stat1.showMessage("DM: "+self.currentdm.getName())
        self.stat2 = QtWidgets.QStatusBar()
        if(self.currentdm.getCurrentAdv() !=None):
            self.stat2.showMessage(self.currentdm.getCurrentAdv().getName())
        else:
            self.stat2.showMessage("no adventure selected")
        self.statusbar.insertWidget(0,self.stat1,0)
        self.statusbar.insertWidget(1,self.stat2,0)
        self.setStatusBar(self.statusbar)

    def BuildDockWidgets(self):
        # make and add dock widgets to QMainWindow
        self.dockExp = QtWidgets.QDockWidget("expolorer", self)
        self.dockExp.setAllowedAreas(
            QtCore.Qt.DockWidgetArea.LeftDockWidgetArea)
        self.addDockWidget(
            QtCore.Qt.DockWidgetArea.LeftDockWidgetArea, self.dockExp)
        # fillDocwidget with other widgets and layouts
        ExplorerText = QtWidgets.QListWidget()
        ExplorerButton = QtWidgets.QPushButton("Leave Adventure.")
        ExplorerWidget = QtWidgets.QWidget()
        vSizer = QtWidgets.QVBoxLayout(ExplorerWidget)
        vSizer.addWidget(ExplorerText)
        vSizer.addWidget(ExplorerButton)
        self.dockExp.setWidget(ExplorerWidget)

    def BuildTabWidget(self):
        # Maps page
        imgHolder = QtWidgets.QLabel()
        img = QtGui.QPixmap("")
        Width = imgHolder.width()
        Height = imgHolder.height()
        imgHolder.setPixmap(img.scaled(
            Width, Height, QtCore.Qt.KeepAspectRatio))
        imgHolder.show()
        # story page
        StoryEdit = QtWidgets.QTextEdit()
        # Characters page
        PlaceHolder1 = QtWidgets.QLabel("Placeholder")
        # Enemies page
        PlaceHolder2 = EnemiesPage(self)
        # Notes page
        NotesEdit = QtWidgets.QTextEdit()
        # tabWidget
        tabWidget = QtWidgets.QTabWidget()
        tabWidget.addTab(imgHolder, "Maps")
        tabWidget.addTab(StoryEdit, "Story")
        tabWidget.addTab(PlaceHolder1, "Characters")
        tabWidget.addTab(PlaceHolder2, "Enemies")
        tabWidget.addTab(NotesEdit, "Notes")
        tabWidget.setTabVisible(0, True)
        tabWidget.show()

        self.setCentralWidget(tabWidget)
        self.show()
     # dialog opening
    def openDmLogin(self):
        loginDialog = DMLogin(self)
        loginDialog.resize(500, 500)
        loginDialog.exec()
        self.currentdm = loginDialog.getDm()

    def openAdvSelect(self):
        if(self.currentdm != None):
            AdvDialog = AdventureSelectionDialog(self, self.currentdm)
            AdvDialog.resize(500, 500)
            AdvDialog.setModal(True)
            AdvDialog.exec()
            tempadv = self.currentdm.getCurrentAdv()
            self.stat2.clearMessage()
            self.stat2.showMessage("Adventure: "+tempadv.getName())


    def __init__(self):
        # body of the constructor
        super().__init__()
        self.currentdm = None
        self.openDmLogin()
        self.BuildStatusAndMenuBars()

        self.openAdvSelect()
        
        self.BuildTabWidget()
        #self.BuildDockWidgets()
