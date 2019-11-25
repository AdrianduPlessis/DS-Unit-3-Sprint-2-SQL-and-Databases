import sqlite3


def create_db(CONN):
    """Creates the Person table."""
    curs = CONN.cursor()
    query = '''CREATE TABLE demo(
                    s CHAR,
                    x INTEGER,
                    y INTEGER);'''
    curs.execute(query)
    CONN.commit()
    # CONN.close()


def insert_and_query(CONN):
    """Write and execute appropriate INSERT INTO statements to add the data"""
    curs = CONN.cursor()

    #TODO Make Dry
    """entries = [['g', 3, 9],
               ['v', 5, 7],
               ['f', 8, 7]]
    for entry in entries:
        #insert_query = "INSERT INTO demo VALUES ('g',3,9)"
        insert_query = f"INSERT INTO demo (s, x, y) VALUES ({entry[0]}, {entry[1]}, {entry[2]})"
        curs.execute(insert_query)
        #print(entry[0])
    CONN.commit()
    print(curs.execute('SELECT * FROM demo;').fetchall())
    """

    insert_query = "INSERT INTO demo VALUES ('g',3,9)"
    curs.execute(insert_query)
    insert_query = "INSERT INTO demo VALUES ('v',5,7)"
    curs.execute(insert_query)
    insert_query = "INSERT INTO demo VALUES ('g',8,7)"
    curs.execute(insert_query)
    CONN.commit()


# Part 1
CONN = sqlite3.connect('demo_data.sqlite3')
# Only run on first pass
create_db(CONN)
curs = CONN.cursor()
insert_and_query(CONN)

#Testing
#Count how many rows you have - it should be 3!
query = """SELECT COUNT(s) FROM demo"""
num_rows = curs.execute(query).fetchone()[0]
print('I have', num_rows, 'rows in my demo.')

#How many rows are there where both x and y are at least 5?
query = """SELECT COUNT(s) 
            FROM demo
            WHERE x >= 5 AND y >= 5"""
num_rows = curs.execute(query).fetchone()[0]
print('I have', num_rows, 'rows, where both x and y are at least 5, in my demo.')

#How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
query = """SELECT COUNT(DISTINCT(y)) 
            FROM demo"""
num_rows = curs.execute(query).fetchone()[0]
print('I have', num_rows, 'unique values of y, in my demo.')

# Part 2

# What are the ten most expensive items (per unit price) in the database?
CONN2 = sqlite3.connect('northwind_small.sqlite3')
curs2 = CONN2.cursor()

query = """SELECT ProductName
            FROM Product
            ORDER BY  UnitPrice DESC
            LIMIT 10"""
expensive_products = curs2.execute(query).fetchall()
print(expensive_products)

# What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
query = """SELECT AVG(HireDate-BirthDate)
            FROM Employee"""
average_age = curs2.execute(query).fetchall()[0][0]
print(average_age)

# Stretch
# How does the average age of employee at hire vary by city?

curs.close()
curs2.close()

#OUTPUT:
"""
I have 3 rows in my demo.
I have 2 rows, where both x and y are at least 5, in my demo.
I have 2 unique values of y, in my demo.
[('Côte de Blaye',), ('Thüringer Rostbratwurst',), ('Mishi Kobe Niku',), ("Sir Rodney's Marmalade",), ('Carnarvon Tigers',), ('Raclette Courdavault',), ('Manjimup Dried Apples',), ('Tarte au sucre',), ('Ipoh Coffee',), ('Rössle Sauerkraut',)]
37.22222222222222
"""



