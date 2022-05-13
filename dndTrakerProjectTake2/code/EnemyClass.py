import os
import csv
class EnemyClass:
    def __init__(self,Foldername):
        self.fileNames = GetFileNamesFromFolder(Foldername)
       # EnemyInfo = GetEnemyInfoFromCSV(fileNames[0])
        #self.textFile = fileNames[1]
       # self.EnemyImageFile= fileNames[2]
        
        self.name=""
        self.Source =""
        self.size=""
        self.type =""
        self.Alingment=""
        self.enviroment=""
        self.numaricStats= []
        self.substats=[]
        self.traitsAndActions=[]

    def getName(self):
        return self.name

    def setName(self,Name):
        self.name =Name
        
    def GetFileNamesFromFolder(Foldername):
        filenames = []
        for file in os.listdir(Foldername):
            if file.endswith(".csv"):
                filenames[0]= file
            if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
                filenames[1]=file
            if file.endswith(".txt"):
                filenames[2]=file
        print(filenames)

    def GetEnemyInfoFromCSV(csvFile):
        with open('employee_birthday.txt') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are {", ".join(row)}')
                    line_count += 1
                else:
                    print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                    line_count += 1
            print(f'Processed {line_count} lines.')
