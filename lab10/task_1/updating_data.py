import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def update_contact_name(old_name, new_name):
    conn = psycopg2.connect(
        dbname="PhoneBook",
        user="postgres",
        password=os.getenv("PASSWORD"),
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET first_name = %s WHERE first_name = %s", (new_name, old_name))
    cur.execute("UPDATE contacts SET second_name = %s WHERE second_name = %s", (new_name, old_name))
    conn.commit()
    conn.close()

def update_contact_phone(name, new_phone):
    conn = psycopg2.connect(
        dbname="PhoneBook",
        user="postgres",
        password=os.getenv("PASSWORD"),
        host="localhost"
    )
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET phone = %s WHERE first_name = %s OR second_name = %s", (new_phone, name, name))
    conn.commit()
    conn.close()

update_contact_name('old_name', 'new_name')
update_contact_phone('name', 'new_phone')
