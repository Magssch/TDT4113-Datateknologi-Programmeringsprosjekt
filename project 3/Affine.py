from Cipher import Cipher
from Caesar import Caesar
from Multiplication import Multiplication

class Affine(Cipher):

    # Uses both Multiplication and Caesar-cipher to encode/decode. Requires a list of length 2 for key-value
    def encode(self, plaintext, key):
        multi = Multiplication().encode(plaintext, key[1])
        return Caesar().encode(multi, key[0])


    def decode(self, text, key):
        multi = Caesar().decode(text, key[0])
        return Multiplication().decode(multi, key[1])

    # Generates a list of two keys
    def generate_keys(self):
        return (Multiplication().generate_keys(), Multiplication().generate_keys())

    def possible_keys(self):
        return Multiplication().possible_keys()

# Test methods
if __name__ == '__main__':
    cipher = Affine()
    print(Cipher.verify(cipher, 'abc test 123', cipher.generate_keys()))