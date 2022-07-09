


class Adventure:
    def __init__(self,Name,Path,Type):
        self.name = Name
        self.path =Path
        self.type = Type
        self.EnemyList=[]
        self.CharList = []
        self.storyList = []
        self.mapslist=[]
        self.notesList = []
        self.currentEnemy = None
        self.currentChar = None
        self.currentStory = None
        self.currentMap=None
        self.CurrentNotes = None
    #name
    def getName(self):
        return self.name
    def setName(self,Name):
        self.name =Name

    #type
    def getType(self):
        return self.type
    def setName(self,type):
        self.type =type

    #path
    def getPath(self):
        return self.path
    def setName(self,Path):
        self.path =Path

    #story
    def getStory(self):
        return self.currentStory
    def setStory(self,story):
        self.currentStory=story

    #map
    def getMap(self):
        return self.currentMap
    def setMap(self,map):
        self.currentMap=map

    #notes
    def getNotes(self):
        return self.CurrentNotes
    def setNotes(self,notes):
        self.CurrentNotes=notes

   #charlist
    def getCharList(self):
        return self.CharList
    def addtoCharList(self,char):
        self.CharList.append(char)
    def removeCharfromList(self,char):
        self.CharList.remove(char)

    #enemylist
    def getEnemyList(self):
        return self.EnemyList
    def addtoEnemyList(self,ENM,EnmName):
        self.EnemyList.append((ENM,EnmName))
    def removeEnemyfromList(self,ENM):
        self.EnemyList.remove(ENM)

    #mapslist
    def getMapList(self):
        return self.mapslist
    def addtoMapList(self,newmap,mapName):
        self.mapslist.append((newmap,mapName))
    def removeMapfromList(self,map):
        self.mapslist.remove(map)

    #Noteslist
    def getNotesList(self):
        return self.notesList
    def addtoNotesList(self,Note,notename):
        self.notesList.append((Note,notename))
    def removeFromNotesList(self,Note):
        self.notesList.remove(Note)
    #story list
    def getStoryList(self):
        return self.storyList
    def addtoStoryList(self,Note,storyname):
        self.storyList.append((Note,storyname))
    def removeFromStoryList(self,story):
        self.storyList.remove(story)