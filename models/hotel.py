class Hotel:
    def __init__(self, position):
        self.__position = position
        self.__worthprice = 200
        self.__rent = 50
        self.__OwnerID = None
    
    def getWorthPrice(self):
        return self.__worthprice
    
    def getRentAmount(self):
        return self.__rent
    
    def getHotelPosition(self):
        return self.__position
    
    def HasHotelOwner(self):
        if self.__OwnerID:
            return True
        else:
            return False
    
    def GetHotelOwner(self):
        return self.__OwnerID
    
    def SetHotelOwner(self,PlayerID):
        self.__OwnerID = PlayerID