import sqlite3

connection = sqlite3.connect("games.db")
cursor = connection.cursor()


cursor.execute("SELECT * FROM games")
print(cursor.fetchall())