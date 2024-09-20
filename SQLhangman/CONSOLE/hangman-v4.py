import random
import sqlite3
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from kivy.graphics import Color, Line, Ellipse


def decrypt(encrypted_base64):
    key = "s4$t%%2rW@kL9&xZ".encode('utf-8')
    encrypted_data = base64.b64decode(encrypted_base64)
    iv = encrypted_data[:AES.block_size]
    encrypted = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted)
    return unpad(decrypted_padded, AES.block_size).decode('utf-8')

def get_words(category_name, column_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f'SELECT "{column_name}" FROM "{category_name}"'
    try:
        cursor.execute(query)
        return [row[0] for row in cursor.fetchall()]
    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()

class HangmanGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.word = ""
        self.chances = 6
        self.blankarr = []
        self.repeated = []

        self.category_label = Label(text="Select a category:")
        self.add_widget(self.category_label)

        self.category_dropdown = DropDown()
        self.category_var = Label(text="Choose a category", size_hint_y=None, height=44)
        self.category_var.bind(on_release=self.category_dropdown.open)
        self.add_widget(self.category_var)

        categories = self.get_categories()
        for category in categories:
            btn = Button(text=category, size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.select_category(btn.text))
            self.category_dropdown.add_widget(btn)

        self.start_button = Button(text="Start Game", on_press=self.start_game)
        self.add_widget(self.start_button)

        self.canvas = self.create_canvas()
        self.add_widget(self.canvas)

    def create_canvas(self):
        canvas = BoxLayout(size_hint_y=None, height=300)
        canvas.bind(size=self.update_canvas_size)
        return canvas

    def update_canvas_size(self, instance, size):
        self.draw_hangman()

    def get_categories(self):
        return get_words('sqlite_sequence', 'name')

    def select_category(self, category):
        self.category_var.text = category
        self.category_dropdown.dismiss()

    def start_game(self, instance):
        category_name = self.category_var.text
        if category_name == "Choose a category":
            self.show_popup("Selection Error", "Please select a valid category.")
            return

        wordlist = get_words(category_name, 'cipher')
        if not wordlist:
            self.show_popup("No Words", "No words found for this category.")
            return

        self.word = decrypt(random.choice(wordlist))
        self.chances = 6
        self.blankarr = ['_' if c.isalpha() else c for c in self.word]
        self.repeated = []

        self.setup_game_ui()

    def setup_game_ui(self):
        self.clear_widgets()
        self.add_widget(Label(text=' '.join(self.blankarr), font_size='24sp'))
        self.chances_label = Label(text=f"Chances left: {self.chances}")
        self.add_widget(self.chances_label)

        self.create_keyboard()
        self.reset_button = Button(text="Choose Another Category", on_press=self.setup_start_menu)
        self.add_widget(self.reset_button)

        self.draw_hangman()

    def draw_hangman(self):
        self.canvas.clear_widgets()
        with self.canvas.canvas:
            Color(0, 0, 0)  # Black color
            # Base
            Line(points=[30, 50, 170, 50])
            Line(points=[50, 50, 50, 30])
            Line(points=[50, 30, 150, 30])
            Line(points=[150, 30, 150, 50])

            # Draw the hangman based on chances
            if self.chances < 6:
                Ellipse(pos=(130, 50), size=(40, 40))  # Head
            if self.chances < 5:
                Line(points=[150, 90, 150, 150])  # Body
            if self.chances < 4:
                Line(points=[150, 110, 130, 130])  # Left arm
            if self.chances < 3:
                Line(points=[150, 110, 170, 130])  # Right arm
            if self.chances < 2:
                Line(points=[150, 150, 130, 170])  # Left leg
            if self.chances < 1:
                Line(points=[150, 150, 170, 170])  # Right leg

    def create_keyboard(self):
        keyboard_layout = BoxLayout(size_hint_y=None, height=50)
        keys = "qwertyuiopasdfghjklzxcvbnm"
        for letter in keys:
            button = Button(text=letter, on_press=lambda btn: self.make_guess(btn.text))
            keyboard_layout.add_widget(button)
        self.add_widget(keyboard_layout)

    def make_guess(self, guess):
        if guess in self.repeated:
            self.show_popup("Already Guessed", "Letter already attempted.")
            return

        self.repeated.append(guess)
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.blankarr[i] = letter
        self.chances -= 1

        if '_' not in self.blankarr:
            self.show_popup("Congratulations", "You've guessed the word!")
            self.reset_game()
        elif self.chances <= 0:
            self.show_popup("Game Over", f"The word was: {self.word}")
            self.reset_game()

        self.chances_label.text = f"Chances left: {self.chances}"
        self.draw_hangman()

    def reset_game(self):
        self.word = ""
        self.chances = 6
        self.blankarr = []
        self.repeated.clear()
        self.setup_start_menu()

    def setup_start_menu(self):
        self.clear_widgets()
        self.__init__()

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()

class HangmanApp(App):
    def build(self):
        return HangmanGame()

if __name__ == "__main__":
    HangmanApp().run()
