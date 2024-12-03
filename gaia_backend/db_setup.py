import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT)''')
    conn.commit()
    conn.close()

def save_user(username, email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)', (username, email, password))
    conn.commit()
    conn.close()

create_db()

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if username and email and password:
        save_user(username, email, password)
        return jsonify({'message': 'User registered successfully'}), 200
    else:
        return jsonify({'error': 'Missing data'}), 400