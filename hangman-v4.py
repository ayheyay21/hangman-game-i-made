from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import messagebox
import sqlite3
import secrets
import string
import base64
import random
import os

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

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.category_name = None
        self.wordlist = []
        self.word = ""
        self.chances = 6
        self.blankarr = []
        self.repeated = []

        self.setup_start_menu()

    def setup_start_menu(self):
        self.clear_widgets()  # Clear existing widgets

        self.category_label = tk.Label(self.master, text="Select a category:")
        self.category_label.pack(pady=10)

        self.category_var = tk.StringVar(self.master)
        self.category_var.set("Choose a category")  # Default value

        categories = table_checker(2)  # Fetch categories
        self.category_menu = tk.OptionMenu(self.master, self.category_var, *categories)
        self.category_menu.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=20)

    def start_game(self):
        self.category_name = self.category_var.get()
        if self.category_name == "Choose a category":
            messagebox.showwarning("Selection Error", "Please select a valid category.")
            return

        self.wordlist = get_words(self.category_name, 'cipher')
        if not self.wordlist:
            messagebox.showwarning("No Words", "No words found for this category.")
            return

        self.word = decrypt(random.choice(self.wordlist))
        self.chances = 6
        self.blankarr = ['_' if c.isalpha() else c for c in self.word]
        self.repeated = []

        self.setup_game_ui()

    def setup_game_ui(self):
        self.clear_widgets()  # Clear existing widgets

        self.canvas = tk.Canvas(self.master, width=200, height=200)
        self.canvas.pack()

        self.display_word = tk.Label(self.master, text=' '.join(self.blankarr), font=("Helvetica", 24))
        self.display_word.pack(pady=20)

        self.entry = tk.Entry(self.master, font=("Helvetica", 18))
        self.entry.pack(pady=20)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.chances_label = tk.Label(self.master, text=f"Chances left: {self.chances}")
        self.chances_label.pack(pady=20)

        self.repeated_label = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.repeated_label.pack(pady=10)

        self.notification_label = tk.Label(self.master, text="", fg="red", font=("Helvetica", 12))
        self.notification_label.pack(pady=5)

        self.reset_button = tk.Button(self.master, text="Choose Another Category", command=self.setup_start_menu)
        self.reset_button.pack(pady=10)

        self.draw_hangman()  # Draw initial empty gallows

    def draw_hangman(self):
        self.canvas.delete("all")  # Clear previous drawings

        # Draw gallows
        self.canvas.create_line(30, 180, 170, 180)  # Base
        self.canvas.create_line(50, 180, 50, 30)    # Vertical post
        self.canvas.create_line(50, 30, 150, 30)    # Horizontal beam
        self.canvas.create_line(150, 30, 150, 50)    # Support beam

        # Draw stick figure based on chances
        if self.chances == 6:  # No drawing
            pass
        elif self.chances == 5:
            self.canvas.create_oval(130, 50, 170, 90)  # Head
        elif self.chances == 4:
            self.canvas.create_oval(130, 50, 170, 90)  # Head
            self.canvas.create_line(150, 90, 150, 150)  # Body
        elif self.chances == 3:
            self.canvas.create_oval(130, 50, 170, 90)  # Head
            self.canvas.create_line(150, 90, 150, 150)  # Body
            self.canvas.create_line(150, 110, 130, 130)  # Left arm
        elif self.chances == 2:
            self.canvas.create_oval(130, 50, 170, 90)  # Head
            self.canvas.create_line(150, 90, 150, 150)  # Body
            self.canvas.create_line(150, 110, 130, 130)  # Left arm
            self.canvas.create_line(150, 110, 170, 130)  # Right arm
        elif self.chances == 1:
            self.canvas.create_oval(130, 50, 170, 90)  # Head
            self.canvas.create_line(150, 90, 150, 150)  # Body
            self.canvas.create_line(150, 110, 130, 130)  # Left arm
            self.canvas.create_line(150, 110, 170, 130)  # Right arm
            self.canvas.create_line(150, 150, 130, 170)  # Left leg
        elif self.chances == 0:
            self.canvas.create_oval(130, 50, 170, 90)  # Head
            self.canvas.create_line(150, 90, 150, 150)  # Body
            self.canvas.create_line(150, 110, 130, 130)  # Left arm
            self.canvas.create_line(150, 110, 170, 130)  # Right arm
            self.canvas.create_line(150, 150, 130, 170)  # Left leg
            self.canvas.create_line(150, 150, 170, 170)  # Right leg

    def make_guess(self):
        guess = self.entry.get().lower()
        self.entry.delete(0, tk.END)

        self.notification_label.config(text="")  # Clear previous notifications

        if len(guess) != 1 or not guess.isalpha():
            self.notification_label.config(text="Invalid input. Please enter a single letter.")
            return

        if guess in self.repeated:
            self.notification_label.config(text="Letter already attempted.")
            self.update_repeated_letters()
            return

        self.repeated.append(guess)

        if guess in self.word:
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.blankarr[i] = letter
            self.display_word.config(text=' '.join(self.blankarr))
            if '_' not in self.blankarr:
                messagebox.showinfo("Congratulations", "You've guessed the word!")
                self.reset_game()
        else:
            self.chances -= 1
            self.chances_label.config(text=f"Chances left: {self.chances}")
            self.draw_hangman()  # Update hangman drawing
            if self.chances == 0:
                messagebox.showinfo("Game Over", f"You couldn't guess the word. It was: {self.word}")
                self.reset_game()

        self.update_repeated_letters()  # Update repeated letters display

    def update_repeated_letters(self):
        if not self.repeated:
            self.repeated_label.config(text="")
        else:
            self.repeated_label.config(text=f"Letters Attempted: {', '.join(self.repeated)}")

    def reset_game(self):
        self.word = ""
        self.chances = 6
        self.blankarr = []
        self.repeated.clear()
        self.update_repeated_letters()  # Reset repeated letters display
        self.notification_label.config(text="")  # Clear notifications
        self.setup_start_menu()  # Return to category selection

    def clear_widgets(self):
        for widget in self.master.winfo_children():
            widget.destroy()  # Clear existing widgets

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()