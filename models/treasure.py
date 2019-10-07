class Treasure:
    def __init__(self,position):
        self.__position = position
        self.__value = 200
    
    def getTreasureValue(self):
        return self.__value
    
    def getTreasurePosition(self):
        return self.__position