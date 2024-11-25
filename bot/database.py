import sqlite3

def initiate_db():
    connection = sqlite3.connect("files/telegram.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )''')

    # for i in range(1,5):
    #    cursor.execute('INSERT INTO Products(title, description, price) VALUES(?,?,?)', (f"Продукт{i}", f"Описание{i}", f"{i*100}"))
    connection.commit()
    connection.close()

def get_all_products(id1):
    connection = sqlite3.connect("files/telegram.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products WHERE id = ?", (id1,))
    connection.commit()
    prod = cursor.fetchall()
    connection.close()
    id, title, description, price = prod[0]
    return f"Название: {title} | Описание: {description} | Цена: {price}"

def add_user(username, email, age):
    connection = sqlite3.connect("files/telegram.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)',(f"{username}", f"{email}", f"{age}", "1000"))
    connection.commit()
    connection.close()

def is_included(username):
    connection = sqlite3.connect("files/telegram.db")
    cursor = connection.cursor()
    if cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchall():
        return True
    return False

