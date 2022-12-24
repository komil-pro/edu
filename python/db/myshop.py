# from getpass import getpass
# from mysql.connector import connect, Error

# try:
#     with connect(
#         host="localhost",
#         user=input("Enter username: "), # python
#         password=getpass("Enter password: "), # Python3
#         database="shop1",
#         auth_plugin='mysql_native_password',
#     ) as connection:
#         print("Connected to DataBase!")
#         sql = "SELECT * FROM suppliers LIMIT 100"
#         with connection.cursor() as cursor:
#             cursor.execute(sql)
#             result = cursor.fetchall()
#             for row in result:
#                 print(row)
# except Error as e:
#     print(e)
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="Python3",
  database="shop1"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM suppliers LIMIT 50")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)