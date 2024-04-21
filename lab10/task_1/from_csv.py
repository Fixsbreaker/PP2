import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    dbname="PhoneBook",
    user="postgres",
    password=os.getenv("PASSWORD"),
    port=5432
)

cur = conn.cursor()

with open('data.csv', 'r') as f:
    next(f) 
    cur.copy_from(f, 'contacts', sep=',', columns=('first_name', 'second_name', 'phone'))

conn.commit()
conn.close()
