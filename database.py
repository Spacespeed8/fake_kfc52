import sqlite3
from datetime import datetime

connection = sqlite3.connect("kfc.db")
sql = connection.cursor()

sql.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER ,"
            "name TEXT, phone_number TEXT, reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS products(pr_id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "pr_name TEXT, pr_price REAL,pr_desc TEXT,pr_quantity INTEGER, pr_photo TEXT, "
            "reg_date DATETIME);")
sql.execute("CREATE TABLE IF NOT EXISTS cart(user_id INTEGER, pr_id INTEGER, pr_count INTEGER,"
            "pr_name TEXT,total_price REAL);")
connection.commit()



def add_users(user_id, name, phone_number):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO users(user_id, name, phone_number, reg_date) VALUES(?,?,?,?);",
                (user_id,name,phone_number,datetime.now()))
    connection.commit()



def check_users(user_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    checker = sql.execute("select * FROM users WHERE user_id=?;",(user_id,)).fetchone()
    if checker:
        return True
    elif not checker:
        return False



def get_all_users():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    all_users= sql.execute("SELECT * FROM users;").fetchall()
    return all_users

def add_product(pr_name, pr_price, pr_desc,pr_quantity,pr_phort):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("INSERT INTO products(pr_name, pr_price,pr_desc,pr_quantity,pr_photo,reg_date"
                "VALUES(?,?,?,?,?,?);",(pr_name,pr_price,pr_desc,pr_quantity,pr_phort,
                                        datetime.now()))


def get_all_product():
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    all_products = sql.execute("SELECT * FROM products;")
def delete_product():
    pass

def get_exact_product():
    pass

def get_pr_id_name():
    pass

def delete_all_products():
    pass

def change_quantity(new_quantity,pr_id):
    connection = sqlite3.connect("kfc.db")
    sql = connection.cursor()
    sql.execute("UPDATE products SET pr_quantity=? WHERE pr_id=?;",(new_quantity,pr_id))
#Корзина

def add_to_cart():
    pass

def delete_exact_pr_from_cart():
    pass

def delete_exact_user_cart():
    pass

def get_cart_id_name():
    pass
