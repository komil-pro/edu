import sqlite3
'''
Некоторые полезные SQL запросы:
# создание новой БД
sqlite3 sqlite_db1.db
'''
connection = sqlite3.connect("sqlite_db1.db") # соединение с базой данных
cursor = connection.cursor()
#print(connection.total_changes) # проверяем создан ли успешно объект connection


# создание новой таблицы
#cursor.execute("CREATE TABLE students (name TEXT, age INTEGER, phone TEXT, email TEXT)")
# добавление данных
#cursor.execute("INSERT INTO students VALUES ('Zebo', 21, 93123123,'zebo@univer.tj')")
#cursor.execute("INSERT INTO students VALUES ('Сухроб', 22, 98012345,'suhrob@univer.tj')")
# получение данных
rows = cursor.execute("SELECT name, phone, email FROM students").fetchall()
print('-'*20)
print(rows)
print('-'*20)
# вариант выборки с критериями
target_student_name = "Сухроб"
rows = cursor.execute(
    "SELECT name, age, email FROM students WHERE name = ?",
    (target_student_name,),
).fetchall()
print('-'*20)
print(rows)
print('-'*20)
#connection.commit()