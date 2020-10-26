from test import a

# db = pymysql.connect("localhost", "root", "374563", "course")
# cursor = db.cursor()
# cursor.execute("SELECT * FROM Student")
# print(cursor.fetchall())

a = {1:1,2:2}
print(a.get(3,4))