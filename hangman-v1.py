import english_words
import random
import os
# repairing directories
script_dir = os.path.dirname(os.path.abspath(__file__))

concheck = True
while concheck == True:
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
        # another attempt at hangman

        with open("wordlist.txt") as f:
            wordlist = []
            for line in f:
                wordlist.append(line.strip())

        word = random.choice(wordlist).lower()

    # Advanced English Words
    elif hangchoice == 2:
        # another attempt at hangman

        wordset = list(english_words.english_words_lower_alpha_set)
        word = random.choice(wordset)

        word = random.choice(wordset)
    #Video games hangman
    elif hangchoice == 3:

        with open("videogameslist.txt") as f:
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
    chance = [chance0, chance1, chance2, chance3, chance4, chance5]

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
        print(f'attempted letters: {repeated}')
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
                print("INCORRECT")
                print(f'{chances} chances remaining')
                if chances == 5:
                    print(chance[5])
                elif chances == 4:
                    print(chance[4])
                elif chances == 3:
                    print(chance[3])
                elif chances == 2:
                    print(chance[2])
                elif chances == 1:
                    print(chance[1])
                elif chances == 0:
                    print(chance[0])
            repeated.append(guess)
        else:
            print("LETTER ALREADY ATTEMPTED")

    if chances == 0 and completion == False:
        print("YOU COULDNT GUESS THE WORD")
    elif chances > 0 and completion == True:
        print("CONGRATULATIONS ON GUESSING THE WORD!!!!")
    print("THE WORD WAS:")
    print(f'[{word}]')

    okchec = input("Do you want to try again? type no if false: ")
    if okchec == 'no':
        concheck = False
