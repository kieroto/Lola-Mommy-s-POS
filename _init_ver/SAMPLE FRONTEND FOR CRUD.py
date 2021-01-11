#THIS IS A SAMPLE CODE FOR IMPORTING CRUD.py AND CALLING ITS CRUD FUNCTIONALITIES

from tkinter import *
import CRUD         #IMPORT CRUD.py TO FRONTEND
import util

root = Tk()
root.title("Sample Frontend")

CRUD.product() #CREATE OR CONNECT DATABASE
CRUD.employee()
CRUD.customer()

productID = StringVar()
productName = StringVar()
category = StringVar()
price = StringVar()
stock = StringVar()


#ADD ENTRY TO DATABASE
def view_cs():
    #a
    rows = CRUD.retrieve_customer()
    for item in rows:
        print(item)
#PRINT TABLE ELEMENTS IN CONSOLE
def view_o():
    rows = CRUD.retrieve_order()
    for item in rows:
        print(item)

def del_cs():
    CRUD.delete_customer()

def del_o():
    CRUD.delete_records()

def dummy():
    CRUD.add_customer(0, '-', '-', 0, '-')
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
button2 = Button(text="dummy", width=12, bg="red", command=dummy, font=("arial", 12, "bold"))
button2.grid(column=2, row=3)

root.mainloop()