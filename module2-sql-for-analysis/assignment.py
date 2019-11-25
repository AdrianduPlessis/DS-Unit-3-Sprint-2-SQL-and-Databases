import sqlite3
import psycopg2

host = 'salt.db.elephantsql.com'
user = 'rzeqtyzf'
database = 'rzeqtyzf'
password = 'homoy3tk4FnkiRVZ44zLU7qjFFqRjuuO'

pg_conn = psycopg2.connect(database=database, user=user, password=password, host=host)
pg_cur = pg_conn.cursor()


create_shippers_table = """
CREATE TABLE Shippers(
   ShipperID serial PRIMARY KEY,
   CompanyName VARCHAR (200) NOT NULL,
   Phone VARCHAR (20) NOT NULL
);
"""

