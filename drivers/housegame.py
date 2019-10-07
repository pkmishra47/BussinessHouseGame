import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from bussinessHouseGame.services.board import BoardService
from bussinessHouseGame.models.jail import Jail
from bussinessHouseGame.models.hotel import Hotel
from bussinessHouseGame.models.treasure import Treasure
from bussinessHouseGame.models.player import Player

class HouseGame:

    def __init__(self):
        pass

    def start_game(self):
        boardservice =  BoardService()

        cell_positions = "E,E,J,H,E,T,J,T,E,E,H,J,T,H,E,E,J,H,E,T,J,T,E,E,H,J,T,H,J,E,E,J,H,E,T,J,T,E,E,H,J,T,E,H,E"
        list_of_places = cell_positions.split(',')
        dice_output = "4,4,4,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12,2,3,5,6,7,8,5,11,10,12"
        list_of_jails = []
        hotels = {}
        list_of_treasures = []
        players = {}
        players_turn = []

        for i in range(len(list_of_places)):
            if list_of_places[i] == 'J':
                list_of_jails.append(Jail(i+1))
            if list_of_places[i] == 'H':
                hotels[i+1] = Hotel(i+1)
            if list_of_places[i] == 'T':
                list_of_treasures.append(Treasure(i+1))

        boardservice.setHotels(hotels)
        boardservice.setJails(list_of_jails)
        boardservice.setTreasures(list_of_treasures)

        for i in range(3):
            players[i+1] = Player("Player" + str(i+1),i+1)
            players_turn.append(i+1)
        
        boardservice.setPlayers(players)

        for dice_val in dice_output.split(','):
            playerID = players_turn.pop(0)

            boardservice.movePlayer(playerID,int(dice_val))
            players_turn.append(playerID)

        winner_player = None
        players = boardservice.GetPlayers()

        max_amount = -9999999
        for player in players:
            print("player " + str(player) + " Amount: " + str(players[player].getAmount()))
            if players[player].getAmount() > max_amount: 
                max_amount = players[player].getAmount()
                winner_player = players[player]

        print("Winner player is " + winner_player.getPlayerName() + " and has total amount : " + str(winner_player.getPlayerAmount())) 

if __name__ == '__main__':
    housegame = HouseGame()
    housegame.start_game()
