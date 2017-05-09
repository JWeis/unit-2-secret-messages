from ciphers import Cipher
from polybius import Polybius
from word_cipher import WordCipher


class Bifid(Cipher):
    """Implements word Bifid cipher which is a combination of Transposition and Polybius ciphers."""

    def __init__(self, keyword):
        """Initiates class that takes a single string as a keyword argument.

        Creates an instance of WordCipher passing in the keyword as an argument.
        Creates an instance of Polybius.
        """
        self.keyword = keyword
        self.word_cipher = WordCipher(keyword)
        self.poly = Polybius()


    def encrypt(self, text):
        """Takes a single argument of text which is the message to be encrypted 

        Passes text to the instance of WordCipher encrypt method. 
        The returned value is passed to the instance of Polybius encrypt method. 
        Returns that value as the encryption. 
        """
        step_one = self.word_cipher.encrypt(text)
        step_two = self.poly.encrypt(step_one)

        return step_two

    def decrypt(self, enc_list):
        """Takes a single argument of enc_list which is the encrypted message. 

        Passes enc_list to the instance of Polybius decrypt method. 
        The returned value is passed to the instance of WordCipher decrypt method. 
        Returns that value as the decrypted message.  
        """
        step_one = self.poly.decrypt(enc_list)
        step_two = self.word_cipher.decrypt(step_one)

        return step_two
