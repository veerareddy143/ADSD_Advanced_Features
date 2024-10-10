import sqlite3
conn = sqlite3.connect('notnull.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE users (user_id INTEGER PRIMARY KEY,username TEXT NOT NULL,email TEXT NOT NULL);''')
cursor.execute('INSERT INTO users (user_id, username, email) VALUES (1, "veera", "veera17@example.com");')
cursor.execute('INSERT INTO users (user_id, username, email) VALUES (2, "Manu", "manu17@example.com");')
# Try to insert a user with a NULL username
try:
    cursor.execute('INSERT INTO users (user_id, username, email) VALUES (3, NULL, "gopi12@example.com");')
except sqlite3.IntegrityError as e:
    print("Error:", e)  
# Try to insert a user with a NULL email
try:
    cursor.execute('INSERT INTO users (user_id, username, email) VALUES (4, "naveen", NULL);')
except sqlite3.IntegrityError as e:
    print("Error:", e) 
print("\n Current data in the users table:")
cursor.execute('SELECT * FROM users')
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()