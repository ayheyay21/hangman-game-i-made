# Configurator
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import sqlite3
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
    #function the retrieves the file names
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

    for word in words:
        encrypted_word = encrypt(word)
        cursor.execute(f'INSERT INTO "{category_name}" (word, cipher) VALUES (?, ?)', (word, encrypted_word))

    conn.commit()
    conn.close()

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

def list_printer(wordlist):
    os.system('cls')
    count = 1
    for element in wordlist:
        print(f"{count}: {element}")
        count += 1
    input("Press enter to continue")

# main function that controls what is done
def configurator():
    while True:
        os.system('cls')
        print("____________________________________")
        print("1: Retrieve data from database")
        print("____________________________________")
        config = int(input(">"))
        if config == 1:
            table_name = table_checker(1)
            column_name = database_column_fetcher(table_name)
            wordlist = get_words(table_name, column_name)
            list_printer(wordlist)


configurator()
