import string

from ciphers import Cipher

class WordCipher(Cipher):
    ALPHA = string.ascii_uppercase

    def __init__(self, keyword):
        self.keyword = keyword
        word = keyword.upper()
        self.plaintext = plaintext = []
        self.keyword_list = keyword_list = []
        self.new_list = new_list = []
        for i in self.ALPHA:
            plaintext.append(i)

        for i in word:
            keyword_list.append(i)

        for i in plaintext:
            if i not in keyword_list:
                new_list.append(i)


        self.enc_grid = enc_grid = {number: letter for letter, number in zip(keyword_list, new_list)}
        self.dec_grid = dec_grid = {letter: number for number, letter, in zip(new_list, keyword_list)}


    def encrypt(self, text):
        text = text.upper()
        output = ''

        for char in text:
            try:
                output += self.dec_grid[char]
            except KeyError:
                if char not in self.dec_grid:
                    output.append(' ')
                else:
                    continue
            else: KeyError

        return output




