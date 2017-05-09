import random
from bifid import Bifid
from polybius import Polybius
from word_cipher import WordCipher


CURRENT_KEY = ''
COUNTER = 0


def one_time_pad():
    used_keys = []
    current_pad = random.randint(1, 500)
    if current_pad not in used_keys:
        used_keys.append(current_pad)
        return current_pad
    elif current_pad in used_keys:
        one_time_pad()
    else:
        return print("Cipher has used all its generated one time keys")


def end_app():
    end_cipher = input("Choose 1 to End Cipher, or 2 to Run Cipher Again:  ")
    if end_cipher == '1':
        exit()
    elif end_cipher == '2':
        app()


def keyword_enc(cipher):
    keyword = input("Please enter a secret keyword - only letters please:  ")
    cipher = cipher(keyword)
    message = input("\nWhat message would like to Encrypt? \n")
    encrypt = cipher.encrypt(message)
    pad = one_time_pad()
    print("\nYour encrypted message is: \n", encrypt, '\n')
    print("Your one time pad to decrypt is: \n", str(pad), '\n')
    print("The secret keyword is: \n", keyword, '\n')
    print("The cipher used to encrypt this message was \n", cipher, '\n\n')
    print("Be sure to share the encrypted message, keyword, and cipher used to whom the message is intended for...\n\n")
    global CURRENT_KEY
    CURRENT_KEY = str(pad)
    return encrypt


def non_keyword_enc(cipher):
    cipher = cipher()
    message = input("\nWhat is the message you would like to send? \n")
    encrypt = cipher.encrypt(message)
    pad = one_time_pad()
    print("\nYour encrypted message is: \n", encrypt, '\n')
    print("Your one time pad to decrypt is: \n", str(pad), '\n')
    print("The cipher used to encrypt this message was \n", cipher, '\n\n')
    print("Be sure to share the encrypted message, keyword, and cipher used to whom the message is intended for...\n\n")
    global CURRENT_KEY
    CURRENT_KEY = str(pad)
    return encrypt


def keyword_dec(cipher):
    keyword = input("\nPlease enter the secret keyword to decrypt your message:  ")
    cipher = cipher(keyword)
    message = input("\nPlease enter the encrypted message \n")
    decrypt = cipher.decrypt(message)
    print("\n Your decrypted message is: \n", decrypt, '\n\n')
    return decrypt


def non_keyword_dec(cipher):
    cipher = cipher()
    message = input("\nPlease enter the encrypted message \n")
    decrypt = cipher.decrypt(message)
    print("\n Your decrypted message is: \n", decrypt, '\n\n')
    return decrypt


def app():
    global COUNTER
    print(COUNTER)
    if COUNTER < 1:
        pass_code = input("Since it is your fist time - please press ENTER to continue")
    else:
        pass_code = input("Please enter the one time pad key:  ")

    if pass_code == CURRENT_KEY:
        if COUNTER < 1:
            choose = input("To Encrypt your first message please type 1:  ")
        else:
            choose = input("Would you like to encrypt or decrypt a message? 1: Encrypt, 2: Decrypt  ")

        if choose == '1':
            cipher = input("Choose your cipher: 1: WordCipher, 2: Polybius, 3: Bifid \n")
            if cipher == '1':
                keyword_enc(WordCipher)
                COUNTER += 1
                end_app()

            if cipher == '2':
                non_keyword_enc(Polybius)
                COUNTER += 1
                end_app()

            if cipher == '3':
                keyword_enc(Bifid)
                COUNTER += 1
                end_app()

        elif choose == '2':
            cipher = input("Which cipher to use: 1: Word Cipher, 2: Polybius, 3: Bifid \n")
            if cipher == '1':
                keyword_dec(WordCipher)
                end_app()

            if cipher == '2':
                non_keyword_dec(Polybius)
                end_app()

            if cipher == '3':
                keyword_dec(Bifid)
                end_app()

        else:
            print("You can only pick 1 or 2")
            app()
    else:
        print("You have entered thr wrong one time pad: Good Bye")
        exit()

app()
