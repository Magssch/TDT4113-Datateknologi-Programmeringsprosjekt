from Player import Player
import random

# randomly chooses an action, using randInt between 0 and 2
class Random(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def choose_action(self):
        return random.randint(0, 2)