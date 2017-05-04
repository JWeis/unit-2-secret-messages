import string

from ciphers import Cipher

class Polybius(Cipher):
    ALPHA = string.ascii_uppercase

    def __init__(self):
        self.alph_list = alph_list = []
        key_nums = [11, 12, 13, 14, 15,
                    21, 22, 23, 24, 25,
                    31, 32, 33, 34, 35,
                    41, 42, 43, 44, 45,
                    51, 52, 53, 54, 55]

        for a in self.ALPHA:
            if a == 'I':
                a = "I/J"
            if a == "J":
                continue
            alph_list.append(a)

        self.enc_grid = {number: letter for letter, number in zip(alph_list, key_nums)}
        self.dec_grid = {letter: number for number, letter, in zip(key_nums, alph_list)}

        print('decrypt:',self.dec_grid ,'\n', 'encrypt:',self.enc_grid)




    def encrypt(self, text):
        text = text.upper()
        message_list = []
        output = []

        for char in text:
            message_list.append(char)

        for i in message_list:
            try:
                output.append(self.dec_grid[i])
            except KeyError:
                if i == 'I':
                    output.append(self.dec_grid['I/J'])
                elif i == "J":
                    output.append(self.dec_grid['I/J'])
                else:
                    continue
            else: KeyError

        return output

    def decrypt(self, num_list):
        message = ''
        for i in num_list:
            message += self.enc_grid[i]
        return message