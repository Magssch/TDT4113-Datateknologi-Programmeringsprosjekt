from Player import Player
import random

# randomly chooses an action, using randint between 0 and 2
class Historian(Player):

    def __init__(self, name, memory):
        Player.__init__(self, name)
        self.memory = memory
        self.history = []

    def choose_action(self):
        count = [0,     0,      0]
        #        ^rock  ^paper  ^scissor

        winningAction = [2,
        #                ^ rock beats scissor
                         0,
        #                ^ paper beats rock
                         1]
        #                ^ scissor beats paper

        if(self.memory > len(self.history)): # if not enough games have been played yet, do random
            return random.randint(0,2)
        else:
            last = self.history[-self.memory:] # Slices history from the end to 'memory'-steps backwards.
                                               # This subsequence may vary in length
            for i in range(0, len(self.history) - self.memory): # Loops through history
                if last == self.history[i:i +self.memory]:  # if a matching subsequence is found
                    if(self.history[(i+self.memory)] == None):
                        count[2] += 1                           # default
                    else:
                        count[self.history[(i+self.memory)]] += 1 # increase count of rock, paper or scissors respectively
            return winningAction[count.index(max(count))]    # Return the action with the highest count

    def receive_result(self, game):
        self.history.append(game.a2 if game.p1 == self else game.a1)

