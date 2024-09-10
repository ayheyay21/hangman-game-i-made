import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def word_extractor(number):
    if number != 0:
        option = number - 1
        optionslist = ['wordlist.txt', 'carslist.txt', 'videogameslist.txt', 'countrieslist.txt',
                       'movielist.txt', 'tvshowlist.txt', 'americanstateslist.txt']
        filename = optionslist[option]
        os.system('cls')
        file_path = os.path.join(script_dir, 'database', filename)
        with open(file_path) as f:
            wordlist = []
            for line in f:
                wordlist.append(line.strip())
        word = random.choice(wordlist).lower()
        return word, len(optionslist)

def main():
    continuechk = True
    while continuechk == True:
        os.system('cls')
        print("_______________________________________")
        print("1: Common English Words")
        print("2: Cars")
        print("3: Video Games")
        print("4: Countries")
        print("5: Movies")
        print("6: TV Shows")
        print("7: American States")
        print("_______________________________________")
        hangchoice = int(input(">"))
        x, num_of_options = word_extractor(hangchoice)
        if hangchoice <= num_of_options and hangchoice > 0:
            word, y = word_extractor(hangchoice)
        else:
            print("____________________________________")
            tchoice = input("Enter a valid number")
            print("____________________________________")
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

        punct = [' ', "'", '"', '-', ':', ';', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        p = 0
        for letter in word:
            if letter in punct:
                blankarr[p] = letter
            p = p + 1

        p = 0
        for letter in word:
            if letter == "'":
                blankarr[p] = letter
            p = p + 1

        completion = False
        chances = 6
        while ((chances > 0) and (completion == False)):

            blanknonarr = ''
            for z in range(0, len(blankarr)):
                blanknonarr = blanknonarr + blankarr[z]

            print(f'({blanknonarr})')
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
            continuechk = False

main()

# List of known issues and possible improvements
# 3- Can use direct user keyboard input to register a letter rather than pressing enter
# 4- Should make a function to automatically insert new words into files
# 5- Could possibly encrypt and decrypt files
