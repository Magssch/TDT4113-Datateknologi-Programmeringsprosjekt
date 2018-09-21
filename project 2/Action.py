class Action:

    def __init__(self, action):
        self.action = action

    # Overskriv er lik
    def __eq__(self, action):
        return self.action == action

    # Overskriv større enn
    def __gt__(self, action):
        return True if (
            (self.action == 0 and action == 1) or
            (self.action == 1 and action == 2) or
            (self.action == 2 and action == 0)
        ) else False
