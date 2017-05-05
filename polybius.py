import string

from ciphers import Cipher

class Polybius(Cipher):
    ALPHA = string.ascii_uppercase

    def __init__(self):
        self._alph_list = []
        self._key_nums = [11, 12, 13, 14, 15,
                          21, 22, 23, 24, 25,
                          31, 32, 33, 34, 35,
                          41, 42, 43, 44, 45,
                          51, 52, 53, 54, 55,
                          56]

        for a in self.ALPHA:
            self._alph_list.append(a)

        self.enc_grid = {number: letter for letter, number in zip(self._alph_list, self._key_nums)}
        self.dec_grid = {letter: number for number, letter, in zip(self._key_nums, self._alph_list)}

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
                if i not in self.dec_grid:
                    output.append(10)
                else:
                    continue
            else: KeyError

        blocks = [output[i:i + 5] for i in range(0, len(output), 5)]

        return blocks

    def decrypt(self, num_list):
        message = ''
        holder_list = []

        for i in num_list:
            holder_list = i
            for a in holder_list:
                if a not in self.enc_grid:
                    message += ''
                else:
                    message += self.enc_grid[a]
                    holder_list = []

        blocks = ' '.join(message[i:i + 5] for i in range(0, len(message), 5))

        return blocks


