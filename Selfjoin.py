import sqlite3
conn = sqlite3.connect('SelfJoin.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        manager_id INTEGER,
        FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
    );
''')
cursor.executemany('''
    INSERT INTO employees (employee_id, employee_name, manager_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Veera', None),       
    (2, 'Manu', 1),         
    (3, 'Gopi', 1),      
    (4, 'Naveen', 2),          
    (5, 'Thiru', 2),      
    (6, 'Lalith', 3)         
])
cursor.execute("Select *from employees")
print("\n Employees Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 
cursor.execute('''
    SELECT e.employee_name AS Employee, m.employee_name AS Manager
    FROM employees e
    LEFT JOIN employees m ON e.manager_id = m.employee_id;
''')
rows = cursor.fetchall()
print("\n Self Join \n")
for row in rows:
    print(row) 
conn.commit()
conn.close()