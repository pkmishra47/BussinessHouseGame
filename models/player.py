class Player:
    def __init__(self,playerName,playerID):
        self.__amount = 1000
        self.__name = playerName
        self.__playerID = playerID
        self.__CurrentPosition = 0
    
    def getPlayerID(self):
        return self.__playerID

    def getPlayerName(self):
        return self.__name
    
    def getPlayerAmount(self):
        return self.__amount
    
    def getAmount(self):
        return self.__amount
    
    def addAmount(self, amount):
        self.__amount += amount
    
    def getCurrentPosition(self):
        return self.__CurrentPosition
    
    def setNewPosition(self,NewPosition):
        self.__CurrentPosition = NewPosition