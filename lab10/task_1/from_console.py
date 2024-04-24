import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def add_contact(first_name, second_name, phone):
    conn = psycopg2.connect(
        host="localhost",
        dbname="PhoneBook",
        user="postgres",
        password=os.getenv("PASSWORD"),
        port=5432
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (first_name, second_name, phone) VALUES (%s, %s, %s)", (first_name, second_name, phone))
    conn.commit()
    conn.close()

first_name = input()
second_name = input()
phone = input()
add_contact(first_name, second_name, phone)
