
#   Superclass for Receiver, Sender and Hacker

class Person:

    def __init__(self, cipher = None):
        self.key = None
        self.cipher = cipher

    def set_key(self, key):
        self.key = key

    def get_key(self):
        return self.key

    def set_cipher(self, cipher):
        self.cipher = cipher

    def get_cipher(self):
        return self.cipher

    def operate_cipher(self, text):
        pass

