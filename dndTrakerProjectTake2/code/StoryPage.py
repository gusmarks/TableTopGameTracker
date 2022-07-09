from PySide6 import QtCore, QtWidgets, QtGui


class StoryPage(QtWidgets.QWidget):
    def __init__(self,mainFrame):
    # body of the constructor
        super().__init__()
        self.frame=mainFrame
        self.buildNotesList()
        self.buildNoteArea()
        self.loadStoryFromDm()
        self.layOut = QtWidgets.QHBoxLayout()
        self.layOut.addLayout(self.listLayout,2)
        self.layOut.addWidget(self.storyWidget,4)
        self.setLayout(self.layOut)


    def buildNotesList(self):
        self.storyList = QtWidgets.QListWidget()
        self.listLayout = QtWidgets.QVBoxLayout()
        self.newStoryBtn = QtWidgets.QPushButton("Add Story")
        self.listLayout.addWidget(self.storyList)
        self.listLayout.addWidget(self.newStoryBtn)
        self.storyList.clicked.connect(self.selectAndLoadStory)
        self.newStoryBtn.clicked.connect(self.addToStoryist)

    def buildNoteArea(self):
        self.storyWidget = QtWidgets.QTextEdit()
        self.storyWidget.acceptRichText()

    def addToStoryist(self):
        #change location eventualy
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.frame,
        "Open File", "/home/gus/Documents/SoftwareDevelpometFiles/00-Personal_Projects/dndTrakerProjectTake2/data", "Txt document (*.txt)")
        name= fileName[0]
        pos=name.rfind("/")
        name = name[pos+1:]
        self.storyList.addItem(name)
        
        self.frame.getCurrentDm().addStorytoDmFolder(fileName[0])

    def selectAndLoadStory(self):
        
        selection=self.storyList.selectedItems()
        for E in self.frame.getCurrentDm().getCurrentAdv().getStoryList():
            if(E[1]==selection[0].text()):
                self.storyWidget.clear()
                with open(E[0]) as f:  
                    lines = f.readlines()
                    for Entry in lines:
                        self.storyWidget.insertPlainText (Entry)

    def loadStoryFromDm(self):
        Noteinfo = self.frame.getCurrentDm().getCurrentAdv().getStoryList()
        for E in Noteinfo:
            if(E[1].endswith('.txt')):
                self.storyList.addItem(E[1])
        
