import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()
try:
    # Створення таблиці Клієнти
    create_table_query = """
    DROP TABLE IF EXISTS Clients,Products,Sales;
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці ExamResults: {e}")