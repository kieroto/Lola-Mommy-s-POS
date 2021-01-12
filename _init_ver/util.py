import CRUD
import sqlite3

def delete_history_entry(pid):
    con = sqlite3.connect('history.db')
    c = con.cursor()
    c.execute("DELETE FROM history WHERE historyID = " + '"'+ str(pid) +'"')
    con.commit()
    con.close()


def add_stock(pid, n):
    con = sqlite3.connect('product.db')
    c = con.cursor()
    c.execute("SELECT stock FROM product WHERE productName = " + '"'+ str(pid) +'"')
    stock = c.fetchall()
    stock_ = int(stock[0][0]) + n
    CRUD.update_stock(pid, int(stock_))
    con.close()

def void_order(pid):
    con = sqlite3.connect('order.db')
    c = con.cursor()
    c.execute("SELECT productName, quantity FROM orderx WHERE orderID = " + '"'+ pid +'"')
    s = c.fetchall()
    #rint(order[0])
    for order in s:
        add_stock(str(order[0]), int(order[1]))
    CRUD.delete_records('"'+ str(pid) +'"')
    con.close()

def retrieve_orderids():
    con = sqlite3.connect('order.db')
    c = con.cursor()
    rows = [row[0] for row in c.execute("SELECT orderID FROM orderx")]
    con.close()
    return rows

def retrieve_order_single(oid):
    con = sqlite3.connect('order.db')
    c = con.cursor()
    c.execute("SELECT * FROM orderx WHERE orderID = " + str(oid))
    rows = c.fetchall()
    con.close()
    return rows

def retrieve_order_from_history():
    con = sqlite3.connect('history.db')
    c = con.cursor()
    c.execute("SELECT * FROM history WHERE action_type = 'order'" )
    rows = c.fetchall()
    con.close()
    return rows

#------------------------
def date_split(date):
    temp = (date.split('/'))
    count = 0
    for x in temp:
        if count < len(temp):
            temp[count] = x.lstrip('0')
            count += 1

    date = temp[0] + '/' + temp[1] + '/' + temp[2]
    return date

def priv_bin(role):
    s = CRUD.retrieve_privilege_bin('"' + role + '"')
    return s[0][1]

def replace(index, Table_):
    focus_item(index, Table_)
    Table_.tree.delete(Table_.tree.selection())

def focus_item(index, Table_):
    child_id = Table_.tree.get_children()[int(index)]
    Table_.tree.focus(child_id)
    Table_.tree.selection_set(child_id)

def wholesale_check(qty, product_):
    if ( qty >= product_[0][5]):
        price = int(product_[0][4])
    else:
        price = int(product_[0][3])
    return price

def check_if_exists(search, list):
    for i in range(0, len(list)):
        if( list[i] == search):
            return 1
    return 0

def get_index(search, list):
    for i in range(0, len(list)):
        if( list[i] == search):
            return i

def extract_orderprev():
    row=CRUD.retrieve_lastorder()
    if not row:
        order = [0,0]
    else:
        order = [row[0][0], row[0][1]]
    return order

def update_order(OC):
    # (primaryID, orderID, userID, customerID, 
    # productID, productName, quantity, totalAmount, date, time):
    CRUD.add_order(OC.pid, OC.oid, OC.userID, OC.customerID, OC.productid, OC.pn, OC.qty, OC.ttl, OC.date, OC.time)
    

def search_cs(key):
    fname = ' customerFirst = "' + key['customerFirst']+'" '
    lname = ' customerLast = "' + key['customerLast']+'" '
    mob = ' mobile = ' + str(key['mobile'])+ ' '
    add = ' address = "' + key['address']+'" '
    key_line = fname + ' AND ' + lname + ' AND ' + mob + ' AND ' + add
    print(key_line)
    row = CRUD.retrieve_customer_search_whole(key_line)
    print(row)
    if row:
        print("match")
        return row[0][0]
    else:
        return -1

def customer_check(cs_details):
    if(cs_details['type']=='short'):
        return -1
    else:
        key = search_cs(cs_details)
    
    if (key!=-1):
        return key
    else:
        try:
            s = CRUD.retrieve_lastcustomer()
            last_id = s[0][0]
            new_id = int(last_id) + 1
        except IndexError:
            new_id = 0
        CRUD.add_customer(new_id, cs_details['customerFirst'], cs_details['customerLast'], 
                        cs_details['mobile'], cs_details['address'])
        return new_id

def undo_order(pd, qty):
    for i in range(0, len(pd)):
        CRUD.update_stock(pd[i], int(CRUD.retreive_name('"'+pd[i]+'"')[0][6] + int(qty[i])))

        