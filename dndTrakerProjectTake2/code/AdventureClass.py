


class Adventure:
    def __init__(self,Name,Path,Type):
        self.name = Name
        self.path =Path
        self.type = Type
        self.EnemyList=None
        self.CharList = None
        self.currentStory = None
        self.mapslist=None
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
    def addtoCharList(self,ENM):
        self.EnemyList.append(ENM)
    def removeCharfromList(self,ENM):
        self.EnemyList.remove(ENM)

    #mapslist
    def getMapList(self):
        return self.mapslist
    def addtoCharList(self,newmap):
        self.mapslist.append(newmap)
    def removeCharfromList(self,map):
        self.mapslist.remove(map)