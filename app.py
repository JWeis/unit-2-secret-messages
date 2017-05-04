from polybius import Polybius

enc = Polybius()

def main():
    test = input(">> what do you want to encrypt?: ")

    return enc.encrypt(test)


if __name__ == "__main__":
    main()