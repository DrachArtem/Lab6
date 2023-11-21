import Connection

# Підключення до бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Створення таблиці Клієнти
    create_table_query = """
    CREATE TABLE Clients (
            ClientCode SERIAL PRIMARY KEY,
            CompanyName VARCHAR(255),
            LegalPerson BOOLEAN,
            Address VARCHAR(255),
            Phone VARCHAR(17),
            ContactPerson VARCHAR(255),
            BankAccount VARCHAR(20)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Клієнти: {e}")

try:
    # Створення таблиці Товари
    create_table_query = """
    CREATE TABLE Products (
            ProductCode SERIAL PRIMARY KEY,
            ProductName VARCHAR(255),
            Price DECIMAL(10, 2),
            Quantity INTEGER
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Товари: {e}")

try:
    # Створення таблиці Продаж товарів
    create_table_query = """
    CREATE TABLE Sales (
            SaleCode SERIAL PRIMARY KEY,
            SaleDate DATE,
            ClientCode INTEGER REFERENCES Clients(ClientCode),
            ProductCode INTEGER REFERENCES Products(ProductCode),
            QuantitySold INTEGER,
            Discount DECIMAL(5, 2) CHECK (Discount >= 3 AND Discount <= 20),
            PaymentMethod VARCHAR(20) CHECK (PaymentMethod IN ('Cash', 'Non-cash')),
            NeedDelivery BOOLEAN,
            DeliveryCost DECIMAL(10, 2)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці Продаж товарів: {e}")

    cursor.close()
    connection.close()
