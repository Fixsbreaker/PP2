import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def delete_record_by_name_or_phone(name=None, phone=None):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="PhoneBook", 
            user="postgres",
            password=os.getenv("PASSWORD"),
            port=5432
        )
        cur = conn.cursor()
        
        if name:
            # Deleting records by user name
            cur.execute("DELETE FROM contacts WHERE first_name ILIKE %s", (name,))
        elif phone:
            # Deleting entries by phone number
            cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
        
        conn.commit()
        cur.close()
        conn.close()
        
        print("The entries have been deleted successfully.")
    except Exception as e:
        print("An error has occurred:", e)

# # Пример использования функции-процедуры удаления записей по имени пользователя
# delete_record_by_name_or_phone(name="John")

# # Пример использования функции-процедуры удаления записей по номеру телефона
# delete_record_by_name_or_phone(phone="1234567890")
