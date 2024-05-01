import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

# создание процедуры для добавления нового пользователя по имени и телефону, обновление телефона, если пользователь уже существует
def update_phone_if_user_exists(username, new_phone):
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="phones",
            user="postgres",
            password=os.getenv("PASSWORD"),
            port=5432
        )
        cur = conn.cursor()

        cur.execute("SELECT * FROM contacts WHERE username = %s", (username,))
        user = cur.fetchone()

        if user:
            # Обновление телефона, если пользователь существует
            cur.execute("UPDATE contacts SET phone = %s WHERE username = %s", (new_phone, username))
            conn.commit()
            print(f"Phone number for {username} updated.")
        else:
            # Добавление нового пользователя, если пользователь не найден
            cur.execute("INSERT INTO contacts (username, phone) VALUES (%s, %s)", (username, new_phone))
            conn.commit()
            print(f"New user {username} added with phone number {new_phone}.")

        conn.close()
    except Exception as e:
        print("An error occurred:", e)


username = input("Input username: ")
new_phone = input("Input phone number: ")

update_phone_if_user_exists(username, new_phone)
