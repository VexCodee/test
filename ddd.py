import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
             )''')

# Dodaj użytkownika admin (dla celów demonstracyjnych)
admin_username = 'admin'
admin_password = 'admin123'
c.execute('INSERT INTO users (username, password) VALUES (?, ?)',
          (admin_username, generate_password_hash(admin_password)))

conn.commit()
conn.close()