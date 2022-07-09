import sys
import os
import pathlib
import csv
sys.path.insert(0, 'code')

import MainFrame

from PyQt5.QtWidgets import QInputDialog
from PySide6 import  QtWidgets


def testing(self):
    AdventureName = QInputDialog.getText(self,"aan","naa")


def SplitEnemyCSVIntoSingulars():
    path = str(pathlib.Path(__file__).parent.resolve())
    path=path+"/data/Enemies"
    fileName = path + "/Bestiary.csv"
    print(fileName)
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file,delimiter =',')
        lineCount =0
        lineNames = ''
        commonNameCount=0
        tempNameForDups=""
        for row in csv_reader:

            if lineCount==0:
                lineNames=row
                lineCount =lineCount+1

            else:
                if(not os.path.isdir(path+'/'+row[0])):
                    tempNameForDups=path+'/'+row[0]
                    os.mkdir(path+'/'+row[0])
                    
                else:
                    if(tempNameForDups==path+'/'+row[0]):
                        commonNameCount=commonNameCount+1
                        os.mkdir(path+'/'+row[0]+str(commonNameCount))

                with open(path+"/"+row[0]+"/"+row[0]+".csv",'w',newline='') as csv_fileNew:
                    linewriter = csv.writer(csv_fileNew)
                    linewriter.writerow(lineNames)
                    linewriter.writerow(row)
                    csv_fileNew.close


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
  

    Frame = MainFrame.MainFrame()
    Frame.resize(1000, 700)
    Frame.show()

    sys.exit(app.exec_())
    