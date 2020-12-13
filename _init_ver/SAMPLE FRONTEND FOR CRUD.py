#THIS IS A SAMPLE CODE FOR IMPORTING CRUD.py AND CALLING ITS CRUD FUNCTIONALITIES

from tkinter import *
import CRUD         #IMPORT CRUD.py TO FRONTEND

root = Tk()
root.geometry("500x300")
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
def add_data():
    if (len(productName.get()) != 0):
        CRUD.add_product(productID.get(), productName.get(), category.get(), price.get(), stock.get())


#PRINT TABLE ELEMENTS IN CONSOLE
def view_table():
    rows = CRUD.retrieve_product()
    print(rows)


label1 = Label(root, text="Add Product", relief="solid", width=20, font=("arial", 16, "bold"))
label1.place(x=90,y=23)

label2 = Label(root, text="Product: ", font=("arial", 12, "bold"))
label2.place(x=90,y=60)

entry1 = Entry(textvar=productName)
entry1.place(x=200,y=60)

label3 = Label(root, text="Category: ", font=("arial", 12, "bold"))
label3.place(x=90,y=83)

entry2 = Entry(textvar=category)
entry2.place(x=200,y=83)

label4 = Label(root, text="Price: ", font=("arial", 12, "bold"))
label4.place(x=90,y=106)

entry3 = Entry(textvar=price)
entry3.place(x=200,y=106)

label5 = Label(root, text="Stock: ", font=("arial", 12, "bold"))
label5.place(x=90,y=129)

entry4 = Entry(textvar=stock)
entry4.place(x=200,y=129)

label6 = Label(root, text="ID: ", font=("arial", 12, "bold"))
label6.place(x=90,y=152)

entry5 = Entry(textvar=productID)
entry5.place(x=200,y=152)

button1 = Button(root, text="Add Product", width=12,bg="red", command=add_data, font=("arial", 12, "bold"))
button1.place(x=160,y=200)

button2 = Button(text="View in console", width=12, bg="red", command=view_table, font=("arial", 12, "bold"))
button2.place(x=160,y=250)

root.mainloop()