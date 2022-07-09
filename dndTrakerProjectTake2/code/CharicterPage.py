
from PyQt5.QtWidgets import  *
from PySide6 import QtCore, QtWidgets, QtGui
import io,os
from PIL import Image, ImageCms
import PySide6
import shutil
import csv

class CharicterPage(QtWidgets.QWidget):
    def __init__(self,mainFrame):
    # body of the constructor
        super().__init__()
        self.CreateLocalData(mainFrame)
        self.buildCharList()
        self.BuildStatBlock()
        #self.loadCharsFromDm()

        Vlayout= QtWidgets.QVBoxLayout()
        Hlayout=QtWidgets.QHBoxLayout()
        Hlayout.addLayout(self.listLayout)
        Vlayout.addWidget(self.statWidget)
        Hlayout.addLayout(Vlayout)
        self.setLayout(Hlayout)



    def BuildStatBlock(self):
        self.statWidget = QtWidgets.QWidget()
        StatLayout = QtWidgets.QVBoxLayout()
        TopLayout = QtWidgets.QHBoxLayout()
        CenterLayout = QtWidgets.QHBoxLayout()
        BottomLayout = QtWidgets.QHBoxLayout()
        
        self.HpTmpHpACHitDice = QtWidgets.QLabel()
        self.speed = QtWidgets.QLabel()
        self.Prof = QtWidgets.QLabel()
        
        self.MainStats = QtWidgets.QLabel()
        self.saves = QtWidgets.QLabel()
        self.skills = QtWidgets.QLabel()

        self.attcks = QtWidgets.QLabel()
        self.LangAndProfs = QtWidgets.QListView()
        self.LangAndProfs.setWordWrap(True)


        TopLayout.addWidget( self.Prof)
        TopLayout.addWidget( self.HpTmpHpACHitDice)
        TopLayout.addWidget( self.speed)

        CenterLayout.addWidget( self.MainStats)
        CenterLayout.addWidget( self.saves)
        CenterLayout.addWidget( self.skills)

        BottomLayout.addWidget( self.attcks)
        BottomLayout.addWidget( self.LangAndProfs)

        StatLayout.addLayout(TopLayout)
        StatLayout.addLayout(CenterLayout)
        StatLayout.addLayout(BottomLayout)

        self.statWidget.setLayout(StatLayout)

    def CreateLocalData(self,mainFrame):
        self.frame= mainFrame
        self.currentChar= None

    def buildCharList(self):
        self.CharList = QtWidgets.QListWidget()
        self.listLayout = QtWidgets.QVBoxLayout()
        self.newCharBtn = QtWidgets.QPushButton("Add New Enemy")
        self.listLayout.addWidget(self.CharList)
        self.listLayout.addWidget(self.newCharBtn)
        #self.CharList.clicked.connect(self.setEnemyFromListToPage)
        #self.newCharBtn.clicked.connect(self.selectAndAddEnemytoList)


    def loadCharsFromDm(self):
        CharInfolist = self.frame.getCurrentDm().getCurrentAdv().getEnemyList()
        for E in CharInfolist:
            self.enemiesList.addItem(E[1])

