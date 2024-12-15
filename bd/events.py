import sqlite3
import hashlib

connection = sqlite3.connect("events.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        description TEXT,
        materials TEXT,
        photo BLOB,
        date_time DATETIME NOT NULL,
        seats_left INTEGER NOT NULL
    )
''')

connection.commit()
connection.close()
print("Таблица мероприятий успешно создана!")