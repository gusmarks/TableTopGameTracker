from multiprocessing import managers
from telnetlib import DM
from PyQt5.QtWidgets import QScrollArea
from PySide6 import QtCore, QtWidgets, QtGui
from code.AdventureSelectorWidget import *

class AdventureSelectionDialog(QtWidgets.QDialog):
    def __init__(self,parent,DM):
        super().__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.selecctorwidget = AdventureSelectorWidget(DM,self)
        self.creatorwidget = AdventureCreatorWidget(DM)

        tempAdv1=self.creatorwidget.getAdv()
        tempAdv2 = self. selecctorwidget.getAdv()
        self.layout.addWidget(self.creatorwidget)
        scrollarea = QtWidgets.QScrollArea()
        scrollarea.setWidget(self.selecctorwidget)
        self.layout.addWidget(scrollarea)
