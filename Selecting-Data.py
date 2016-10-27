#David Justice
#10-26-16
#Searching Data

import sqlite3

def select_product(id):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select Name,Price from Product where ProductID=?",(id,))
        product = cursor.fetchone()
        return product
                       
if __name__ == "__main__":
    product = select_product(3)
    print(product)
