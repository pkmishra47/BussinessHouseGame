import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from bussinessHouseGame.models.hotel import Hotel
from bussinessHouseGame.models.jail import Jail
from bussinessHouseGame.models.player import Player
from bussinessHouseGame.models.treasure import Treasure

class BoardService:

    def __init__(self):
        self.__players = {}
        self.__hotels = {}
        self.__jails = None
        self.__treasures = None
    

    def GetPlayers(self):
        return self.__players

    def setPlayers(self, playersObj):
        self.__players = playersObj
    
    def setJails(self,list_of_jails):
        self.__jails = list_of_jails
    
    def setHotels(self,hotelsObj):
        self.__hotels = hotelsObj
    
    def setTreasures(self,list_of_treasures):
        self.__treasures = list_of_treasures

    def movePlayer(self,playerID,position):

        currentPosition = (self.__players[playerID]).getCurrentPosition()
        newPosition = currentPosition + position
        currentAmount = (self.__players[playerID]).getPlayerAmount()
        (self.__players[playerID]).setNewPosition(newPosition)

        print("Player with id " + str(playerID) + " and current position " + str(currentPosition) + " moving to new position " + str(newPosition))


        for jail in self.__jails:
            if newPosition == jail.getJailPosition():
                (self.__players[playerID]).addAmount(-1*jail.getFineAmount())
                print("Player with id " + str(playerID) + " has paid fine in jail.")
            
        for hotel in self.__hotels:
            if newPosition == self.__hotels[hotel].getHotelPosition():
                if self.__hotels[hotel].HasHotelOwner():
                    (self.__players[self.__hotels[hotel].GetHotelOwner()]).addAmount(self.__hotels[hotel].getRentAmount())
                    (self.__players[playerID]).addAmount(-1*self.__hotels[hotel].getRentAmount())
                    print("Player with id " + str(playerID) + " has paid rent to player " +  str(self.__hotels[hotel].GetHotelOwner()))
                elif currentAmount >= self.__hotels[hotel].getWorthPrice():
                    (self.__hotels)[hotel].SetHotelOwner(playerID)
                    (self.__players[playerID]).addAmount(-1*self.__hotels[hotel].getWorthPrice())
                    print("Player with id " + str(playerID) + " has become owner of hotel" )

        for treasure in self.__treasures:
            if newPosition == treasure.getTreasurePosition():
                (self.__players[playerID]).addAmount(treasure.getTreasureValue())




    