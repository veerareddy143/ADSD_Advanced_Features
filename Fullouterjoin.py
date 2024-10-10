import sqlite3
conn = sqlite3.connect('Fullouterjoin.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE employees (
        employee_id INTEGER PRIMARY KEY,
        employee_name TEXT NOT NULL,
        department_id INTEGER,
        FOREIGN KEY (department_id) REFERENCES departments(department_id)
    );
''')

cursor.execute('''
    CREATE TABLE departments (
        department_id INTEGER PRIMARY KEY,
        department_name TEXT NOT NULL
    );
''')

cursor.executemany('''
    INSERT INTO departments (department_id, department_name) 
    VALUES (?, ?);
''', [
    (1, 'Engineering'),
    (2, 'AI_ML'),
    (3, 'HR'),
    (4, 'Marketing')
])

cursor.execute("Select *from departments")
print("\n Departments Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.executemany('''
    INSERT INTO employees (employee_id, employee_name, department_id) 
    VALUES (?, ?, ?);
''', [
    (1, 'Veera', 1),      
    (2, ' Manu', 2),     
    (3, 'Gopi', None),  
    (4, 'Naveen', 3)      
])

cursor.execute("Select *from employees")
print("\n Employees Table\n")
rows = cursor.fetchall()
for row in rows:
    print(row) 

cursor.execute('''
    SELECT employees.employee_name, departments.department_name
    FROM employees
    LEFT JOIN departments ON employees.department_id = departments.department_id

    UNION

    SELECT employees.employee_name, departments.department_name
    FROM departments
    LEFT JOIN employees ON employees.department_id = departments.department_id;
''')

print("\n Full Outer Join \n")
rows = cursor.fetchall()
for row in rows:
    print(rows)

conn.commit()
conn.close()