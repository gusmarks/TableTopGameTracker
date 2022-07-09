from PyQt5.QtWidgets import  *
from PySide6 import QtCore, QtWidgets, QtGui



class CharicterCreator(QtWidgets.QWidget):
    def __init__(self,mainFrame):
    # body of the constructor
        super().__init__()


    def buildPersonalInfoColection(self):

        self.Nametextbox = QLineEdit(self)
        self.Nametextbox.move(20, 20)
        self.Nametextbox.resize(280,40)

        self.Alingmenttextbox = QLineEdit(self)
        self.Alingmenttextbox.move(20, 20)
        self.Alingmenttextbox.resize(280,40)

        self.Playernametextbox = QLineEdit(self)
        self.Playernametextbox.move(20, 20)
        self.Playernametextbox.resize(280,40)

        self.PersonalVlayout= QtWidgets.QVBoxLayout()
        self.PersonalHlayout=QtWidgets.QHBoxLayout()
