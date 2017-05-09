import string
from ciphers import Cipher


class Polybius(Cipher):
    ALPHA = string.ascii_uppercase

    def __init__(self):
        self.alpha_list = []
        self.key_nums = ['11', '12', '13', '14', '15', '21', '22', '23', '24', '25', '31', '32', '33', '34', '35', '41', '42', '43', '44',
                         '45', '51', '52', '53', '54', '55', '56']
        for a in self.ALPHA:
            self.alpha_list.append(a)
        self.enc_grid = {number: letter for letter, number in zip(self.alpha_list, self.key_nums)}
        self.dec_grid = {letter: number for number, letter, in zip(self.key_nums, self.alpha_list)}
        self.num_grid = ['0', '1', '2', '3', '4', '5', '6', '7','8', '9']

    def encrypt(self, text):
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
        #blocks = ' '.join(output[i:i + 5] for i in range(0, len(output), 5))
        return output

    def decrypt(self, num_list):
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

