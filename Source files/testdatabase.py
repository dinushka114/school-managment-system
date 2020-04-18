import sqlite3

db = sqlite3.connect("STC_DB.db")

cursor = db.cursor()

data = cursor.execute("select*from user")

for row in data:
    print(row[0])

db.close()
