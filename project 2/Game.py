from Action import Action

class Game:

    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2
        self.winner, self.a1, self.a2 = None, None, None

    #Runs a game
    def play_game(self):
        self.a1, self.a2 = self.p1.choose_action(), self.p2.choose_action()

        # Send the actions played to the players (for MostFrequent og Historian)
        self.p1.receive_result(self)
        self.p2.receive_result(self)

        # Make a1,a2, that are actions, into Action-objects that can be compared
        a1, a2 = Action(self.a1), Action(self.a2)

        # Choose the winner
        if a1 == a2:
            return
        elif a1 > a2:
            self.winner = self.p1
        else:
            self.winner = self.p2

    # print action
    @staticmethod
    def print_action(a):
        if a == 0:
            return "Rock"
        elif a == 1:
            return "Paper"
        elif a == 2:
            return "Scissor"
        else:
            return "N/A"

    # toString-method
    def __str__(self):
        text = "Player "+self.p1.name+" used " + self.print_action(self.a1) + "\n" + "Player "+self.p2.name+" used" +\
               self.print_action(self.a2) + "\n"
        if self.winner is None:
            return text+"It was a draw"
        elif self.winner == self.p1:
            return text+"Player "+self.p1.name+"  won!"
        else:
            return text+"Player "+self.p2.name+"  won!"