import random
from bifid import Bifid
from polybius import Polybius
from word_cipher import WordCipher


CURRENT_KEY = '4612'

def one_time_pad():
    current_pad = random.randint(1, 5000)
    return current_pad


def keyword_enc(cipher):
    keyword = input("Choose a seceret keyword:  ")
    cipher = cipher(keyword)
    message = input("What is the message you would like to send? \n")
    encrypt = cipher.encrypt(message)
    print('your encrypted message is: ', encrypt)
    print('your one time pad to decrypt is: ', one_time_pad())
    return encrypt


def non_keyword_enc(cipher):
    cipher = cipher()
    message = input("What is the message you would like to send? \n")
    encrypt = cipher.encrypt(message)
    print('your encrypted message is: ', encrypt)
    print('your one time pad to decrypt is: ', one_time_pad())
    return encrypt


def keyword_dec(cipher):
    keyword = input("Choose a seceret keyword:  ")
    cipher = cipher(keyword)
    message = input("What is the message you would like to send? \n")
    decrypt = cipher.decrypt(message)
    return print(decrypt)


def non_keyword_dec(cipher):
    cipher = cipher()
    message = input("What is the message you would like to send? \n")
    decrypt = cipher.decrypt(message)
    return print(decrypt)


def app():
    pass_code = input("Enter the access token:  ")
    if pass_code ==  CURRENT_KEY:
        choose = input("Would you like to encrypt or decrypt a message? 1: Encrypt, 2: Decrypt  ")
        if choose == '1':
            cipher = input("Choose your cipher: 1: Word Cipher, 2: Polybius, 3: Bifid \n")
            if cipher == '1':
                keyword_enc(WordCipher)

            if cipher == '2':
                non_keyword_enc(Polybius)

            if cipher == '3':
                keyword_enc(Bifid)

        elif choose == '2':
            cipher = input("Which cipher to use: 1: Word Cipher, 2: Polybius, 3: Bifid \n")
            if cipher == '1':
                keyword_dec(WordCipher)

            if cipher == '2':
                non_keyword_dec(Polybius)

            if cipher == '3':
                keyword_dec(Bifid)

        else:
            print("You can only pick 1 or 2")
            app()
    else:
        print("You have entered thr wrong token: Good Bye")
        exit()

app()
