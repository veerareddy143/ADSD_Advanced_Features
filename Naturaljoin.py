import sqlite3
conn = sqlite3.connect('Natural_join.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL
    );
''')

cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        order_date TEXT NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    );
''')

cursor.executemany('''
    INSERT INTO customers (customer_id, customer_name) 
    VALUES (?, ?);
''', [
    (1, 'Veera'),
    (2, 'Manu'),
    (3, 'Gopi'),
    
])

cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, order_date) 
    VALUES (?, ?, ?);
''', [
    (101, 1, '2023-02-12'),  
    (102, 2, '2023-03-11'),  
    (103, 1, '2023-05-3'),  
    (104, 3, '2023-07-10')   
])

cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT * 
    FROM customers
    NATURAL JOIN orders;
''')

print("\n Natural Join \n")
rows = cursor.fetchall()
print("Customer Name | Order ID | Order Date")
print("-------------------------------------")
for row in rows:
    customer_name = row[1]  
    order_id = row[2]       
    order_date = row[3]    
    print(f"{customer_name:<14} | {order_id:<8} | {order_date}")

conn.commit()
conn.close()