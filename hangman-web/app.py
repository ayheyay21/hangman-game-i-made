from flask import Flask, render_template, request, redirect, flash
import random
import sqlite3
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
from flask import session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a more secure key


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


@app.route('/')
def index():
    categories = get_words('sqlite_sequence', 'name')
    return render_template('index.html', categories=categories)


@app.route('/start', methods=['POST'])
def start_game():
    if request.method == 'POST':
        category_name = request.form.get('category')
        if category_name == "Choose a category":
            flash("Please select a valid category.")
            return redirect('/')

        wordlist = get_words(category_name, 'cipher')
        if not wordlist:
            flash("No words found for this category.")
            return redirect('/')

        word = decrypt(random.choice(wordlist))
        session['current_word'] = word  # Store the word in the session
        session['chances'] = 6  # Reset chances
        session['guessed_letters'] = []  # Reset guessed letters

        return render_template('game.html', word=' '.join(['_' for _ in word]), chances=session['chances'])
    else:
        flash("Invalid request method.")
        return redirect('/')


@app.route('/guess', methods=['POST'])
def make_guess():
    guess = request.form['guess']
    word = session.get('current_word')
    chances = session.get('chances', 6)
    guessed_letters = session.get('guessed_letters', [])

    if guess in guessed_letters:
        flash("Letter already guessed.")
    else:
        guessed_letters.append(guess)
        session['guessed_letters'] = guessed_letters

        if guess not in word:
            chances -= 1

    session['chances'] = chances

    if '_' not in ''.join(['_' if letter not in guessed_letters else letter for letter in word]):
        flash("Congratulations, you've guessed the word!")
        return redirect('/')

    if chances <= 0:
        flash(f"Game Over! The word was: {word}")
        return redirect('/')

    session['current_word'] = word
    return render_template('game.html', word=' '.join(['_' if letter not in guessed_letters else letter for letter in word]), chances=chances)


if __name__ == '__main__':
    app.run(debug=True)
