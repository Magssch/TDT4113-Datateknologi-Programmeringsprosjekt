from Player import Player

# moves sequentially between actions.
class Sequential(Player):

    def __init__(self, name):
        Player.__init__(self, name)
        self.nextAction = 2

    def choose_action(self):
        self.nextAction += 1
        if self.nextAction > 2:
            self.nextAction = 0
        return self.nextAction