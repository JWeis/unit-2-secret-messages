import string
from ciphers import Cipher


class Polybius(Cipher):
    """Implements word Polybius Square cipher using upper case english alphabet."""
    ALPHA = string.ascii_uppercase

    def __init__(self):
        """Initiates class with no arguments.
        
        Two dictionaries are created with opposite key value pairs. One to encrypt, and the other to decrypt.
        Dictionaries are paired with a string number and a letter.
        Lastly a number list is created with string numbers from 0 - 9 to be used to check against.
        """
        self.alpha_list = []
        self.key_nums = ['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44',
                         '45', '51', '52', '53', '54', '55', '56']

        for a in self.ALPHA:
            self.alpha_list.append(a)

        self.enc_grid = {number: letter for letter, number in zip(self.alpha_list, self.key_nums)}
        self.dec_grid = {letter: number for number, letter, in zip(self.key_nums, self.alpha_list)}
        self.num_grid = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']

    def encrypt(self, text):
        """Takes a single argument of text which is the message to be encrypted 

        Each item of text is check against num_grid, and dec_grid from initialization. If the value of the item
        in text matches in either, the value or value of key is appended to the output variable. 
        If there is no match the item is ignored. Output is a series of numbers that separated by a space.
        """
        text = text.upper()
        message_list = []
        output = ''

        for char in text:
            message_list.append(char)

        for i in message_list:
            if i in self.num_grid:
                output += i + ' '
            elif i not in self.dec_grid:
                output += ''
            else:
                output += self.dec_grid[i] + ' '

        return output

    def decrypt(self, num_list):
        """Takes a single argument of num_list which is the encrypted message. 

        Each item of text is check against num_grid, and enc_grid from initialization. If the value of the item
        in text matches in either, the value or volue of key is appended to the output variable. 
        If there is no match the item is ignored. 
        Message is then manipulated to be organized in five letter blocks and then returned.
        """
        message = ''
        holder_list = num_list.split()

        for i in holder_list:
            if i in self.num_grid:
                message += i
            elif i not in self.enc_grid:
                message += ''
            else:
                message += self.enc_grid[i]

        blocks = ' '.join(message[i:i + 5] for i in range(0, len(message), 5))

        return blocks
