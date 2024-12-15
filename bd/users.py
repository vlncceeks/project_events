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

#-----------------------------------------------------------
import sqlite3
import hashlib

# Функция для хеширования пароля
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Данные для добавления
users_data = [
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3')
]

# Подключаемся к базе данных
connection = sqlite3.connect("events.db")
cursor = connection.cursor()

# Добавляем пользователей в таблицу
for login, password in users_data:
    password_hash = hash_password(password)
    cursor.execute('''
        INSERT INTO users (login, password_hash)
        VALUES (?, ?)
    ''', (login, password_hash))

# Сохраняем изменения в базе данных
connection.commit()

# Закрываем соединение
connection.close()

print("Данные успешно добавлены!")
