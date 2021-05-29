import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (Name, Post) VALUES (?, ?)",
            ('Your Name','You can see your posts here')
            )

#cur.execute("INSERT INTO posts (Name, Post) VALUES (?, ?)"
 #           )

connection.commit()
connection.close()