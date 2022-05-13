
from fileinput import filename
from PyQt5.QtCore import QStringListModel
from code.EnemyClass import*
from PyQt5.QtGui import QImage, QPainter, QPicture, QPixmap, QPixmap
from PyQt5.QtWidgets import  *
from PySide6 import QtCore, QtWidgets, QtGui
import io,os
from PIL import ImageQt, Image, ImageCms
import PySide6

class EnemiesPage(QtWidgets.QWidget):
    def CreateLocalData(self,mainFrame):
        self.mainframe= mainFrame
        self.currentEnemy= None
    def selectAndAddEnemytoList(self):
        #print(parent.getCurrentDm().getPath())
        if(self.mainframe.getCurrentDm().getCurrentAdv()!=None):
           
            tmpPath= self.mainframe.getCurrentDm().getPath()
            
            tmpPathindex = tmpPath.rfind("/")
            tmpPath= tmpPath[0:tmpPathindex]
            tmpPathindex = tmpPath.rfind("/")
            tmpPath= tmpPath[0:tmpPathindex]

            MainEnemyFolderPath=QtWidgets.QFileDialog.getExistingDirectory(
                                                self, "Open Directory", tmpPath+"/Enemies", PySide6.QtWidgets.QFileDialog.Option.ShowDirsOnly)
            DmFolderPath=self.mainframe.getCurrentDm().getCurrentAdv().getPath()+"/Enemies"
            print(MainEnemyFolderPath)
            print(DmFolderPath)
            for file_name in os.listdir(MainEnemyFolderPath):
                # construct full file path
                source = MainEnemyFolderPath + file_name
                destination = DmFolderPath + file_name
                # copy only files
                if os.path.isfile(source):
                    shutil.copy(source, destination)
                    print('copied', file_name)


            #print(name)
            
           
            #for dir in os.walk(tmpPath):
             #   print(dir[2])
        
    def convert_to_srgb(self,file_path):
        '''Convert PIL image to sRGB color space (if possible)''' 
        img = Image.open(file_path)
        icc = img.info.get('icc_profile', '')
        if icc:
            io_handle = io.BytesIO(icc)     # virtual file
            src_profile = ImageCms.ImageCmsProfile(io_handle)
            dst_profile = ImageCms.createProfile('sRGB')
            img_conv = ImageCms.profileToProfile(img, src_profile, dst_profile)
            icc_conv = img_conv.info.get('icc_profile','')
        if icc != icc_conv:
            # ICC profile was changed -> save converted file
            img_conv.save(file_path,
                        format = 'JPEG',
                        quality = 50,
                        icc_profile = icc_conv)


    def BuildImageWidget(self):
        self.imageWidget = QtWidgets.QWidget()
        ImageLayout = QtWidgets.QVBoxLayout()

        imgHolder = QtWidgets.QLabel()
        self.convert_to_srgb("/home/gus/Documents/SoftwareDevelpometFiles/00-Personal_Projects/dndTrakerProjectTake2/data/Enemies/Goblin/GoblinImg.jpg")
        img = QtGui.QPixmap("/home/gus/Documents/SoftwareDevelpometFiles/00-Personal_Projects/dndTrakerProjectTake2/data/Enemies/Goblin/GoblinImg.jpg")
        Width = imgHolder.width()
        Height = imgHolder.height()
        imgHolder.setPixmap(img.scaled(Width,Height, QtCore.Qt.KeepAspectRatio))
        imgHolder.show()
        
        ImageLayout.addWidget(imgHolder)
        self.imageWidget.setLayout(ImageLayout)

    def BuildStoryWidget(self):
        self.StoryWidget = QtWidgets.QWidget()
        StoryLayout = QtWidgets.QVBoxLayout()

        StoryDisplay= QtWidgets.QTextEdit()
        StoryLayout.addWidget(StoryDisplay)
        self.StoryWidget.setLayout(StoryLayout)

    def BuildStatBlock(self):
        self.statWidget = QtWidgets.QWidget()
        StatLayout = QtWidgets.QVBoxLayout()

        statDisplay = QtWidgets.QListWidget()
        StatLayout.addWidget(statDisplay)
        self.statWidget.setLayout(StatLayout)

    def buildEnemiesList(self):
        self.enemiesList = QtWidgets.QListWidget()
        self.listLayout = QtWidgets.QVBoxLayout()
        self.newEnemyBtn = QtWidgets.QPushButton("Add New Enemy")
        self.listLayout.addWidget(self.enemiesList)
        self.listLayout.addWidget(self.newEnemyBtn)
        self.newEnemyBtn.clicked.connect(self.selectAndAddEnemytoList)

         
       
    def __init__(self,mainFrame):
    # body of the constructor
        super().__init__()
        self.CreateLocalData(mainFrame)
        self.BuildImageWidget()
        self.BuildStoryWidget()
        self.BuildStatBlock()
        self.buildEnemiesList()
        Vlayout= QtWidgets.QVBoxLayout()
        Hlayout=QtWidgets.QHBoxLayout()
        Vlayout.addWidget(self.imageWidget)
        Vlayout.addWidget(self.StoryWidget)
        Hlayout.addLayout(self.listLayout)
        Hlayout.addWidget(self.statWidget)
        Hlayout.addLayout(Vlayout)
        self.setLayout(Hlayout)

        
        