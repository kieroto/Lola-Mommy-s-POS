#THIS IS A SAMPLE CODE FOR IMPORTING CRUD.py AND CALLING ITS CRUD FUNCTIONALITIES

from tkinter import *
import CRUD         #IMPORT CRUD.py TO FRONTEND
import util

root = Tk()
root.title("Sample Frontend")

CRUD.product() #CREATE OR CONNECT DATABASE
CRUD.employee()
CRUD.customer()
CRUD.adjust()
CRUD.history()
#ADD ENTRY TO DATABASE
def view_cs():
    rows = CRUD.retrieve_customer()
    for item in rows:
        print(item)
#PRINT TABLE ELEMENTS IN CONSOLE
def view_o():
    rows = CRUD.retrieve_order()
    for item in rows:
        print(item)
def view_r():
    rows = CRUD.retrieve_privileges()
    for item in rows:
        print(item)
def view_u():
    rows = CRUD.retrieve_employee()
    for item in rows:
        print(item)

def del_cs():
    CRUD.delete_customer()

def del_o():
    CRUD.delete_orders()

def dummy():
    CRUD.add_customer(0, '-', '-', 0, '-')

def dummy2():
    CRUD.sqlitequery()
    CRUD.adjust()

    CRUD.add_role('Admin', '111111111')
    CRUD.add_role('Cashier', '111111111')
    CRUD.add_role('Inventory Staff', '111111111')

def del_u():
    CRUD.delete_user()
    CRUD.add_employee(1,1,'Admin')

def wipeh():
    CRUD.delete_history()
    CRUD.history()

def viewh():
    row=CRUD.retrieve_history()
    for item in row:
        print(item)
    
CRUD.product()
CRUD.customer()
CRUD.employee()
CRUD.order()
CRUD.history()
CRUD.adjust()


button1 = Button(root, text="View customers", width=12,bg="red", command=view_cs, font=("arial", 12, "bold"))
button1.grid(column=0, row=0)
button2 = Button(text="View in orders", width=12, bg="red", command=view_o, font=("arial", 12, "bold"))
button2.grid(column=2, row=0)
button2 = Button(text="Delete Customers", width=12, bg="red", command=del_cs, font=("arial", 12, "bold"))
button2.grid(column=0, row=1)
button2 = Button(text="Delete Orders", width=12, bg="red", command=del_o, font=("arial", 12, "bold"))
button2.grid(column=2, row=1)
button1 = Button(root, text="View users", width=12,bg="red", command=view_u, font=("arial", 12, "bold"))
button1.grid(column=0, row=2)
button2 = Button(text="View in roles", width=12, bg="red", command=view_r, font=("arial", 12, "bold"))
button2.grid(column=2, row=2)
button2 = Button(text="dummy", width=12, bg="red", command=dummy, font=("arial", 12, "bold"))
button2.grid(column=2, row=3)
button2 = Button(text="wipe roles", width=12, bg="red", command=dummy2, font=("arial", 12, "bold"))
button2.grid(column=0, row=3)
button2 = Button(text="wipe users", width=12, bg="red", command=del_u, font=("arial", 12, "bold"))
button2.grid(column=0, row=4)
button2 = Button(text="WIPE history", width=12, bg="red", command=wipeh, font=("arial", 12, "bold"))
button2.grid(column=2, row=4)
button2 = Button(text="see history", width=12, bg="red", command=viewh, font=("arial", 12, "bold"))
button2.grid(column=2, row=5)




root.mainloop()