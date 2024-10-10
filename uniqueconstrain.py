import sqlite3
conn = sqlite3.connect('unique_constrain.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE users ( user_id INTEGER PRIMARY KEY, user_name TEXT NOT NULL, email TEXT NOT NULL UNIQUE); ''')
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (1, 'Veera', 'veera17@example.com');''')
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (2, 'Manu', 'manu17@example.com');''')

cursor.execute('''select *from users;''')
print(cursor.fetchall())

# Trying to insert a user with the same email (Error Conditions)
cursor.execute('''INSERT INTO users (user_id, user_name, email) VALUES (3, 'Jake Doe', 'john.doe@example.com');''')  

conn.commit()
conn.close()