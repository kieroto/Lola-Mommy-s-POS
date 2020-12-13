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
    pass

def history():
    pass

# ----------------------------------------------- ADD ----------------------------------------------------------------------------------------- #


def add_product(productID, productName, category, price, stock):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("INSERT INTO product VALUES (:productID, :productName, :category, :price, :stock)",
            {
                'productID': productID,
                'productName': productName,
                'category': category,
                'price': price,
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

def add_employee(userID, username, password, role):
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    c.execute("INSERT INTO employee VALUES (:userID, :username, :password, :role)",
            {
                'userID': userID,
                'username': username,
                'password': password,
                'role': role,
            })

    con.commit()
    con.close()

def add_order():
    pass

def add_history():
    pass


# ----------------------------------------------- RETRIEVE FOR VIEW ---------------------------------------------------------------------------------------- #

def retrieve_product():
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("SELECT * FROM product")
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

def retrieve_employee():
    con = sqlite3.connect('employee.db')
    c = con.cursor()
    c.execute("SELECT * FROM employee")
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_order():
    pass

def retrieve_customer():
    pass

# ----------------------------------------------- UPDATE ELEMENT ------------------------------------------------------------------------------------------ #
# ----------------------------------------------- SEARCH ELEMENT ------------------------------------------------------------------------------------------ #
# ----------------------------------------------- DELETE ENTRY -------------------------------------------------------------------------------------------- #


#TEMPLATE TO DELETE ENTRY
def delete_database_name(id):
    con = sqlite3.connect('database_name.db')
    c = con.cursor()
    c.execute("DELETE FROM database_name WHERE id=?",id)
    con.commit()
    con.close()

