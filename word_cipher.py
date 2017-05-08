import string
from ciphers import Cipher


class WordCipher(Cipher):
    ALPHA = string.ascii_uppercase

    def __init__(self, keyword):
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

    def cipher_list(self):
        return self.new_list
