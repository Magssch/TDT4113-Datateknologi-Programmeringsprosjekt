import random
from Cipher import Cipher

class Caesar(Cipher):

    def encode(self, text, key):
        ntext = ''
        for i in range (0, len(text)):
            if self.alphabet[0] > ord(text[i]) > self.alphabet[1]: # Check if word is ascii-character, ignore if not
                continue
            ntext = ntext + chr(((ord(text[i]) - self.alphabet[0] + key) % self.alphabetLength()) + self.alphabet[0])
            # The encoding works as follows:
            # Take the ascii value minus lower limit of alphabet.
            # This ensures all numbers are in the interval [0, self.alphabetLength()-1]
            # Add to this the key/shift value
            # Use modulo of the length of the alphabet, this allows the algorithm to wrap around on too large numbers
            # Add value of lower limit of alphabet back to the result, in order to convert back into ascii
        return ntext

    def decode(self, text, key):
        return self.encode(text, -key) # Decode uses encode, with the key value negated

    # Generate keys, no point in using values outside [0, self.alphabetLength()] because of modulo-operator.
    def generate_keys(self):
        return random.randint(0, self.alphabetLength())

    # Returns all possible keys, up to alphabet length
    def possible_keys(self):
        return range(0, self.alphabetLength())

# Test-function:
if __name__ == '__main__':
    cipher = Caesar()
    print(Cipher.verify(cipher, 'abc test 123', 5))