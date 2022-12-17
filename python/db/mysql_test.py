from getpass import getpass
from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="myproject",
        auth_plugin='mysql_native_password',
    ) as connection:
        print("Connected to DataBase!")
        sql = "CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), price DECIMAL(7,2), category INT(2));"
        with connection.cursor() as cursor:
            cursor.execute(sql)

except Error as e:
    print(e)