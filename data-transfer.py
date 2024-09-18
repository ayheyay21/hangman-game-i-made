import sqlite3
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

