from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import secrets
import string
import base64
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def decrypt(encrypted_base64):
    key = "s4$t%%2rW@kL9&xZ"
    key = key.encode('utf-8')
    encrypted_data = base64.b64decode(encrypted_base64)
    iv = encrypted_data[:AES.block_size]
    encrypted = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted)
    decrypted = unpad(decrypted_padded, AES.block_size)
    return decrypted.decode('utf-8')


# function used a random word from a chosen theme text file
def word_extractor(filename):
    os.system('cls')
    file_path = os.path.join(script_dir, 'database', filename)
    with open(file_path) as f:
        wordlist = []
        for line in f:
            wordlist.append(line.strip())

    word1 = random.choice(wordlist)
    word2 = decrypt(word1)
    word = word2.lower()
    return word

# function that automatically outputs the possible options
def file_checker():
    #function the retrieves the file names
    def file_name_retriever():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        target_folder = os.path.join(script_dir, 'database')
        files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))]
        return files
    file_names = file_name_retriever()
    #removes the .txt from the end
    options = [os.path.splitext(f)[0] if f.endswith('.txt') else f for f in file_names]

    # replaces a dash in the file name with a space
    def dash_remover(word_in_options):
        string1 = ''
        for item in word_in_options:
            if item == '-':
                string1 = string1 + " "
            else:
                string1 = string1 + item
        return string1

    f = 0
    for item in options:
        replacement = dash_remover(item)
        options[f] = replacement
        f += 1

    while True:
        count = 0
        print("______________________________________")
        for item in options:
            count += 1
            print(f"{count}: {item.title()}")
        print("______________________________________")
        try:
            hangchoice = int(input(">"))
            if hangchoice > 0 and hangchoice <= count:
                selected_file = file_names[hangchoice - 1]
                return selected_file
            elif hangchoice == -1:
                return 'quit'
            else:
                print("____________________________________")
                tchoice = input("Invalid Input")
                print("____________________________________")
                os.system('cls')
                print("ENTER -1 TO QUIT")
        except:
            print("____________________________________")
            tchoice = input("Invalid Input")
            print("____________________________________")
            os.system('cls')
            print("ENTER -1 TO QUIT")


#the main hangman game
def main():
    continuechk = True
    while continuechk == True:
        os.system('cls')
        option = file_checker()
        if option == 'quit':
            continuechk = False
        else:
            # sends choice to word_extractor and return a random word from chosen file
            word = word_extractor(option)
            wordarr = [None] * (len(word))
            blankarr = [None] * (len(word))
            blankarr1 = [None] * (len(word))
            blank2arr = []
            blank1 = '_' * (len(word))
            blank = blank1
            # hangman diagrams
            def chance_printer(chances):
                def chance_printer2(chancearr):
                    for item in chancearr:
                        print(item)

                chancearr6 = ['     ______ ', "    |      |", '           |', '           |', '           |', '   ---------']
                chancearr5 = ['     ______ ', "    |      |", '    O      |', '           |', '           |', '   ---------']
                chancearr4 = ['     ______ ', "    |      |", '    O      |', '    |      |', '           |', '   ---------']
                chancearr3 = ['     ______ ', "    |      |", '    O      |', '   /|      |', '           |', '   ---------']
                chancearr2 = ['     ______ ', "    |      |", '    O      |', '   /|\     |', '           |', '   ---------']
                chancearr1 = ['     ______ ', "    |      |", '    O      |', '   /|\     |', '   /       |', '   ---------']
                chancearr0 = ['     ______ ', "    |      |", '    O      |', '   /|\     |', '   / \     |', '   ---------']
                if chances == 6:
                    chance_printer2(chancearr6)
                elif chances == 5:
                    chance_printer2(chancearr5)
                elif chances == 4:
                    chance_printer2(chancearr4)
                elif chances == 3:
                    chance_printer2(chancearr3)
                elif chances == 2:
                    chance_printer2(chancearr2)
                elif chances == 1:
                    chance_printer2(chancearr1)
                elif chances == 0:
                    chance_printer2(chancearr0)

            for x in range(0, (len(word))):
                blankarr[x] = blank[x]
            for x in range(0, (len(word))):
                wordarr[x] = word[x]

            repeated = [None]
            repeated.remove(None)

            # used to add the punctuations and numbers to the blanks
            punct = [' ', "'", '"', '-', ':', ';', ',', '.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            p = 0
            for letter in word:
                if letter in punct:
                    blankarr[p] = letter
                p = p + 1

            # the game begins here
            # the game runs until the user runs out of chances or completes the game
            completion = False
            chances = 6
            while ((chances > 0) and (completion == False)):

                blanknonarr = ''
                for z in range(0, len(blankarr)):
                    blanknonarr = blanknonarr + blankarr[z]

                # adds spaces to the blanks output
                blank2 = ''
                for item in blanknonarr:
                    blank2 = blank2 + item
                    blank2 = blank2 + ' '
                blank2arr = []
                for item in blank2:
                    blank2arr.append(item)
                blank2arr.pop()
                blank3 = ''
                for item in blank2arr:
                    blank3 = blank3 + item

                print(f'[{blank3}]')
                guess1 = input("Guess a letter: ")
                guess = guess1.lower()
                if len(guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyz':
                    rep = False
                    if guess not in repeated:
                        for g in range(0, (len(word))):
                            blankarr1[g] = blankarr[g]
                        y = 0
                        for letter in word:
                            if letter == guess:
                                blankarr[y] = letter
                            y = y + 1
                        if blankarr == wordarr:
                            completion = True
                        if blankarr1 == blankarr:
                            chances = chances - 1
                            os.system('cls')
                            print("INCORRECT")
                        else:
                            os.system('cls')
                            print("CORRECT")

                        repeated.append(guess)
                    else:
                        os.system('cls')
                        print("LETTER ALREADY ATTEMPTED")
                else:
                    os.system('cls')
                    print(f"[{guess}] is an invalid input. Single letters only")

                print(f'Attempted letters: {repeated}')
                chance_printer(chances)

            os.system('cls')
            if chances == 0 and completion == False:
                print("YOU COULDNT GUESS THE WORD")
                chance_printer(0)
            elif chances > 0 and completion == True:
                print("CONGRATULATIONS ON GUESSING THE WORD!!!!")
                chance_printer(chances)
            print("THE WORD WAS:")
            print(f'[{word}]')

            okchec = input("Do you want to try again? type no if false: ")
            if okchec == 'no':
                continuechk = False


main()

# List of known issues and possible improvements
# 3- Can use direct user keyboard input to register a letter rather than pressing enter
# 4- Should make a function to automatically insert new words into files
