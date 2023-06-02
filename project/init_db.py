import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

#cur = connection.cursor()

#cur.execute("INSERT INTO User (firstName, lastName, userName, password) VALUES (?, ?, ?, ?)")
#cur.execute("INSERT INTO Item (category, color, season, style, fit) VALUES (?, ?, ?, ?, ?)")
#cur.execute("INSERT INTO Closet (closet_name, user_id) VALUES (?, ?)")

            
print("script executed")
connection.commit()
print("committed")
connection.close()
print("closed")