import Connection
ClientCode = 4
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()


def run_query(sql_query):
    # Підключення до бази даних та виконання запитів
    try:
        cursor.execute(sql_query)

        # Отримання результатів запиту
        records = cursor.fetchall()

        # Вивід результатів
        for record in records:
            print(record)

    except Exception as e:
        print(f"Ошибка: {e}")


# Запит 1
# -------------------------------------------------------------------
print("Відобразити всі продажі, які були оплачені готівкою та відсортувати їх по назві клієнта за алфавітом:")
sql_query = """
   SELECT * FROM Sales
WHERE PaymentMethod = 'Cash'
ORDER BY ClientCode;

"""
run_query(sql_query)

# Запит 2
# ------------------------------------------------------------
print("Відобразити всі продажі, по яких потрібна була доставка:")
sql_query = """
    SELECT * FROM Sales
WHERE NeedDelivery = TRUE;


"""
run_query(sql_query)

# Запит 3
# ------------------------------------------------------------
print("Порахувати суму та суму з урахуванням скидки, яку треба сплатити кожному клієнту (запит з обчислювальним полем)::")
sql_query = """
       SELECT ClientCode,
       SUM(Price * QuantitySold) AS Total,
       SUM((Price * QuantitySold) * (1 - Discount)) AS TotalWithDiscount
FROM Sales,Products
GROUP BY ClientCode;


"""
run_query(sql_query)

# Запит 4
# ------------------------------------------------------------
print("Відобразити всі покупки вказаного клієнта (запит з параметром):")
sql_query = """
SELECT * FROM Sales
WHERE ClientCode = ClientCode;

"""
run_query(sql_query)

# Запит 5
# ------------------------------------------------------------
print("Порахувати кількість покупок, які скоїв кожен клієнт (підсумковий запит):")
sql_query = """
    SELECT ClientCode, COUNT(SaleCode) AS PurchaseCount
FROM Sales
GROUP BY ClientCode;


"""
run_query(sql_query)

# Запит 6
# ------------------------------------------------------------
print("Порахувати суму, яку сплатив кожен клієнт за готівковим та безготівковим розрахунком (перехресний запит):")

sql_query = """
    SELECT ClientCode,
       SUM(CASE WHEN PaymentMethod = 'Cash' THEN (Price * QuantitySold) ELSE 0 END) AS CashTotal,
       SUM(CASE WHEN PaymentMethod = 'Non-cash' THEN (Price * QuantitySold) ELSE 0 END) AS NonCashTotal
FROM Sales,Products
GROUP BY ClientCode;


"""
run_query(sql_query)

# Закриття підключення
cursor.close()
connection.close()