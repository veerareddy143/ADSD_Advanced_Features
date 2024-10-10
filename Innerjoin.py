import sqlite3
connection = sqlite3.connect('Cust_mer_orders.db')
cursor = connection.cursor()
# Creating customers table
cursor.execute('''CREATE TABLE IF NOT EXISTS customers ( customer_id INTEGER PRIMARY KEY,customer_name TEXT NOT NULL);''')
# Creating the orders table
cursor.execute('''CREATE TABLE IF NOT EXISTS orders ( order_id INTEGER PRIMARY KEY,customer_id INTEGER,
               product_name TEXT NOT NULL,FOREIGN KEY (customer_id) REFERENCES customers(customer_id));''')
# Inserting records into customer table 
cursor.executemany('''INSERT INTO customers (customer_id, customer_name) VALUES (?, ?);''', [
    (1, 'Veera'),
    (2, 'Manu'),
    (3, 'Gopi'),
    (4, 'Naveen'),
    (5, 'Thiru')
])
# Selecting the Records from customers table
cursor.execute("Select *from customers")
print("\n Customers Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row)
# Inserting records into the orders table
cursor.executemany('''
    INSERT INTO orders (order_id, customer_id, product_name) VALUES (?, ?, ?);''', [
    (101, 1, 'IPhone'),
    (102, 2, 'Smartphone'),
    (103, 1, 'Android'),
    (104, 3, 'Earpods'),
    (105, 4, 'Watch'),
    (106, 5, 'Camera'),
    (107, 3, 'Headphones'),
    (108, 2, 'Laptop')
])
# Selecting the Records from orders table
cursor.execute("Select *from orders")
print("\n Orders Table \n")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.execute('''SELECT customers.customer_name, orders.product_name FROM customers 
               INNER JOIN orders ON customers.customer_id = orders.customer_id;''')
print("\n Inner Join \n")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
connection.close()