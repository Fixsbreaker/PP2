import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def delete_contact_by_name(name):
    conn = psycopg2.connect(
        dbname="PhoneBook",
        user="postgres",
        password=os.getenv("PASSWORD"),
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE first_name = %s OR second_name = %s", (name, name))
    conn.commit()
    conn.close()

def delete_contact_by_phone(phone):
    conn = psycopg2.connect(
        dbname="PhoneBook",
        user="postgres",
        password=os.getenv("PASSWORD"),
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
    conn.commit()
    conn.close()

delete_contact_by_name('name')
delete_contact_by_phone('phone')
