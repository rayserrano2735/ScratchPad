# Python Driver for PostgreSQL
import psycopg2

# Configure connection to PostgreSQL
conn = psycopg2.connect(
    host="172.31.57.149",
    database="dvdrental",
    user="rserrano",
    password="test123")

conn = psycopg2.connect("host= 172.31.57.149 dbname=dvdrental user=rserrano password=test123")

# create a cursor
cur = conn.cursor()

# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = cur.fetchone()
print(db_version)

# First PostgreSQL query from Python
cur.execute('select customer_id, last_name from customer')
customer_data = cur.fetchone()
print(customer_data)

# close the communication with the PostgreSQL
cur.close()
