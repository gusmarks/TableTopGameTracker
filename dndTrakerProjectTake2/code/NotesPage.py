from PyQt5.QtWidgets import *
from PySide6 import QtWidgets

class notesPage(QtWidgets.QWidget):

    def __init__(self,mainFrame):
    # body of the constructor
        super().__init__()
        self.frame=mainFrame
        self.buildNotesList()
        self.buildNoteArea()
        self.loadNotesFromDm()
        self.layOut = QtWidgets.QHBoxLayout()
        self.layOut.addLayout(self.listLayout,2)
        self.layOut.addWidget(self.notewidget,4)
        self.setLayout(self.layOut)


    def buildNotesList(self):
        self.noteList = QtWidgets.QListWidget()
        self.listLayout = QtWidgets.QVBoxLayout()
        self.newNoteBtn = QtWidgets.QPushButton("Add Note")
        self.listLayout.addWidget(self.noteList)
        self.listLayout.addWidget(self.newNoteBtn)
        self.noteList.clicked.connect(self.selectAndLoadNote)
        self.newNoteBtn.clicked.connect(self.addToNotesListAndSaveNote)

    def buildNoteArea(self):

        self.notewidget = QtWidgets.QTextEdit()

    def addToNotesListAndSaveNote(self):
        if(self.notewidget.toPlainText()!=""):
            noteName = QtWidgets.QInputDialog.getText(self.frame, 'Text Input', 'Enter a name for the note:')
            text = self.notewidget.toPlainText()
            self.noteList.addItem(noteName[0])
            filenameAndPath = self.frame.getCurrentDm().getCurrentAdv().getPath()+"/Notes"+"/"+noteName[0]+".txt"
            self.frame.getCurrentDm().addNotetoDmFolder(text,filenameAndPath)

    def loadNotesFromDm(self):
        Noteinfo = self.frame.getCurrentDm().getCurrentAdv().getNotesList()
        for E in Noteinfo:
            self.noteList.addItem(E[1])

    def selectAndLoadNote(self):

        selection=self.noteList.selectedItems()
        for E in self.frame.getCurrentDm().getCurrentAdv().getNotesList():

            if(E[1]==selection[0].text()):
                self.notewidget.clear()
                with open(E[0]) as f:
                    lines = f.readlines()
                    for line in lines:
                        self.notewidget.insertPlainText (line)