# Configurator
import random
import os

script_dir = os.path.dirname(os.path.abspath(__file__))


# extracts list of words from a text file
def wordlist_extractor(filename, tag):
    os.system('cls')
    file_path = os.path.join(script_dir, 'database', filename)
    with open(file_path) as f:
        wordlist = []
        for line in f:
            wordlist.append(line.strip())
    if tag == 1:
        return wordlist
    elif tag == 2:
        print("_____________________________")
        print(wordlist)
        print("_____________________________")
        input("Press enter to continue")
        os.system('cls')
        return -1


# function used to remove specific bits of data from a text file
def remove_line(filename, line_to_remove, tag):
    file_path = os.path.join(script_dir, 'database', filename)
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
    file_path = os.path.join(script_dir, 'database', filename)
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
    remove_line(filename, '', 3)
    remove_line(filename, '', 4)
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
    file_path = os.path.join(script_dir, 'database', filename)
    with open(file_path, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    words.sort()
    with open(file_path, 'w') as file:
        for word in words:
            file.write(word + '\n')
    remove_line(filename, '', 3)
    remove_line(filename, '', 4)
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
    file_path = os.path.join(script_dir, 'database', filename)
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
                remove_line(file_path, item, 1)
            print("______________________________________________________________")
            print(f"[SUCCESS] Duplicates have been removed from [{file_path}]")
            print("______________________________________________________________")
            input("Press enter to continue")


# main function that controls what is done
def configurator():
    os.system('cls')
    print("____________________________________")
    print("1: Check data files for duplicates")
    print("2: Sorting the data files")
    print("3: Shuffle the data files")
    print("4: Access all the words in the file")
    print("____________________________________")
    config = int(input(">"))
    if config == 1:
        filename = input("Enter the name of the file located in the database folder: ")
        duplicate_checker(filename)
    elif config == 2:
        filename = input("Enter the name of the file located in the database folder: ")
        file_sorter(filename, 1)
    elif config == 3:
        filename = input("Enter the name of the file located in the database folder: ")
        file_shuffler(filename, 1)
    elif config == 4:
        filename = input("Enter the name of the file located in the database folder: ")
        wordlist_extractor(filename, 2)


configurator()
