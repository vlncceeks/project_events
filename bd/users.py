import sqlite3
import hashlib

connection = sqlite3.connect("events.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL
    )
''')

connection.commit()
connection.close()
print("База данных и таблица успешно созданы!")