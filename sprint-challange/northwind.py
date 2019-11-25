import sqlite3

# Part 3

# What are the ten most expensive items (per unit price) in the database and their suppliers?
CONN = sqlite3.connect('northwind_small.sqlite3')
curs = CONN.cursor()

query = """SELECT Product.ProductName, Supplier.CompanyName
        FROM Product
        INNER JOIN Supplier ON Product.SupplierID=Supplier.Id
        ORDER BY UnitPrice
        LIMIT 10"""

high_end_suppliers = curs.execute(query).fetchall()
print(high_end_suppliers)

# What is the largest category (by number of unique products in it)?
# TODO Complete with single query
query = """SELECT CategoryID
           FROM Product
           GROUP BY CategoryID
           ORDER BY COUNT(*) DESC
           LIMIT 1"""
most_popular_catID = curs.execute(query).fetchall()[0][0]

query = f"""SELECT CategoryName
            FROM Category
            WHERE Id={most_popular_catID}"""

most_popular_category = curs.execute(query).fetchall()[0][0]

print('The most popular product category is', most_popular_category)