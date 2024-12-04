import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )''')


initiate_db()


def get_all_products():
    cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
    connection.commit()
    prod = cursor.fetchall()
    title, description, price = prod[0]
    return f"Название: {title} | Описание: {description} | Цена: {price}"


connection.commit()
connection.close()
