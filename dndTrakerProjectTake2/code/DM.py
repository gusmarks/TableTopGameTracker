import numpy as np
import mariadb
import sys
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
        #print(str)
        cur.execute(str)  
        Adventures = cur.fetchall()
        for x in Adventures:
            self.AdventureList.append(x)