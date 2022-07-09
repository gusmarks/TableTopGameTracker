from tokenize import Number


class charicter():
    def __init__(self):
        self.playerName= ""
        self.charName = ""
        self.Class =""
        self.lvl=0
        self.background = ""
        self.race = ""
        self.Alignment = ""
         
        self.HP = 0
        self.maxHp=0
        self.temphp= 0
        self.AC = 0
        self.initiative = 0
        self.speed = 0
        self.hitdice=("",0)

        self.primaryStats = []
        self.skills = []
        self.savingthrows=[]
        self.skillproficencies=[]
        self.saveproficencies=[]

        self.attacks = []
        self.spells=[]
        self.featuresAndTraits = []
        self.languages= []
        self.proficencies=[]
        self.spellCastingAbility=""
        self.spellAttackBonus=0
        self.spellsaveDc=0

        self.Platinum=0
        self.gold=0
        self.electrum=0
        self.silver=0
        self.copper=0
        self.tresure=[]

        self.alliesAndOrginisations=[]


    def getPlayerName(self):
        return self.playerName
    def setPlayerName(self,name):
        self.playerName= name
    def getChatName(self):
        return self.charName 
    def setCharName(self,name):
        self.charName= name
    def getClass(self):
        return self.Class
    def setClass(self,Class):
        self.Class = Class
    def getLvl(self):
        return self.lvl
    def setLvl(self,lvl):
        self.lvl=lvl
    def getBackground(self):
        return self.background
    def setBackground(self,BkG):
        self.background=BkG
    def getRace(self):
        return self.race
    def setRace(self,Race):
        self.race=Race
    def getAlignment(self):
        return self.Alignment
    def setAlignment(self,Alng):    
        self.Alignment = Alng


    def getHP(self):
        return self.HP
    def addToHP(self,number):
        self.HP+= number
    def subFromHP(self,number):
        self.HP-= number

    def getTmpHP(self):
        return self.HP
    def addToTmpHP(self,number):
        self.HP+= number
    def subFromTmpHP(self,number):
        self.HP-= number
        self.temphp= 0
        self.AC = 0
        self.initiative = 0
        self.speed = 0
        self.hitdice=("",0)