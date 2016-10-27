#David Justice
#10-26-16
#Inserting Data

import sqlite3

def insert_data(values):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name, Price) values (?,?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    product = ("Espresso",1.50)
    insert_data(product)
    product = ("Latte",1.35)
    insert_data(product)
    product = ("Mocha",2.40)
    insert_data(product)
    product = ("Green Tea",1.20)
    insert_data(product)
    product = ("Black Tea",1.00)
    insert_data(product)
    product = ("Americano",1.50)
    insert_data(product)
