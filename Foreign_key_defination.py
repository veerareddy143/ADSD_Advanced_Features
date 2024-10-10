import sqlite3
conn = sqlite3.connect('Foreignkey_Definition.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE authors (
        author_id INTEGER PRIMARY KEY,
        author_name TEXT NOT NULL);''')

cursor.execute('''
    CREATE TABLE books (
        book_id INTEGER PRIMARY KEY,
        book_title TEXT NOT NULL,
        author_id INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(author_id));''')

cursor.executemany('''
    INSERT INTO authors (author_id, author_name) 
    VALUES (?, ?);''', [
    (1, 'Br KCR'),
    (2, 'Swamy vivekanandha'),
    (3, 'Jr Rasidh')])

cursor.execute("Select *from authors")
print("\n Author Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO books (book_id, book_title, author_id) 
    VALUES (?, ?, ?);''', [
    (1, 'The KCR', 1),           
    (2, 'A man in tha forest', 2),      
    (3, 'Little hooks', 3)])

cursor.execute("Select *from books")
print("\n Books Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
    
conn.commit()
conn.close()