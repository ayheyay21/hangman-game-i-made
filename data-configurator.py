# Configurator
import random
import os
script_dir = os.path.dirname(os.path.abspath(__file__))

def file_sorter(filename, tag):
    file_path = os.path.join(script_dir, 'database', filename)
    with open(file_path, 'r') as file:
        words = file.readlines()
    words = [word.strip() for word in words]
    words.sort()
    with open(file_path, 'w') as file:
        for word in words:
            file.write(word + '\n')
    os.system('cls')
    if tag == 1:
        print("______________________________________________________________")
        print(f"[SUCCESS]: [{file_path}] has been successfully sorted")
        print("______________________________________________________________")
        input("Press enter to continue")
        return -1
    elif tag == 2:
        return -2

def duplicate_checker(filename):

    def remove_line(file_name, line_to_remove):
        with open(file_name, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != line_to_remove]
        with open(file_name, 'w') as file:
            file.writelines(lines)
        with open(file_name, 'a') as file:
            file.write(f"\n{line_to_remove}")
        with open(file_name, 'r') as file:
            lines = file.readlines()
        lines = [line for line in lines if line.strip() != '']
        with open(file_name, 'w') as file:
            file.writelines(lines)

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
                remove_line(file_path, item)
            print("______________________________________________________________")
            print(f"[SUCCESS] Duplicates have been removed from [{file_path}]")
            print("______________________________________________________________")
            input("Press enter to continue")

def configurator():
    os.system('cls')
    print("____________________________________")
    print("1: Check data files for duplicates")
    print("2: Sorting the data files")
    print("____________________________________")
    config = int(input(">"))
    if config == 1:
        filename = input("Enter the name of the file located in the database folder: ")
        duplicate_checker(filename)
    elif config == 2:
        filename = input("Enter the name of the file located in the database folder: ")
        file_sorter(filename, 1)

configurator()
