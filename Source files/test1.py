import sqlite3

db = sqlite3.connect("STC_DB.db")

cursor = db.cursor()

results = cursor.execute("select*from students")

data = results.fetchall()

for row in data:
    print(row)

db.close()
