import random
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))

sys.set_int_max_str_digits(0)
#This function decrypts previously encrypted values
def decrypt(cipher):
    while True:
        try:
            os.system('cls')
            cipherarr = [None] * (len(cipher))
            c = 0
            for char in cipher:
                cipherarr[c] = char
                c += 1
            cipherogarr = [None] * (len(cipher))
            hexval = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            remapval = ['%', 'r', '[', '?', '7', 'q', '$', 'K', 'z', ')', '{', 'a', 'F', '3', '6', 'e']
            b = 0
            for value in cipherarr:
                v = 0
                flag = False
                while flag == False:
                    if value == remapval[v]:
                        cipherogarr[b] = hexval[v]
                        flag = True
                    v += 1
                b += 1
            hexstring = ''
            for item in cipherogarr:
                hexstring = hexstring + item
            denval = int(hexstring, base=16)
            denvalstr = str(denval)
            denvalstrarr = [None] * (len(denvalstr))
            denvalintarr = [0] * (len(denvalstr))
            d = 0
            for item in denvalstr:
                denvalstrarr[d] = item
                d += 1
            w = 0
            for digit in denvalstrarr:
                denvalintarr[w] = int(digit)
                w += 1
            remap2 = [4, 7, 5, 1, 9, 6, 3, 8, 0, 2]
            ogdenvalintarr = [0] * (len(denvalintarr))
            h = 0
            for digit in denvalintarr:
                ogdenvalintarr[h] = remap2[digit]
                h += 1
            ogdenvalintarrrev = ogdenvalintarr[::-1]
            originaldenary = [0] * (len(ogdenvalintarrrev))
            f = 0
            for item in ogdenvalintarrrev:
                originaldenary[f] = 9 - item
                f += 1
            orignaldenarystrarr = [None] * (len(originaldenary))
            p = 0
            for item in originaldenary:
                orignaldenarystrarr[p] = str(item)
                p += 1
            originaldenarystr = ''
            for item in orignaldenarystrarr:
                originaldenarystr = originaldenarystr + item
            originaldenaryint = int(originaldenarystr)
            decimal = originaldenaryint
            hex_digits = "0123456789ABCDEF"
            hexadecimal = ""
            while decimal > 0:
                remainder = decimal % 16
                hexadecimal = hex_digits[remainder] + hexadecimal
                decimal = decimal // 16
            kys = hexadecimal
            code = kys
            codeshift1 = int(code[len(code) - 2])
            codeshift2 = int(code[len(code) - 1])
            codearr = [None] * (len(code) // 2)
            for count in range(0, len(codearr)):
                codearr[count] = ''
            index = 0
            for t in range(0, len(codearr)):
                for y in range(0 + index, 2 + index):
                    codearr[t] = codearr[t] + code[y]
                index += 2
            codearr.pop()
            codebinarr = [None] * (len(codearr))
            r = 0
            for item in codearr:
                hexdecnum = item
                binnum = ""
                hexlen = len(hexdecnum)
                i = 0
                while i < hexlen:
                    if hexdecnum[i] == '0':
                        binnum = binnum + "0000"
                    elif hexdecnum[i] == '1':
                        binnum = binnum + "0001"
                    elif hexdecnum[i] == '2':
                        binnum = binnum + "0010"
                    elif hexdecnum[i] == '3':
                        binnum = binnum + "0011"
                    elif hexdecnum[i] == '4':
                        binnum = binnum + "0100"
                    elif hexdecnum[i] == '5':
                        binnum = binnum + "0101"
                    elif hexdecnum[i] == '6':
                        binnum = binnum + "0110"
                    elif hexdecnum[i] == '7':
                        binnum = binnum + "0111"
                    elif hexdecnum[i] == '8':
                        binnum = binnum + "1000"
                    elif hexdecnum[i] == '9':
                        binnum = binnum + "1001"
                    elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
                        binnum = binnum + "1010"
                    elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
                        binnum = binnum + "1011"
                    elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
                        binnum = binnum + "1100"
                    elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
                        binnum = binnum + "1101"
                    elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
                        binnum = binnum + "1110"
                    elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
                        binnum = binnum + "1111"
                    i = i + 1
                codebinarr[r] = binnum
                r += 1
            binstring = ''
            for f in range(0, len(codebinarr)):
                binstring = binstring + codebinarr[f]
            binstringarr = [None] * (len(binstring))
            for g in range(0, len(binstring)):
                binstringarr[g] = binstring[g]
            for item in range(0, len(binstringarr), codeshift2):
                if binstringarr[item] == '0':
                    binstringarr[item] = '1'
                elif binstringarr[item] == '1':
                    binstringarr[item] = '0'
            for item in range(0, len(binstringarr), codeshift1):
                if binstringarr[item] == '0':
                    binstringarr[item] = '1'
                elif binstringarr[item] == '1':
                    binstringarr[item] = '0'
            binstring2 = ''
            for u in range(0, len(binstringarr)):
                binstring2 = binstring2 + binstringarr[u]
            binstringarr2 = [None] * (len(binstring2) // 8)
            for n in range(0, len(binstringarr2)):
                binstringarr2[n] = ''
            index = 0
            for t in range(0, len(binstringarr2)):
                for y in range(0 + index, 8 + index):
                    binstringarr2[t] = binstringarr2[t] + binstring2[y]
                index += 8
            arrbindec = [None] * (len(binstringarr2))
            for k in range(0, len(binstringarr2)):
                b_num = list(binstringarr2[k])
                value = 0
                for i in range(len(b_num)):
                    digit = b_num.pop()
                    if digit == '1':
                        value = value + pow(2, i)
                arrbindec[k] = value
            binascarr = [None] * len(binstringarr2)
            z = 0
            for item in arrbindec:
                binascarr[z] = chr(item)
                z += 1
            decryptcipherstr = ''
            for h in range(0, len(binascarr)):
                decryptcipherstr = decryptcipherstr + binascarr[h]
            return decryptcipherstr
        except:
            return ''

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
                if chances == 6:
                    chancearr6 = ['  ______ ', " |      |", '        |', '        |', '        |', '---------']
                    chance_printer2(chancearr6)
                elif chances == 5:
                    chancearr5 = ['  ______ ', " |      |", ' O      |', '        |', '        |', '---------']
                    chance_printer2(chancearr5)
                elif chances == 4:
                    chancearr4 = ['  ______ ', " |      |", ' O      |', ' |      |', '        |', '---------']
                    chance_printer2(chancearr4)
                elif chances == 3:
                    chancearr3 = ['  ______ ', " |      |", ' O      |', '/|      |', '        |', '---------']
                    chance_printer2(chancearr3)
                elif chances == 2:
                    chancearr2 = ['  ______ ', " |      |", ' O      |', '/|\     |', '        |', '---------']
                    chance_printer2(chancearr2)
                elif chances == 1:
                    chancearr1 = ['  ______ ', " |      |", ' O      |', '/|\     |', '/       |', '---------']
                    chance_printer2(chancearr1)
                elif chances == 0:
                    chancearr0 = ['  ______ ', " |      |", ' O      |', '/|\     |', '/ \     |', '---------']
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
# 5- Could possibly encrypt and decrypt files
