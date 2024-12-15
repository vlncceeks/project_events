import sqlite3
import json

# Подключаемся к базе данных
connection = sqlite3.connect("events.db")

# Включаем возможность работы с именами столбцов
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

# Выполняем запрос для получения всех данных из таблицы users
cursor.execute("SELECT * FROM users")

# Извлекаем все строки результата (будут в формате Row)
rows = cursor.fetchall()

# Преобразуем строки в словари
users_list = [dict(row) for row in rows]

# Преобразуем данные в JSON (для использования как API)
json_data = json.dumps(users_list, indent=4)

# Печатаем JSON
print(json_data)

# Закрываем соединение
connection.close()
