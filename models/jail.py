class Jail:
    def __init__(self,position):
        self.__position = position
        self.__fineAmount = 150
    
    def getFineAmount(self):
        return self.__fineAmount
    
    def getJailPosition(self):
        return self.__position
        