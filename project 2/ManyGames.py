from matplotlib import pyplot as plot
from Game import *
from Random import *
from Sequential import *
from MostFrequent import *
from Historian import *


class ManyGames:

    # Setup game
    def __init__(self):
        self.p1 = self.setupPlayer(True)
        self.p2 = self.setupPlayer(False)
        self.num_games = int(input("Velg hvor mange spill som skal spilles: "))
        self.p1_wins = 0
        self.p2_wins = 0

    # Runs a single game, saving the score of p1 and p2
    def run_game(self):
        game = Game(self.p1, self.p2)
        game.play_game()
        if game.winner == self.p1:
            self.p1_wins+=1
        elif game.winner == self.p2:
            self.p2_wins += 1
        else:
            self.p1_wins += 0.5
            self.p2_wins += 0.5
        return str(game)


    # Starts a tournament, runs an amount of games, and then plots the result.
    def tournament(self):
        win_percentage = []
        round = 0
        while round < self.num_games:
            print(self.run_game())
            win_percentage.append(self.p1_wins / (self.p1_wins + self.p2_wins))
            round += 1

        plot.ylabel('Gevinst')
        plot.xlabel('Antall spill')
        plot.ylim(0,1)
        plot.plot(win_percentage)
        plot.show()

    # Initializes a player
    def setupPlayer(self, isPlayer1):
        if(isPlayer1):
            name = input("Hva heter spiller 1? ")
        else:
            name = input("Hva heter spiller 2? ")
        while True:
            ptype = int(input("Velg spillertype: (Skriv 1 for Tilfeldig, 2 for Sekvensiell, 3 for Mest vanlig og 4 for Historiker) "))
            if ptype == 1:
                player = Random(name)
                break
            elif ptype == 2:
                player = Sequential(name)
                break
            elif ptype == 3:
                player = MostFrequent(name)
                break
            elif ptype == 4:
                memory = int(input("Velg antall ledd i minnet til Historian: "))
                player = Historian(name, memory)
                break
            else:
                print("Den spillertypen finnes ikke. (velg fra 1-4)")
        return player

# Runs the class if the script is executed and not imported.
if __name__ == '__main__':
    game = ManyGames()
    game.tournament()





















