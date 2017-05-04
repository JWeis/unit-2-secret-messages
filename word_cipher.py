import string

from ciphers import Cipher

class WordCipher(Cipher):
    ALPHA = string.ascii_uppercase

    def __init__(self, keyword):
        self.keyword = keyword
        self.word = keyword.upper()
        self.plaintext = plaintext = []
        self.keyword_list = keyword_list = []
        self.place_list = place_list = []

        for i in self.ALPHA:
            plaintext.append(i)

        for i in self.word:
            keyword_list.append(i)

        for i in plaintext:
            if i not in keyword_list:
                place_list.append(i)

        self.new_list = new_list = keyword_list + place_list


        self.enc_grid = enc_grid = {number: letter for letter, number in zip(plaintext, new_list)}
        self.dec_grid = dec_grid = {letter: number for number, letter, in zip(new_list, plaintext)}


    def encrypt(self, text):
        text = text.upper()
        output = ''

        for char in text:
            try:
                output += self.dec_grid[char]
            except KeyError:
                if char not in self.dec_grid:
                    output += ' '
                else:
                    continue
            else: KeyError

        return output

    def decrypt(self, text):
        message = ''
        for i in text:
            try:
                message += self.enc_grid[i]
            except KeyError:
                if i not in self.enc_grid:
                    message += ' '
            else: KeyError

        return message




