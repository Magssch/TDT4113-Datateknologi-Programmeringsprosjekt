from Person import Person

class Sender(Person):

    def operate_cipher(self, text):
        return self.get_cipher().encode(text, self.get_key())

