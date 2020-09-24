import pymysql

db = pymysql.connect("localhost", "root", "374563", "course")
cursor = db.cursor()
cursor.execute("SELECT * FROM Student")
print(cursor.fetchall())
