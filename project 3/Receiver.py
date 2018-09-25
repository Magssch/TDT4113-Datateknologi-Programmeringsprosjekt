from Person import Person

class Receiver(Person):

    def operate_cipher(self, text):
        return self.get_cipher().decode(text, self.get_key())

