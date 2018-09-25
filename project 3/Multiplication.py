import random
import math
from crypto_utils import modular_inverse
from Cipher import Cipher

class Multiplication(Cipher):

    # Similar to Caesar-cipher, but multiplies the value with a key, instead of adding to it.
    def encode(self, text, key):
        ntext = ''
        for i in range (0, len(text)):
            if self.alphabet[0] > ord(text[i]) > self.alphabet[1]:
                continue
            ntext = ntext + chr((((ord(text[i]) * key) - self.alphabet[0]) % self.alphabetLength()) + self.alphabet[0])
        return ntext

    # In order to reverse encoding, use encode() with a modular inverse of the key
    def decode(self, text, key):
        return self.encode(text, modular_inverse(key, self.alphabetLength()))


    # Generate a key that has no gcd > 1 with the length of the alphabet
    def generate_keys(self):
        n = random.randint(0, self.alphabetLength())
        while True:
            if not math.gcd(n, self.alphabetLength()) == 1:
                n = random.randint(0, self.alphabetLength())
            else:
                return n

    # Generate a list of keys that has no gcd > 1 with the length of the alphabet
    def possible_keys(self):
        keys = []
        for i in range(0, self.alphabetLength()):
            if math.gcd(i, self.alphabetLength()) == 1:
                keys.append(i)
        return keys

# Test method
if __name__ == '__main__':
    cipher = Multiplication()
    print(Cipher.verify(cipher, 'abc test 123', cipher.generate_keys()))