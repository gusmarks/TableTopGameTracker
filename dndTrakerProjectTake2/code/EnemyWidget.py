from EnemyClass import*
from PyQt5.QtWidgets import  *
from PySide6 import QtCore, QtWidgets, QtGui
import io,os,sys
sys.path.insert(0, 'PIL')
from PIL import Image, ImageCms
import PySide6
import shutil
import csv

class EnemiesPage(QtWidgets.QWidget):
    def __init__(self,mainFrame):
    # body of the constructor
        super().__init__()
        self.CreateLocalData(mainFrame)
        self.BuildImageWidget()
        self.BuildStoryWidget()
        self.BuildStatBlock()
        self.buildEnemiesList()
        self.loadEnemiesFromDm()
        Vlayout= QtWidgets.QVBoxLayout()
        Hlayout=QtWidgets.QHBoxLayout()
        Vlayout.addWidget(self.imageWidget)
        Vlayout.addWidget(self.StoryWidget)
        Hlayout.addLayout(self.listLayout)
        Hlayout.addWidget(self.statWidget)
        Hlayout.addLayout(Vlayout)
        self.setLayout(Hlayout)
    def CreateLocalData(self,mainFrame):
        self.frame= mainFrame
        self.currentEnemy= None

    def BuildImageWidget(self):
        self.imageWidget = QtWidgets.QWidget()
        ImageLayout = QtWidgets.QVBoxLayout()

        self.imgHolder = QtWidgets.QLabel()
        self.convert_to_srgb("/home/gus/Documents/SoftwareDevelpometFiles/00-Personal_Projects/dndTrakerProjectTake2/data/Enemies/Goblin/GoblinImg.jpg")
        img = QtGui.QPixmap("/home/gus/Documents/SoftwareDevelpometFiles/00-Personal_Projects/dndTrakerProjectTake2/data/Enemies/Goblin/GoblinImg.jpg")
        Width = self.imgHolder.width()
        Height = self.imgHolder.height()
        self.imgHolder.setPixmap(img.scaled(Width,Height, QtCore.Qt.KeepAspectRatio))
        self.imgHolder.show()
        
        ImageLayout.addWidget(self.imgHolder)
        self.imageWidget.setLayout(ImageLayout)

    def BuildStoryWidget(self):
        self.StoryWidget = QtWidgets.QWidget()
        StoryLayout = QtWidgets.QVBoxLayout()

        self.StoryDisplay= QtWidgets.QTextEdit()
        StoryLayout.addWidget(self.StoryDisplay)
        self.StoryWidget.setLayout(StoryLayout)

    def BuildStatBlock(self):
        self.statWidget = QtWidgets.QWidget()
        StatLayout = QtWidgets.QVBoxLayout()

        self.statDisplay = QtWidgets.QListWidget()
        self.statDisplay.setWordWrap(True)
        StatLayout.addWidget(self.statDisplay)
        self.statWidget.setLayout(StatLayout)

    def buildEnemiesList(self):
        self.enemiesList = QtWidgets.QListWidget()
        self.listLayout = QtWidgets.QVBoxLayout()
        self.newEnemyBtn = QtWidgets.QPushButton("Add New Enemy")
        self.listLayout.addWidget(self.enemiesList)
        self.listLayout.addWidget(self.newEnemyBtn)
        self.enemiesList.clicked.connect(self.setEnemyFromListToPage)
        self.newEnemyBtn.clicked.connect(self.selectAndAddEnemytoList)

    def loadEnemiesFromDm(self):
        EnemieInfolist = self.frame.getCurrentDm().getCurrentAdv().getEnemyList()
        for E in EnemieInfolist:
            self.enemiesList.addItem(E[1])


    def selectAndAddEnemytoList(self):
        if(self.frame.getCurrentDm().getCurrentAdv()!=None):
            tmpPath= self.frame.getCurrentDm().getPath()
            tmpPathindex = tmpPath.rfind("/")
            tmpPath= tmpPath[0:tmpPathindex]
            tmpPathindex = tmpPath.rfind("/")
            tmpPath= tmpPath[0:tmpPathindex]
            MainEnemyFolderPath=QtWidgets.QFileDialog.getExistingDirectory(
                                self, "Open Directory", tmpPath+"/Enemies", PySide6.QtWidgets.QFileDialog.Option.ShowDirsOnly)
            DmFolderPath=self.frame.getCurrentDm().getCurrentAdv().getPath()+"/Enemies"
            pos=MainEnemyFolderPath.rfind("/")
            folderName = MainEnemyFolderPath[pos:]
            os.mkdir(DmFolderPath+folderName)
            for file_name in os.listdir(MainEnemyFolderPath):
                # construct full file path
                source = MainEnemyFolderPath +"/" +file_name
                destination = DmFolderPath +folderName+"/"+ file_name
                # copy only files
                if os.path.isfile(source):
                    shutil.copy(source, destination)
            folderName = folderName[1:]
            self.enemiesList.addItem(folderName)
        
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

    def setEnemyFromListToPage(self):
        name = self.enemiesList.selectedItems()
        enemieinfo = []
        path=self.frame.getCurrentDm().getCurrentAdv().getPath()+"/Enemies"
        for entry in os.listdir(path):
            if(entry==name[0].text()):
                for file in os.listdir(path+"/"+entry):
                    enemieinfo.append(file)

        enemieinfo[2] =path+"/"+name[0].text()+"/"+enemieinfo[2]
        enemieinfo[1] =path+"/"+name[0].text()+"/"+enemieinfo[1]
        enemieinfo[0] =path+"/"+name[0].text()+"/"+enemieinfo[0]
        for E in enemieinfo:

            if(E.endswith(".txt")):
                self.handleTXT(E)
            if(E.endswith(".csv")):
                self.handleCSV(E)
            if(E.endswith(".png")or E.endswith(".jpg")):
                self.handleImage(E)

    def handleTXT(self,file):
        self.StoryDisplay.clear()
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                self.StoryDisplay.insertPlainText(line)
        
    def handleCSV(self,Csv):
        rowTitles=[]
        rowInfo= []
        i=0
        with open(Csv, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for row in reader:
                
                if(i==0):
                    rowTitles=row
                    i=i+1
                else:
                    rowInfo=row
        self.statDisplay.clear()
        for title,info in zip(rowTitles,rowInfo):
            info =info.replace(".","\n")
            self.statDisplay.addItem(title+":"+info)


    def handleImage(self,file):
        #self.convert_to_srgb(file)
        img = QtGui.QPixmap(file)
        Width = self.imgHolder.width()
        Height = self.imgHolder.height()
        self.imgHolder.setPixmap(img.scaled(Width,Height, QtCore.Qt.KeepAspectRatio))
