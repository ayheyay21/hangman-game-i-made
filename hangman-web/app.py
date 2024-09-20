from flask import Flask, render_template, request, redirect, url_for, session
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import sqlite3
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

HANGMAN_DIAGRAMS = [
    ['     ______ ', "    |      |", '           |', '           |', '           |', '   ---------'],  # 6 chances
    ['     ______ ', "    |      |", '    O      |', '           |', '           |', '   ---------'],  # 5 chances
    ['     ______ ', "    |      |", '    O      |', '    |      |', '           |', '   ---------'],  # 4 chances
    ['     ______ ', "    |      |", '    O      |', '   /|      |', '           |', '   ---------'],  # 3 chances
    ['     ______ ', "    |      |", '    O      |', '   /|\\     |', '           |', '   ---------'],  # 2 chances
    ['     ______ ', "    |      |", '    O      |', '   /|\\     |', '   /       |', '   ---------'],  # 1 chance
    ['     ______ ', "    |      |", '    O      |', '   /|\\     |', '   / \\     |', '   ---------'],  # 0 chances
]


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


def get_words(category_name, column_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f'SELECT "{column_name}" FROM "{category_name}"'

    cursor.execute(query)
    words = [row[0] for row in cursor.fetchall()]
    conn.close()
    return words


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = request.form['category']
        wordlist = get_words(category, 'cipher')
        word = decrypt(random.choice(wordlist))
        session['word'] = word
        session['chances'] = 6
        session['guessed_letters'] = []
        return redirect(url_for('game'))

    categories = get_words('sqlite_sequence', 'name')
    return render_template('index.html', categories=categories)


@app.route('/game', methods=['GET', 'POST'])
def game():
    # Check if 'word' is in session; if not, redirect to the index
    if 'word' not in session:
        return redirect(url_for('index'))

    word = session['word']
    chances = session['chances']
    guessed_letters = session['guessed_letters']

    if request.method == 'POST':
        guess = request.form['guess'].lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            guessed_letters.append(guess)
            session['guessed_letters'] = guessed_letters

            if guess not in word:
                chances -= 1

            session['chances'] = chances

        if chances <= 0 or all(letter in guessed_letters or letter == ' ' for letter in word):
            return redirect(url_for('result'))

    hangman_diagram = HANGMAN_DIAGRAMS[6 - chances]

    # Prepare the display word with spaces preserved
    displayed_word = ''.join([letter if letter in guessed_letters or letter == ' ' else '_' for letter in word])

    return render_template('game.html', word=displayed_word, chances=chances, guessed_letters=guessed_letters,
                           hangman_diagram=hangman_diagram)


@app.route('/result')
def result():
    word = session['word']
    chances = session['chances']
    return render_template('result.html', word=word, chances=chances)


@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
