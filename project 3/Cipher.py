
#   Superclass for ciphers. Defines the start and end of ascii-characters (self.alphabet), as well as
#   the length of that alphabet. Also defines a static verify-method, to be used for testing purposes.

class Cipher:

    def __init__(self):
        self.alphabet = [32, 126]

    def encode(self, plaintext, key):
        pass

    def decode(self, ciphertext, key):
        pass

    def generate_keys(self):
        pass

    def alphabetLength(self):
        return self.alphabet[1]-self.alphabet[0]+1

    def possible_keys(self):
        pass

    @staticmethod
    def verify(self, plaintext, key): return plaintext == self.decode(self.encode(plaintext, key), key)
