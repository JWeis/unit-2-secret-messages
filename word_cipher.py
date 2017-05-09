import string
from ciphers import Cipher


class WordCipher(Cipher):
    """Implements word transposition cipher using upper case english alphabet."""
    ALPHA = string.ascii_uppercase

    def __init__(self, keyword):
        """Takes a single string as a keyword to be used in setting up encryption.
        
        A List is created of letters that are transposition based on the keyword.
        Two dictionaries are created with opposite key value pairs. One to encrypt, and the other to decrypt. 
        Lastly a number list is created with string numbers from 0 - 9 to be used to check against.
        """
        self.keyword = keyword
        self.word = keyword.upper()
        self.plaintext = []
        self.keyword_list = []
        self.place_list = []

        for i in self.ALPHA:
            self.plaintext.append(i)

        for i in self.word:
            self.keyword_list.append(i)

        for i in self.plaintext:
            if i not in self.keyword_list:
                self.place_list.append(i)

        self.new_list = self.keyword_list + self.place_list
        self.enc_grid = {number: letter for letter, number in zip(self.plaintext, self.new_list)}
        self.dec_grid = {letter: number for number, letter, in zip(self.new_list, self.plaintext)}
        self.num_grid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def encrypt(self, text):
        """Takes a single argument of text which is the message to be encrypted 
        
        Each item of text is check against num_grid, and dec_grid from initialization. If the value of the item
        in text matches in either, the value or value of key is appended to the output variable. If there is no match the item 
        is ignored. Output is then manipulated to be organized in five letter blocks and then returned.
        """
        text = text.upper()
        output = ''

        for char in text:
            if char in self.num_grid:
                output += char
            elif char not in self.dec_grid:
                output += ''
            else:
                output += self.dec_grid[char]

        blocks = ' '.join(output[i:i+5] for i in range(0, len(output), 5))

        return blocks

    def decrypt(self, text):
        """Takes a single argument of text which is the encrypted message. 
        
        Each item of text is check against num_grid, and enc_grid from initialization. If the value of the item
        in text matches in either, the value is appended to the output variable. If there is no match the item 
        is ignored. Output is then manipulated to be organized in five letter blocks and then returned.
        """
        text = text.upper()
        message = ''

        for i in text:
            if i in self.num_grid:
                message += i
            elif i not in self.enc_grid:
                message += ''
            else:
                message += self.enc_grid[i]

        blocks = ' '.join(message[i:i + 5] for i in range(0, len(message), 5))

        return blocks
