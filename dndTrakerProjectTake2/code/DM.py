import mariadb,os
import sys
import shutil
class DM:
    def __init__(self,Name,Path):
        self.name = Name
        self.path =Path
        self.AdventureList = []
        self.currentAdventure = None
        
        self.getAdventures()

    def getName(self):
        return self.name

    def setName(self,Name):
        self.name =Name
    def getPath(self):
        return self.path

    def setPath(self,Path):
        self.path =Path

    def getCurrentAdv(self):
        if(self.currentAdventure!=None):
            return self.currentAdventure
        return None
        
    def setCurrentAdv(self,adv):
        self.currentAdventure=adv
    def getAdventures(self):
        try:
            conn = mariadb.connect(
                user="Gus",
                password="",
                host="localhost",
                port=3306,
                database="DnDAdventures"
            )
        except mariadb.Error as e:
          print(f"Error connecting to MariaDB Platform: {e}")
          sys.exit(1)

        cur = conn.cursor()
        str = "SELECT * FROM Adventures WHERE DmName ="+"'"+self.name+"'"
        cur.execute(str)  
        Adventures = cur.fetchall()
        for x in Adventures:
            self.AdventureList.append(x)

    # add to folder functions
    def addMaptoDmFolder(self,fileN,Name):
        source=fileN
        dest = self.getCurrentAdv().getPath()+"/Maps"+"/"+Name
        shutil.copy(source, dest)
        self.getCurrentAdv().addtoMapList(dest,Name)

    
    def addNotetoDmFolder(self,text,name):
        with open(name, 'w') as yourFile:
            yourFile.write(str(text))


    def addChartoDmFolder(self,filePathandName):
        CharPath = self.getCurrentAdv().getPath()+"/Characters"
        # make csv files with all info
        
        

    def addStorytoDmFolder(self,filePathandName):
        StoryPath = self.getCurrentAdv().getPath()+"/Story"
        shutil.copy(filePathandName, StoryPath)

    def addEnemyoDmFolder(self,filePathandName):
        pass  
        

#load information from file

    def loadMapsFromFolder(self):
        mapsPath = self.getCurrentAdv().getPath()+"/Maps"
        for E in os.listdir(mapsPath):
            self.getCurrentAdv().addtoMapList(mapsPath+"/"+E,E)


    def loadNotesFromFolder(self):
        NotesPath = self.getCurrentAdv().getPath()+"/Notes"
        for E in os.listdir(NotesPath):
            file_exists = os.path.exists(NotesPath+"/"+E)
            if(file_exists):
                self.getCurrentAdv().addtoNotesList(NotesPath+"/"+E,E)

    def loadStoryFromFolder(self):
        StoryPath = self.getCurrentAdv().getPath()+"/Story"
        for E in os.listdir(StoryPath):
            file_exists = os.path.exists(StoryPath+"/"+E)
            if(file_exists):
                self.getCurrentAdv().addtoStoryList(StoryPath+"/"+E,E)
    
    def loadEnemiesFromFolder(self):

        EnemiesPath = self.getCurrentAdv().getPath()+"/Enemies"
        for E in os.listdir(EnemiesPath):

            self.getCurrentAdv().addtoEnemyList(EnemiesPath+"/"+E,E)#edit to use enemie class
        
    def loadCharsFromFolder(self):

        CharPath = self.getCurrentAdv().getPath()+"/Characters"
        for E in os.listdir(CharPath):

            self.getCurrentAdv().addtoCharList(CharPath+"/"+E,E)#edit to use enemie class
        
        