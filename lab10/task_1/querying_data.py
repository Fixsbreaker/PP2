import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def query_contacts():
    conn = psycopg2.connect(
        host="localhost",
        dbname="PhoneBook",
        user="postgres",
        password=os.getenv("PASSWORD"),
        port=5432
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Запрос всех контактов и вывод на экран
query_contacts()
