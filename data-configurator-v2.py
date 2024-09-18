# Configurator
from logging import exception

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import sqlite3
import secrets
import string
import base64
import random
import os

from unicodedata import category


def encrypt(plaintext):
    key = "s4$t%%2rW@kL9&xZ"
    key = key.encode('utf-8')
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    encrypted = cipher.encrypt(padded_plaintext)
    encrypted_base64 = base64.b64encode(iv + encrypted).decode('utf-8')
    return encrypted_base64

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

def table_checker(tag):
    def table_name_retriever():
        tables = get_words('sqlite_sequence', 'name')
        return tables

    options = table_name_retriever()

    if tag == 1:
        while True:
            os.system('cls')
            print("List of tables: ")
            count = 0
            print("______________________________________")
            for item in options:
                count += 1
                print(f"{count}: {item.title()}")
            print("______________________________________")
            try:
                hangchoice = int(input(">"))
                if hangchoice > 0 and hangchoice <= count:
                    selected_table = options[hangchoice - 1]
                    return selected_table
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
        return options

def get_words(category_name, column_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    query = f'SELECT "{column_name}" FROM "{category_name}"'

    try:
        cursor.execute(query)
        cipher = [row[0] for row in cursor.fetchall()]
        return cipher

    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")
        return []

    finally:
        conn.close()

def insert_words(category_name, words):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{category_name}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            cipher TEXT NOT NULL
        );''')

    wordlist = get_words(category_name, 'word')
    f = False
    for word in words:
        if word not in wordlist:
            encrypted_word = encrypt(word)
            cursor.execute(f'INSERT INTO "{category_name}" (word, cipher) VALUES (?, ?)', (word, encrypted_word))
        else:
            print(f"The word [{word}] already exists in table [{category_name}]")
            f = True

    if f == True:
        input("press enter to continue")

    conn.commit()
    conn.close()

def word_inserter():
    os.system('cls')
    while True:
        print("______________________________")
        print("1: Pre-existing category")
        print("2: Create a new table")
        print("______________________________")
        p = int(input(">"))
        if p == 1:
            os.system('cls')
            table = table_checker(1)
            os.system('cls')
            break
        elif p == 2:
            os.system('cls')
            print("\n\n")
            category_name = input("Enter the name of the category: ")
            table = category_name
            break
        else:
            os.system('cls')
            print("invalid input")

    print("\n\n")
    words = []
    check = True
    while check:
        os.system('cls')
        print("\n")
        print("Enter -1 to stop inputting words")
        print("\n\n")
        word = input("Enter the word: ")
        if word == '-1':
            break
        words.append(word)


    insert_words(table, words)
    os.system('cls')
    print("\n\n[SUCCESS] The word(s) have been inserted into the database")
    input("Press enter to continue")
    os.system('cls')

def database_column_fetcher(table_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f'PRAGMA table_info("{table_name}")'
    try:
        cursor.execute(query)
        columns_info = cursor.fetchall()
        options = [column[1] for column in columns_info]
        while True:
            os.system('cls')
            print("List of columns: ")
            count = 0
            print("______________________________________")
            for item in options:
                count += 1
                print(f"{count}: {item.title()}")
            print("______________________________________")
            try:
                hangchoice = int(input(">"))
                if hangchoice > 0 and hangchoice <= count:
                    selected_column = options[hangchoice - 1]
                    return selected_column
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

    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()

def list_printer(wordlist, tag):
    os.system('cls')
    if tag == 1:
        count = 1
        for element in wordlist:
            print(f"{count}: {element}")
            count += 1

def delete_table(table_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(f'DROP TABLE IF EXISTS "{table_name}"')
        conn.commit()
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()
    finally:
        conn.close()

def table_reset(table_name):
    wordlist = get_words(table_name, 'word')
    delete_table(table_name)
    insert_words(table_name, wordlist)

def delete_row_by_name(table_name, name):
    # Connect to the SQLite database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f'DELETE FROM "{table_name}" WHERE word = ?', (name,))
        conn.commit()

        os.system('cls')
        print(f'[SUCCESS] Row with word "{name}" deleted from {table_name}.')
        input("Press enter to continue")

    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        conn.rollback()

    finally:
        conn.close()

def row_deleter():
    try:
        table_name = table_checker(1)
        wordlist = get_words(table_name, 'word')
        list_printer(wordlist, 1)
        name = input("Enter the name of the row you wish to delete: ").lower()
        delete_row_by_name(table_name, name)
        table_reset(table_name)
        os.system('cls')
    except Exception as e:
        print(f"Error: {e}")
        input("Press enter to continue")

# main function that controls what is done
def configurator():
    os.system('cls')
    while True:
        try:
            print("Enter -1 to quit")
            print("____________________________________")
            print("1: Retrieve data from database")
            print("2: Insert data into the database")
            print("3: Remove an element from a table")
            print("____________________________________")
            config = int(input(">"))
            if config == 1:
                os.system('cls')
                table_name = table_checker(1)
                column_name = database_column_fetcher(table_name)
                wordlist = get_words(table_name, column_name)
                list_printer(wordlist, 1)
                input("Press enter to continue")
                os.system('cls')
            elif config == 2:
                os.system('cls')
                word_inserter()
                os.system('cls')
            elif config == 3:
                os.system('cls')
                row_deleter()
            elif config == -1:
                return
            else:
                os.system('cls')
                print("invalid input")
        except Exception as e:
            os.system('cls')
            print(f"error: {e}")

configurator()
