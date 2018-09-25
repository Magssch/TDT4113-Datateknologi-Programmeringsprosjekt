from Receiver import Receiver
from Caesar import Caesar
from Multiplication import Multiplication
from Affine import Affine
from Unbreakable import Unbreakable
import time

class Hacker(Receiver):

    def __init__(self, cipher = None):
        super(Hacker, self).__init__(cipher)

        # Reads and saves english dictionary as a set.
        file = open("english_words.txt", 'r')
        dictList = file.read()
        self.dict = set(dictList.split('\n'))
        file.close()


    def hack(self, text, cipher = None):

        if not cipher == None:
            self.set_cipher(cipher)

        if isinstance(cipher, Unbreakable):
            for word in cipher.possible_keys():
                if(len(word) < 1):  # Avoiding empty lines in dictionary
                    continue
                self.set_key(word)
                decrypt = self.bruteForce(text)
                if not decrypt == None:
                    return decrypt
        else:
            for key in cipher.possible_keys():
                if isinstance(cipher, Affine):  # Sets a second set of keys, if cipher is Affine
                    second_keys = cipher.possible_keys()
                    isAffine = True
                else:
                    second_keys = range(1)  # Ensures nested for-loop is only run once, if there is only one key
                    isAffine = False

                for second_key in second_keys:
                    if isAffine:
                        self.set_key([key, second_key])
                    else:
                        self.set_key(key)   # Only run once, if cipher is not Affine

                    decrypt = self.bruteForce(text)
                    if not decrypt == None:
                        return decrypt

    # Common bruteforce decryption method for Ceasar, Multiplication, Affine, and Unbreakable with minor alterations
    # between the different encryption algorithms.
    def bruteForce(self, text):
        decrypted = self.operate_cipher(text)
        if isinstance(self.get_key(), str):
            print("Testing key \'" + self.get_key() + "\', output text: \"" + decrypted + "\"")
        else:
            print("Testing key " + str(self.get_key()) + ", output text: \"" + decrypted + "\"")
        decrypted_words = decrypted.split()
        isPlaintext = True
        for word in decrypted_words:    # Checks if word is in english dictionary.
            if not word in self.dict:
                isPlaintext = False     # One mismatched word is enough to exclude from further investigation
                break
        if isPlaintext:
            return decrypted            # Return text if all words are matched with english dictionary
        else:
            return None                 # Fallback if anything goes wrong ;-)


# Test methods
if __name__ == '__main__':

    #Tests Ceasar-cipher
    print("Test: Cracking a Caesar-cipher:\n")
    time.sleep(2)
    cipher = Caesar()
    hacker = Hacker()
    print("\nDecrypted text found: \"" + hacker.hack(cipher.encode("this is a test", cipher.generate_keys()), cipher) + "\"\n")
    time.sleep(1)

    #Tests Multiplication-cipher
    print("Test: Cracking a Multiplication-cipher:\n")
    time.sleep(2)
    cipher = Multiplication()
    print("\nDecrypted text found: \"" + hacker.hack(cipher.encode("this is a second test", cipher.generate_keys()), cipher) + "\"\n")
    time.sleep(1)

    #Tests Affine-cipher
    print("Test: Cracking an Affine-cipher:\n")
    time.sleep(2)
    cipher = Affine()
    print("\nDecrypted text found: \"" + hacker.hack(cipher.encode("this is a third test", cipher.generate_keys()), cipher) + "\"\n")
    time.sleep(1)

    #Tests Unbreakable-cipher
    print("Test: Cracking an Unbreakable-cipher:\n")
    time.sleep(2)
    cipher = Unbreakable()
    print("\nDecrypted text found: \"" + hacker.hack(cipher.encode("this is too easy", cipher.generate_keys()), cipher) + "\"\n")