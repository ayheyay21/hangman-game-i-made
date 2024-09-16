# Configurator
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def decrypt(cipher):
    def string_separate_into_elements_list(stringbin1):
        stringbin1arr = [None] * (len(stringbin1))
        v = 0
        for bit in stringbin1:
            stringbin1arr[v] = bit
            v += 1
        return stringbin1arr
    def dec_remap_char(cipherarr, cipher):
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
        return cipherogarr
    def list_join_into_string(wordarrbin):
        stringbin1 = ''
        for letter in range(0, len(wordarrbin)):
            stringbin1 = stringbin1 + wordarrbin[letter]
        return stringbin1
    def hex_into_dec_string(hexstring):
        denval = int(hexstring, base=16)
        denvalstr = str(denval)
        return denvalstr
    def string_separate_into_elements_list(stringbin1):
        stringbin1arr = [None] * (len(stringbin1))
        v = 0
        for bit in stringbin1:
            stringbin1arr[v] = bit
            v += 1
        return stringbin1arr
    def each_element_string_to_int(denvalstrarr):
        denvalintarr = [0] * (len(denvalstr))
        w = 0
        for digit in denvalstrarr:
            denvalintarr[w] = int(digit)
            w += 1
        return denvalintarr
    def dec_remap_digits(denvalintarr):
        remap2 = [4, 7, 5, 1, 9, 6, 3, 8, 0, 2]
        ogdenvalintarr = [0] * (len(denvalintarr))
        h = 0
        for digit in denvalintarr:
            ogdenvalintarr[h] = remap2[digit]
            h += 1
        return ogdenvalintarr
    def subtract_each_element_from_nine(ogdenvalintarrrev):
        originaldenary = [0] * (len(ogdenvalintarrrev))
        f = 0
        for item in ogdenvalintarrrev:
            originaldenary[f] = 9 - item
            f += 1
        return originaldenary
    def int_list_to_string(originaldenary):
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
        return decimal
    def denary_string_to_hex_string(decimal):
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""
        while decimal > 0:
            remainder = decimal % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            decimal = decimal // 16
        kys = hexadecimal
        code = kys
        return code
    def shift_dec_code(code):
        codeshift1 = int(code[len(code) - 2])
        codeshift2 = int(code[len(code) - 1])
        return codeshift1, codeshift2
    def split_string_into_pairs_minus_last_two(code):
        codearr = [None] * (len(code) // 2)
        for count in range(0, len(codearr)):
            codearr[count] = ''
        index = 0
        for t in range(0, len(codearr)):
            for y in range(0 + index, 2 + index):
                codearr[t] = codearr[t] + code[y]
            index += 2
        codearr.pop()
        return codearr
    def two_digit_hex_into_eight_bit_binary(codearr):
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
        return codebinarr
    def list_join_into_string(codebinarr):
        binstring = ''
        for f in range(0, len(codebinarr)):
            binstring = binstring + codebinarr[f]
        return binstring
    def string_split_into_separate_elements(binstring):
        binstringarr = [None] * (len(binstring))
        for g in range(0, len(binstring)):
            binstringarr[g] = binstring[g]
        return binstringarr
    def string_swap_codeshift(binstringarr, codeshift1, codeshift2):
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
        return binstringarr
    def split_string_into_eight_bits(binstring2):
        binstringarr2 = [None] * (len(binstring2) // 8)
        for n in range(0, len(binstringarr2)):
            binstringarr2[n] = ''
        index = 0
        for t in range(0, len(binstringarr2)):
            for y in range(0 + index, 8 + index):
                binstringarr2[t] = binstringarr2[t] + binstring2[y]
            index += 8
        return binstringarr2
    def eight_bit_binary_to_denary(binstringarr2):
        arrbindec = [None] * (len(binstringarr2))
        for k in range(0, len(binstringarr2)):
            b_num = list(binstringarr2[k])
            value = 0
            for i in range(len(b_num)):
                digit = b_num.pop()
                if digit == '1':
                    value = value + pow(2, i)
            arrbindec[k] = value
        return arrbindec
    def denary_to_ascii_char(arrbindec):
        binascarr = [None] * len(binstringarr2)
        z = 0
        for item in arrbindec:
            binascarr[z] = chr(item)
            z += 1
        return binascarr

    while True:
        try:
            os.system('cls')
            cipherarr = string_separate_into_elements_list(cipher)
            cipherogarr = dec_remap_char(cipherarr, cipher)
            hexstring = list_join_into_string(cipherogarr)
            denvalstr = hex_into_dec_string(hexstring)
            denvalstrarr = string_separate_into_elements_list(denvalstr)
            denvalintarr = each_element_string_to_int(denvalstrarr)
            ogdenvalintarr = dec_remap_digits(denvalintarr)
            ogdenvalintarrrev = ogdenvalintarr[::-1]
            originaldenary = subtract_each_element_from_nine(ogdenvalintarrrev)
            decimal = int_list_to_string(originaldenary)
            code = denary_string_to_hex_string(decimal)
            codeshift1, codeshift2 = shift_dec_code(code)
            codearr = split_string_into_pairs_minus_last_two(code)
            codebinarr = two_digit_hex_into_eight_bit_binary(codearr)
            binstring = list_join_into_string(codebinarr)
            binstringarr = string_split_into_separate_elements(binstring)
            binstringarr = string_swap_codeshift(binstringarr, codeshift1, codeshift2)
            binstring2 = list_join_into_string(binstringarr)
            binstringarr2 = split_string_into_eight_bits(binstring2)
            arrbindec = eight_bit_binary_to_denary(binstringarr2)
            binascarr = denary_to_ascii_char(arrbindec)
            decryptcipherstr = list_join_into_string(binascarr)
            return decryptcipherstr
        except:
            return 'error'

def encrypt(word):
    os.system('cls')
    def ascii_convert(word):
        x = 0
        wordarrdec = [0] * (len(word))
        wordarrhex = [None] * (len(word))

        for letter in word:
            wordarrdec[x] = ord(letter)
            x += 1
        return wordarrdec
    def eight_bit_binary_convert(wordarrdec):
        wordarrbin = []
        for item in wordarrdec:
            b_string = bin(item)[2:]
            b_string = b_string.zfill(8)
            wordarrbin.append(b_string)
        return wordarrbin
    def list_join_into_string(wordarrbin):
        stringbin1 = ''
        for letter in range(0, len(wordarrbin)):
            stringbin1 = stringbin1 + wordarrbin[letter]
        return stringbin1
    def string_separate_into_elements_list(stringbin1):
        stringbin1arr = [None] * (len(stringbin1))
        v = 0
        for bit in stringbin1:
            stringbin1arr[v] = bit
            v += 1
        return stringbin1arr
    def picking_random_numbers_and_joining():
        choice1 = [3, 5, 7]
        choice2 = [2, 4, 6]
        ranshift1 = random.choice(choice1)
        ranshift2 = random.choice(choice2)
        finalranshift = (str(ranshift1)) + (str(ranshift2))
        return finalranshift, ranshift1, ranshift2
    def binary_switcher(stringbin1arr, ranshift1, ranshift2):
        for item in range(0, len(stringbin1arr), ranshift1):
            if stringbin1arr[item] == '0':
                stringbin1arr[item] = '1'
            elif stringbin1arr[item] == '1':
                stringbin1arr[item] = '0'
        for item in range(0, len(stringbin1arr), ranshift2):
            if stringbin1arr[item] == '0':
                stringbin1arr[item] = '1'
            elif stringbin1arr[item] == '1':
                stringbin1arr[item] = '0'
        return stringbin1arr
    def split_string_into_bytes_of_eight(stringbin1arr):
        stringbin2 = [None] * (((len(stringbin1arr)) // 8))
        for n in range(0, len(stringbin2)):
            stringbin2[n] = ''
        index = 0
        for t in range(0, len(stringbin2)):
            for y in range(0 + index, 8 + index):
                stringbin2[t] = stringbin2[t] + stringbin1arr[y]
            index += 8
        return stringbin2
    def binary_list_to_denary_list(stringbin2):
        arrbindec = [None] * (len(stringbin2))
        for k in range(0, len(stringbin2)):
            b_num = list(stringbin2[k])
            value = 0
            for i in range(len(b_num)):
                digit = b_num.pop()
                if digit == '1':
                    value = value + pow(2, i)
            arrbindec[k] = value
        return arrbindec
    def denary_list_to_hex_list(arrbindec, stringbin2):
        arrbinhex = [None] * (len(stringbin2))
        for i in range(0, len(stringbin2)):
            decimal = int(arrbindec[i])
            intact = decimal
            hexadecimal = ''
            dictionary = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
                          9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            while (decimal != 0):
                c = decimal % 16
                hexadecimal = dictionary[c] + hexadecimal
                decimal = int(decimal / 16)
            arrbinhex[i] = hexadecimal
        for o in range(0, len(arrbinhex)):
            if len(arrbinhex[o]) < 2:
                arrbinhex[o] = '0' + arrbinhex[o]
        return arrbinhex
    def hex_to_denary_string(finalstring):
        decf = int(finalstring, base=16)
        decfstr = str(decf)
        return decfstr
    def each_string_element_into_int(decfstrarr):
        decfintarr = [0] * (len(decfstr))
        y = 0
        for digit in decfstrarr:
            decfintarr[y] = int(digit)
            y += 1
        return decfintarr
    def subtract_each_element_from_nine(decfintarr):
        decfmodintarr = [0] * (len(decfstr))
        z = 0
        for digit in decfintarr:
            decfmodintarr[z] = 9 - digit
            z += 1
        return decfmodintarr
    def enc_remap_digits(decfrevintarr, decfstr):
        decfrevintarrremap = [0] * (len(decfstr))
        decfrevstrarrremap = [None] * (len(decfstr))
        remap1 = [8, 3, 9, 6, 0, 2, 5, 1, 7, 4]
        h = 0
        for digit in decfrevintarr:
            decfrevintarrremap[h] = remap1[digit]
            h += 1
        f = 0
        for digit in decfrevintarrremap:
            decfrevstrarrremap[f] = str(digit)
            f += 1
        denstring = ''
        for g in decfrevstrarrremap:
            denstring = denstring + g
        denint = int(denstring)
        decimal = denint
        return decimal
    def denary_string_to_hex_string(decimal):
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""
        while decimal > 0:
            remainder = decimal % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            decimal = decimal // 16
        finalhex = hexadecimal
        return finalhex
    def enc_remap_hex(finalhexarr, finalhex):
        finalhexremaparr = [None] * (len(finalhex))
        hexval = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        remapval = ['%', 'r', '[', '?', '7', 'q', '$', 'K', 'z', ')', '{', 'a', 'F', '3', '6', 'e']
        b = 0
        for value in finalhexarr:
            v = 0
            flag = False
            while flag == False:
                if value == hexval[v]:
                    finalhexremaparr[b] = remapval[v]
                    flag = True
                v += 1
            b += 1
        return finalhexremaparr

    while True:
        try:
            wordarrdec = ascii_convert(word)
            wordarrbin = eight_bit_binary_convert(wordarrdec)
            stringbin1 = list_join_into_string(wordarrbin)
            stringbin1arr = string_separate_into_elements_list(stringbin1)
            finalranshift, ranshift1, ranshift2 = picking_random_numbers_and_joining()
            stringbin1arr = binary_switcher(stringbin1arr, ranshift1, ranshift2)
            stringbin2 = split_string_into_bytes_of_eight(stringbin1arr)
            arrbindec = binary_list_to_denary_list(stringbin2)
            arrbinhex = denary_list_to_hex_list(arrbindec, stringbin2)
            finalstring = list_join_into_string(arrbinhex)
            finalstring = finalstring + finalranshift
            decfstr = hex_to_denary_string(finalstring)
            decfstrarr = string_separate_into_elements_list(decfstr)
            decfintarr = each_string_element_into_int(decfstrarr)
            decfmodintarr = subtract_each_element_from_nine(decfintarr)
            decfrevintarr = decfmodintarr[::-1]
            decimal = enc_remap_digits(decfrevintarr, decfstr)
            finalhex = denary_string_to_hex_string(decimal)
            finalhexarr = string_separate_into_elements_list(finalhex)
            finalhexremaparr = enc_remap_hex(finalhexarr, finalhex)
            finalremapstring = list_join_into_string(finalhexremaparr)
            kys = finalremapstring
            check = decrypt(kys)
            if check == word:
                return kys
        except:
            continue

def file_encrypter(filename):
    file_path = os.path.join(script_dir, 'database', filename)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        encrypted = []

        for item in lines:
            cipher = encrypt(item)
            encrypted.append(cipher)
        with open(file_path, 'w') as file:
            # Iterate through the list and write each element to a new line in the file
            for item in encrypted:
                file.write(str(item) + '\n')
        remove_line(filename, '', 4)
        print(f"[SUCCESS] All the elements in [{file_path}] were successfully encrypted")

    except Exception as e:
        os.system('cls')
        print("An error occurred. Error info below")
        print("________________________________________")
        print(e)
        print("________________________________________")
        try:
            input("Press enter to return: ")
            os.system('cls')
            return -1
        except:
            os.system('cls')
            return -1
            pass

#This uses the decrypt function to decrypt every line in the previously encrypted file
def file_decrypter(filename):
    file_path = os.path.join(script_dir, 'database', filename)
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines]
        decrypted = []
        for item in lines:
            decypher = decrypt(item)
            decrypted.append(decypher)
        with open(file_path, 'w') as file:
            for item in decrypted:
                file.write(str(item) + '\n')
        remove_line(filename, '', 4, 'database')
        print(f"[SUCCESS] All the elements in [{file_path}] were successfully decrypted")

    except Exception as e:
        os.system('cls')
        print("An error occurred. Error info below")
        print("________________________________________")
        print(e)
        print("________________________________________")
        try:
            input("Press enter to return: ")
            return -1
            os.system('cls')
        except:
            os.system('cls')
            return -1
            pass


def file_checker(folder, tag):
    #function the retrieves the file names
    def file_name_retriever():
        script_dir = os.path.dirname(os.path.abspath(__file__))
        target_folder = os.path.join(script_dir, folder)
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

    if tag == 1:
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
    elif tag == 2:
        return file_names

# extracts list of words from a text file
def wordlist_extractor(filename, tag, folder):
    file_path = os.path.join(script_dir, folder, filename)
    with open(file_path) as f:
        wordlist = []
        for line in f:
            wordlist.append(line.strip())
    if tag == 1:
        return wordlist
    elif tag == 2:
        os.system('cls')
        print("_____________________________")
        print(wordlist)
        print("_____________________________")
        input("Press enter to continue")
        os.system('cls')
        return -1

# function used to remove specific bits of data from a text file
def remove_line(filename, line_to_remove, tag, folder):
    file_path = os.path.join(script_dir, folder, filename)
    # removes all instances of a word and then append it once to the end of the text file
    if tag == 1:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != line_to_remove]
        with open(file_path, 'w') as file:
            file.writelines(lines)
        with open(file_path, 'a') as file:
            file.write(f"\n{line_to_remove}")
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != '']
        with open(file_path, 'w') as file:
            file.writelines(lines)

    # removes all instances of the line without appending it to the end of the text file
    elif tag == 2:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != line_to_remove]
        with open(file_path, 'w') as file:
            file.writelines(lines)

    # removes and blanks from a text file
    elif tag == 3:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != '']
        with open(file_path, 'w') as file:
            file.writelines(lines)

    # removes the training new line character from the end of the text file
    elif tag == 4:
        with open(file_path, 'r') as file:
            content = file.read()
        content = content.rstrip('\n')
        with open(file_path, 'w') as file:
            file.write(content)

# function used to shuffle all items in a text file
def file_shuffler(filename, tag):
    os.system('cls')
    file_path = os.path.join(script_dir, 'database-backup', filename)
    with open(file_path, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    wordslength = len(words)
    shuffle = []
    while len(shuffle) != wordslength:
        pick = random.choice(words)
        if pick not in shuffle:
            shuffle.append(pick)
            words.remove(pick)

    with open(file_path, 'w') as file:
        for word in shuffle:
            file.write(word + '\n')
    remove_line(filename, '', 3, 'database-backup')
    remove_line(filename, '', 4, 'database-backup')
    if tag == 1:
        print("______________________________________________________________")
        print(f"[SUCCESS]: [{file_path}] has been successfully shuffled")
        print("______________________________________________________________")
        input("Press enter to continue")
        return -1
    elif tag == 2:
        return -2

# function used to sort all items in a text file alphabetically
def file_sorter(filename, tag):
    file_path = os.path.join(script_dir, 'database-backup', filename)
    with open(file_path, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    words.sort()
    with open(file_path, 'w') as file:
        for word in words:
            file.write(word + '\n')
    remove_line(filename, '', 3, 'database-backup')
    remove_line(filename, '', 4, 'database-backup')
    os.system('cls')
    if tag == 1:
        print("______________________________________________________________")
        print(f"[SUCCESS]: [{file_path}] has been successfully sorted")
        print("______________________________________________________________")
        input("Press enter to continue")
        return -1
    elif tag == 2:
        return -2

# function used to check for duplicates in a text file
def duplicate_checker(filename):
    os.system('cls')
    file_path = os.path.join(script_dir, 'database-backup', filename)
    with open(file_path) as f:
        wordlist = []
        for line in f:
            wordlist.append(line.strip())

    duplicates = []
    duplicates_index = []
    dupl = []

    count = 1
    for item in wordlist:
        if item in dupl:
            duplicates.append(item)
            duplicates_index.append(count)
        dupl.append(item)
        count += 1

    if duplicates == []:
        print("___________________________________________________")
        print(f"There are no duplicates in [{file_path}]")
        print("___________________________________________________")
        input("Press enter to continue")
        os.system('cls')
    else:
        print("______________________________________________________________")
        print(f"Duplicates found in [{file_path}]:\n> {duplicates}\n Line Numbers: {duplicates_index}")
        print("______________________________________________________________")
        remove = input("Remove them? (y/n)\n>")
        os.system('cls')
        if remove == 'y':
            for item in duplicates:
                remove_line(file_path, item, 1, 'database-backup')
            print("______________________________________________________________")
            print(f"[SUCCESS] Duplicates have been removed from [{file_path}]")
            print("______________________________________________________________")
            input("Press enter to continue")

def length_comparer(filename):
    d_list = wordlist_extractor(filename, 1, 'database')
    db_list = wordlist_extractor(filename, 1, 'database-backup')
    lenD = len(d_list)
    lenDB = len(db_list)
    return lenD, lenDB

# function used to sync unencrypted database-backup words to database encrypted versions
def file_synchronization():
    while True:
        try:
            os.system('cls')
            db_filenames = file_checker('database-backup', 2)
            missedfiles = []
            print("___________________________________")
            for file in db_filenames:
                lenD, lenDB = length_comparer(file)
                even = 'SYNCED'
                if lenD != lenDB:
                    even = 'MISSING'
                    missedfiles.append(file)

                print(f'[{file}]')
                print(f'Database Items: [{lenD}] Database-Backup Items: [{lenDB}] Status: [{even}]')
            print("___________________________________")
            print("Do you wish to synchronize? (y/n)")
            u = input(">").lower()
            if u == 'y':
                check = True
                while check:
                    os.system('cls')
                    print("___________________________________")
                    print("1: SYNCHRONIZE ALL FILES")
                    print("2: SYNCHRONIZE MISSING FILES ONLY")
                    print("3: TO QUIT")
                    print("___________________________________")
                    y = int(input(">"))
                    if y == 1:
                        fileslist = db_filenames
                        check = False
                    elif y == 2:
                        fileslist = missedfiles
                        check = False
                    elif y == 3:
                        return -1
                    else:
                        print("invalid input")
                        print("press enter to continue")

                print("This may take a while. Do Not Exit The Program")
                input("Press enter to start")
                for file in fileslist:
                    file_path = os.path.join(script_dir, 'database', file)
                    words = wordlist_extractor(file, 1, 'database-backup')
                    encrypted = []
                    for item in words:
                        cipher = encrypt(item)
                        encrypted.append(cipher)
                    with open(file_path, 'w') as file:
                        # Iterate through the list and write each element to a new line in the file
                        for item in encrypted:
                            file.write(str(item) + '\n')
                    print(file)
                    remove_line(file_path, '', 4, 'database')
                os.system('cls')
                print("[SUCCESS] All files have been synced")
                input("Press enter to continue")
                break

            elif u == 'n':
                break
            else:
                print("invalid input")

        except:
            print("invalid input")


# main function that controls what is done
def configurator():
    os.system('cls')
    print("____________________________________")
    print("1: Check data files for duplicates")
    print("2: Sorting the data files")
    print("3: Shuffle the data files")
    print("4: Access all the words in the file")
    print("5: Encrypt file (Ensure all elements are unencrypted first)")
    print("6: Decrypt file (Ensure all elements are encrypted first")
    print("7: Sync database from database backup")
    print("____________________________________")
    config = int(input(">"))
    if config == 1:
        filename = file_checker('database-backup', 1)
        duplicate_checker(filename)
    elif config == 2:
        filename = file_checker('database-backup', 1)
        file_sorter(filename, 1)
    elif config == 3:
        filename = file_checker('database-backup', 1)
        file_shuffler(filename, 1)
    elif config == 4:
        filename = file_checker('database', 1)
        wordlist_extractor(filename, 2, 'database')
    elif config == 5:
        filename = file_checker('database', 1)
        file_encrypter(filename)
    elif config == 6:
        filename = file_checker('database', 1)
        file_decrypter(filename)
    elif config == 7:
        file_synchronization()

configurator()
