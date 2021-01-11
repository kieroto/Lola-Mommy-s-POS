import sqlite3

# ----------------------------------------------- CREATE ----------------------------------------------------------------------------------------- #

def product():
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS product (
            productID INTEGER PRIMARY KEY,
            productName text,
            category text,
            price integer,
            wholesaleprice integer,
            minWholesale integer,
            stock integer
        ) """)
    con.commit()
    con.close()


def customer():
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS customer (
                customerID INTEGER PRIMARY KEY,
                customerFirst text,
                customerLast text,
                mobile int,
                address text
            ) """)
    con.commit()
    con.close()

def employee():
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS employee (
                userID INTEGER PRIMARY KEY,
                username text,
                password text,
                role text
            ) """)
    con.commit()
    con.close()

def order():
    con = sqlite3.connect('order.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS orderx (
                primaryID INTEGER PRIMARY KEY,
                orderID INTEGER,
                userID INTEGER,
                customerID INTEGER,
                productID INTEGER,
                productName text,
                quantity INTEGER,
                totalAmount INTEGER,
                date text,
                time text
                ) """)
    con.commit()
    con.close()

def history():
    con = sqlite3.connect('history.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS history (
                        historyID INTEGER PRIMARY KEY,
                        userID INTEGER,
                        action text,
                        date text,
                        time text
                    ) """)
    con.commit()
    con.close()

def adjust():
    con = sqlite3.connect('role_priv.db')
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS privileges (
                    role_id INTEGER PRIMARY KEY,
                    role text,
                    privileges_bin text
                ) """)
    con.commit()
    con.close()


# ----------------------------------------------- ADD ----------------------------------------------------------------------------------------- #


def add_product(productID, productName, category, price, wholesaleprice, minWholesale, stock):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("INSERT INTO product VALUES (:productID, :productName, :category, :price, :wholesaleprice, :minWholesale, :stock)",
            {
                'productID': productID,
                'productName': productName,
                'category': category,
                'price': price,
                'wholesaleprice': wholesaleprice,
                'minWholesale': minWholesale,
                'stock': stock
            })

    con.commit()
    con.close()

def add_customer(customerID, customerFirst, customerLast, mobile, address):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("INSERT INTO customer VALUES (:customerID, :customerFirst, :customerLast, :mobile, :address)",
            {
                'customerID': customerID,
                'customerFirst': customerFirst,
                'customerLast': customerLast,
                'mobile': mobile,
                'address': address
            })

    con.commit()
    con.close()

def add_employee(username, password, role):
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    # c.execute("INSERT INTO employee VALUES (:username, :password, :role)",
    c.execute("INSERT INTO employee (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        
            # {
            #     # 'userID': userID,
            #     'username': username,
            #     'password': password,
            #     'role': role,
            # })

    con.commit()
    con.close()

def add_order(primaryID, orderID, userID, customerID, productID, productName, quantity, totalAmount, date, time):
    con = sqlite3.connect('order.db')
    c = con.cursor()
    c.execute("INSERT INTO orderx VALUES (:primaryID, :orderID, :userID, :customerID, :productID, :productName, :quantity, :totalAmount, :date, :time)",
              {
                  'primaryID': primaryID,
                  'orderID': orderID,
                  'userID': userID,
                  'customerID': customerID,
                  'productID': productID,
                  'productName': productName,
                  'quantity': quantity,
                  'totalAmount': totalAmount,
                  'date': date,
                  'time': time,
              })

    con.commit()
    con.close()

def add_history(historyID, userID, action, date, time):
    con = sqlite3.connect('history.db')
    c = con.cursor()
    c.execute("INSERT INTO employee VALUES (:historyID, :userID, :action, :date, :time)",
              {
                  'historyID': historyID,
                  'userID': userID,
                  'action': action,
                  'date': date,
                  'time': time,
              })

    con.commit()
    con.close()


# ----------------------------------------------- RETRIEVE FOR VIEW ---------------------------------------------------------------------------------------- #

def retrieve_product():
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("SELECT * FROM product")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_category(cat):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("SELECT * FROM product WHERE category = " + cat +" AND stock > 0")
    rows = c.fetchall()
    con.close()
    return rows

def retreive_name(pname):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("SELECT * FROM product WHERE productName = " + pname)
    rows = c.fetchall()
    con.close()
    return rows


def retrieve_customer():
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("SELECT * FROM customer")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_customer_search(key):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("SELECT * FROM customer WHERE " + key)
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_employee():
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    c.execute("SELECT * FROM employee")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_order():
    con = sqlite3.connect('order.db')
    c = con.cursor()
    c.execute("SELECT * FROM orderx")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_history():
    con = sqlite3.connect('history.db')
    c = con.cursor()
    c.execute("SELECT * FROM history")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_privileges():
    con = sqlite3.connect('role_priv.db')
    c = con.cursor()
    c.execute("SELECT * FROM privileges")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_lastorder():
    con = sqlite3.connect('order.db')
    c = con.cursor()
    c.execute("SELECT * FROM orderx ORDER BY primaryID DESC LIMIT 1")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_lastcustomer():
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("SELECT * FROM customer ORDER BY customerID DESC LIMIT 1")
    rows = c.fetchall()
    con.close()
    return rows
# ----------------------------------------------- UPDATE ELEMENT ------------------------------------------------------------------------------------------ #

def update_product(productID, productName, category, price, wholesaleprice, minWholesale, stock):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute(
        'UPDATE product SET productName=?, category=?, price=?, wholesaleprice=?, minWholesale=?, stock=? WHERE productID=?', 
        (productName, category, price, 
        wholesaleprice, minWholesale, stock, int(productID))
    )
    con.commit()
    con.close()

def update_stock(productName, stock):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute(
        'UPDATE product SET stock=? WHERE productName=?', 
        (int(stock), str(productName))
    )
    con.commit()
    con.close()

def update_customer(customerID, customerFirst, customerLast, mobile, address):
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("""UPDATE customer SET
           customerFirst = :customerFirst,
           customerLast = :customerLast,
           mobile = :mobile,
           address = :address,

           WHERE customerID = :customerID""",
              {
                  'customerID': customerID,
                  'customerFirst': customerFirst,
                  'customerLast': customerLast,
                  'mobile': mobile,
                  'address': address
              }
    )
    con.commit()
    con.close()

def update_employee(userID, username, password, role):
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    c.execute("""UPDATE employee SET
               username = :username,
               password = :password,
               role = :role,

               WHERE userID = :userID""",
              {
                'userID': userID,
                'username': username,
                'password': password,
                'role': role,
              }
    )
    con.commit()
    con.close()

def update_priv(role, privileges_bin):
    con = sqlite3.connect('role_priv.db')
    c = con.cursor()
    c.execute("""UPDATE privileges SET
                privileges_bin = :privileges_bin

                WHERE role = :role""",
                {
                    'role':role,
                    'privileges_bin':privileges_bin,
                }
    )
    con.commit()
    con.close()

# ----------------------------------------------- SEARCH ELEMENT ------------------------------------------------------------------------------------------ #


# ----------------------------------------------- DELETE ENTRY -------------------------------------------------------------------------------------------- #


#TEMPLATE TO DELETE ENTRY
def delete_database_name(id):
    con = sqlite3.connect('database_name.db')
    c = con.cursor()
    c.execute("DELETE FROM table_name WHERE primary_id = " + id)
    con.commit()
    con.close()

def delete_product(productID):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("DELETE FROM product WHERE productID = " + productID)
    con.commit()
    con.close()

def delete_records():
    con = sqlite3.connect('order.db')
    c = con.cursor()
    c.execute("DELETE FROM orderx ")
    con.commit()
    con.close()

def delete_customer():
    con = sqlite3.connect('customer.db')
    c = con.cursor()
    c.execute("DELETE FROM customer ")
    con.commit()
    con.close()