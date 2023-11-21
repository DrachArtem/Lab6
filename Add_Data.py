import Connection

#Подключение к базе данных
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:


    # Додавання клієнтів
    clients_data = [
        (1, 'Дмитро', True, 'Київ', '+38(063)-333-2354', 'Dmytro@gmail.com', '1234567890'),
        (2, 'Назар', False, 'Корсунь-Шевченківський', '+38(098)-444-2464', 'Nazar@gmail.com', '0987654321'),
        (3, 'Артем', True, 'Київ', '+38(063)-555-6565', 'Artem@gmail.com', '9876543210'),
        (4, 'Марія', False, 'Черкаси', '+38(098)-666-8699', 'Maria@gmail.com', '2454364934'),
    ]

    insert_query = """
    INSERT INTO Clients (ClientCode, CompanyName, LegalPerson, Address, Phone, ContactPerson, BankAccount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (ClientCode) DO UPDATE
            SET Address = EXCLUDED.Address, Phone = EXCLUDED.Phone, ContactPerson = EXCLUDED.ContactPerson, BankAccount = EXCLUDED.BankAccount
    """

    for record in clients_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Клієнт: {e}")

try:

    # Додавання продуктів
    products_data = [
        (1, 'Сир', 10.99, 100),
        (2, 'Ковбаса', 25.50, 50),
        (3, 'Кола', 2.99, 200),
        (4, 'Печиво', 8.99, 250),
        (5, 'Багет', 10.25, 125),
        (6, 'Макарони', 3.99, 150),
        (7, 'Рис', 4.99, 400),
        (8, 'Гречка', 5.99, 300),
        (9, 'Сахар', 2.99, 330),
        (10, 'Олива', 5.99, 425),
    ]

    insert_query = """
     INSERT INTO Products (ProductCode, ProductName, Price, Quantity)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (ProductCode) DO NOTHING
    """

    for record in products_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Товари: {e}")

try:

    # Додавання продаж товарів
    sales_data = [
        (1, '2023-11-18', 1, 2, 5, 10, 'Cash', True, 5.00),
        (2, '2023-11-19', 2, 3, 5, 3, 'Non-cash', False, 1.00),
        (3, '2023-11-20', 1, 4, 5, 5, 'Cash', True, 7.00),
        (4, '2023-11-21', 2, 5, 5, 4, 'Non-cash', True, 6.00),
        (5, '2023-11-22', 3, 6, 5, 6, 'Non-cash', False, 1.00),
        (6, '2023-11-23', 4, 7, 5, 7, 'Cash', True, 2.00),
        (7, '2023-11-24', 1, 8, 5, 20, 'Cash', True, 69.00),
        (8, '2023-11-25', 2, 9, 5, 16, 'Cash', False, 56.00),
        (9, '2023-11-26', 3, 10, 5, 17, 'Non-cash', True, 79.00),
        (10, '2023-11-27', 4, 1, 5, 19, 'Cash', True, 22.00),
        (11, '2023-11-28', 1, 2, 5, 11, 'Cash', False, 54.00),
        (12, '2023-11-29', 2, 3, 5, 9, 'Non-cash', True, 35.00),
        (13, '2023-11-30', 3, 4, 5, 8, 'Non-cash', False, 5.00),
        (14, '2023-12-01', 4, 5, 5, 17, 'Cash', True, 11.00),
        (15, '2023-12-02', 3, 6, 5, 15, 'Non-cash', False, 12.00),
        (16, '2023-12-03', 2, 7, 5, 18, 'Cash', True, 42.00),
        (17, '2023-12-04', 1, 8, 5, 13, 'Non-cash', False, 31.00),
        (18, '2023-12-05', 4, 9, 5, 14, 'Cash', True, 25.00),
        (19, '2023-12-06', 3, 10, 5, 15, 'Non-cash', False, 18.00),
    ]

    insert_query = """
    INSERT INTO Sales (SaleCode, SaleDate, ClientCode, ProductCode, QuantitySold, Discount, PaymentMethod, NeedDelivery, DeliveryCost)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for record in sales_data:
        cursor.execute(insert_query, record)

    connection.commit()

except Exception as e:
    print(f"Помилка при додаванні даних до таблиці Продажі товарів: {e}")

cursor.close()
connection.close()
