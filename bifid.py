from ciphers import Cipher
from polybius import Polybius
from word_cipher import WordCipher


class Bifid(Cipher):
    def __init__(self, keyword):
        self.keyword = keyword
        self.word_cipher = WordCipher(keyword)
        self.poly = Polybius()


    def encrypt(self, text):
        step_one = self.word_cipher.encrypt(text)
        step_two = self.poly.encrypt(step_one)
        return step_two

    def decrypt(self, enc_list):
        step_one = self.poly.decrypt(enc_list)
        step_two = self.word_cipher.decrypt(step_one)
        return step_two
