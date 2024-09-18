# Configurator
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import secrets
import string
import base64
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def encrypt(plaintext):
    key = "s4$t%%2rW@kL9&xZ"
    key = key.encode('utf-8')
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded_plaintext)
    encrypted_base64 = base64.b64encode(iv + encrypted).decode('utf-8')
    return encrypted_base64

def decrypt_string(encrypted_base64):
    key = "s4$t%%2rW@kL9&xZ"
    key = key.encode('utf-8')
    encrypted_data = base64.b64decode(encrypted_base64)
    iv = encrypted_data[:AES.block_size]
    encrypted = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted)
    decrypted = unpad(decrypted_padded, AES.block_size)
    return decrypted.decode('utf-8')

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
