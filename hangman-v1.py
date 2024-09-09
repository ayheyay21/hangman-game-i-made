import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

concheck = True
while concheck == True:
    os.system('cls')
    print("_________________________________________________________________________")
    print("Enter 1 for Common English Words")
    print("_________________________________________________________________________")
    print("Enter 2 for Advanced English words")
    print("_________________________________________________________________________")
    print("Enter 3 for Video Games")
    print("_________________________________________________________________________")
    hangchoice = int(input(">"))
    # Common English Words
    if hangchoice == 1:
        os.system('cls')
        # another attempt at hangman
        file_path = os.path.join(script_dir, 'database', 'wordlist.txt')

        with open(file_path) as f:
            wordlist = []
            for line in f:
                wordlist.append(line.strip())

        word = random.choice(wordlist).lower()

    # Advanced English Words
    elif hangchoice == 2:
        os.system('cls')
        # another attempt at hangman

        wordset = list(english_words.english_words_lower_alpha_set)
        word = random.choice(wordset)

        word = random.choice(wordset)
    #Video games hangman
    elif hangchoice == 3:
        os.system('cls')
        file_path = os.path.join(script_dir, 'database', 'videogameslist.txt')

        with open(file_path) as f:
            wordlist = []
            for line in f:
                wordlist.append(line.strip())

        word = random.choice(wordlist).lower()


    # End of hangman
    else:
        print("_________________________________________________________________________")
        tchoice = input("Enter a valid number")
        print("_________________________________________________________________________")
        break

    wordarr = [None] * (len(word))
    blankarr = [None] * (len(word))
    blankarr1 = [None] * (len(word))
    blank1 = '-' * (len(word))
    blank = blank1

    chance6 = '''
                                        ______
                                       |      |
                                              |
                                              |
                                              |
                                      ---------

                            '''

    chance5 = '''
                                        ______
                                       |      |
                                       O      |
                                              |
                                              |
                                      ---------

                            '''
    chance4 = '''
                                        ______
                                       |      |
                                       O      |
                                       |      |
                                              |
                                      ---------

                            '''
    chance3 = '''
                                        ______
                                       |      |
                                       O      |
                                      /|      |
                                              |
                                      ---------

                            '''
    chance2 = '''
                                        ______
                                       |      |
                                       O      |
                                      /|\     |
                                              |
                                      ---------

                            '''
    chance1 = '''
                                        ______
                                       |      |
                                       O      |
                                      /|\     |
                                      /       |
                                      ---------

                            '''
    chance0 = '''
                                        ______
                                       |      |
                                       O      |
                                      /|\     |
                                      / \     |
                                      ---------

                            '''
    chance = [chance0, chance1, chance2, chance3, chance4, chance5, chance6]

    for x in range(0, (len(word))):
        blankarr[x] = blank[x]
    for x in range(0, (len(word))):
        wordarr[x] = word[x]

    repeated = [None]
    repeated.remove(None)

    p = 0
    for letter in word:
        if letter == ' ':
            blankarr[p] = letter
        p = p + 1

    completion = False
    chances = 6
    while ((chances > 0) and (completion == False)):
        
        blanknonarr = ''
        for z in range(0, len(blankarr)):
            blanknonarr = blanknonarr + blankarr[z]
        
        print(f'({blanknonarr})')
        guess = input("Guess a letter: ")
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

        print(f'Attempted letters: {repeated}')
        print(chance[chances])
          

    os.system('cls')
    if chances == 0 and completion == False:
        print("YOU COULDNT GUESS THE WORD")
        print(chance[0])
    elif chances > 0 and completion == True:
        print("CONGRATULATIONS ON GUESSING THE WORD!!!!")
        print(chance[chances])
    print("THE WORD WAS:")
    print(f'[{word}]')

    okchec = input("Do you want to try again? type no if false: ")
    if okchec == 'no':
        concheck = False

# List of known issues and possible improvements
# 1- It takes any single or multiple characters as a possible input
# 2- Lacks functions for retrieving data from the data files
# 3- Can use direct user keyboard input to register a letter rather than pressing enter
# 4- Should make a function to automatically insert new words into files
# 5- Could possibly encrypt and decrypt files
