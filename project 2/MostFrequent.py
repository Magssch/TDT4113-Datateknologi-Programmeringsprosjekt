from Player import Player
import random

class MostFrequent(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.opponent_rocks, self.opponent_papers, self.opponent_scissors = 0, 0, 0

    # chooses an action based on which action has been played the most. Random if none have been played.
    def choose_action(self):
        if self.opponent_rocks and self.opponent_papers and self.opponent_scissors == 0:
            return random.randint(0, 2)
        elif self.opponent_rocks > self.opponent_papers and self.opponent_rocks > self.opponent_scissors:
            return 0
        elif self.opponent_papers > self.opponent_rocks and self.opponent_papers > self.opponent_scissors:
            return 1
        elif self.opponent_scissors > self.opponent_rocks and self.opponent_scissors > self.opponent_papers:
            return 2

    # Classify the action.
    def receive_result(self, game):
        opponentAction = game.a2 if game.p1 == self else game.a1
        if opponentAction == 0:
            self.opponent_rocks += 1
        elif opponentAction == 1:
            self.opponent_papers += 1
        else:
            self.opponent_scissors += 1
