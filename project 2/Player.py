__author__ = 'Magssch'

#Superclass for different player types
class Player:

    def __init__(self, name):
        self.name = name

    def choose_action(self):
        pass

    def receive_result(self, game):
        pass

    def getName(self):
        return type(self)

