import psycopg2
from psycopg2 import OperationalError
def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Підключення до бази данних PostgreSQL пройшло успішно")
    except OperationalError as e:
        print(f"Сталася помилка '{e}'")
    return connection