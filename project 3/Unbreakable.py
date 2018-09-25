import random

from Cipher import Cipher

class Unbreakable(Cipher):

    # Encodes a text by using a word rather than a numerical key.
    def encode(self, plaintext, key):
        ciphertext = ""
        for i in range(0, len(plaintext)):
            ciphertext = ciphertext + chr(((ord(plaintext[i]) + ord(key[(i % len(key))]) - (self.alphabet[0]*2))
                                           % self.alphabetLength()) + self.alphabet[0])
        return ciphertext

    # Similar to encode() but using some fancy modular mathematics to get a decoded string.
    def decode(self, text, key):
        newKey = ''
        for char in key:
            newKey = newKey + chr((self.alphabetLength() - ((ord(char)-self.alphabet[0])
                                                            % self.alphabetLength())) + self.alphabet[0])
        return self.encode(text, newKey)

    # Chooses a random word/key in the english dictionary
    def generate_keys(self):
        file = open("english_words.txt", 'r')
        dict = file.read()
        dictWords = list(dict.split('\n'))
        file.close()
        return dictWords[random.randint(0, len(dictWords)-1)]

    # Possible keys must be in the english dictionary
    def possible_keys(self):
        file = open("english_words.txt", 'r')
        dict = file.read()
        dictWords = list(dict.split('\n'))
        file.close()
        return dictWords

# Test method
if __name__ == '__main__':
    cipher = Unbreakable()
    print(Cipher.verify(cipher, 'abc test 123', cipher.generate_keys()))