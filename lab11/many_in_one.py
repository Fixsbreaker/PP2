import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def search_records(pattern):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="PhoneBook", 
            user="postgres",
            password=os.getenv("PASSWORD"),
            port=5432
        )
        cur = conn.cursor()
        
        req = "SELECT * FROM contacts WHERE first_name ILIKE %s OR second_name ILIKE %s OR phone LIKE %s"
        cur.execute(req, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))


        
        res = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return res
    except Exception as e:
        print("An error has occurred:", e)

def add_users(users):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="PhoneBook", 
            user="postgres",
            password=os.getenv("PASSWORD"),
            port=5432
        )
        cur = conn.cursor()
        
        invalid_data = []
        
        for user in users:
            if len(user[2]) != 7:  # Проверяем длину телефонного номера
                invalid_data.append(user)
            else:
                try:
                    cur.execute("INSERT INTO contacts (first_name, second_name, phone) VALUES (%s, %s, %s)", user)
                    conn.commit()
                except Exception as e:
                    print("Error when adding a user:", e)
        
        cur.close()
        conn.close()
        
        return invalid_data
    except Exception as e:
        print("An error has occurred:", e)


# Пример использования функции поиска записей
pattern = input("Enter the search template: ")
matching_records = search_records(pattern)
if matching_records:
    for record in matching_records:
        print(record)
else:
    print("No records found.")

# Пример использования функции добавления пользователей
users_to_add = [("Albert", "Vrrr", "1111111111"), ("Kolkey", "Kernet", "293485"), ("Soket", "Vin", "2943575"), ("Lor", "Bor", "123456789")]
invalid_data = add_users(users_to_add)
if invalid_data:
    print("The following data is incorrect:")
    for data in invalid_data:
        print(data)
else:
    print("Users have been successfully added.")
