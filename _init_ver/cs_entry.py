from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *

class cs_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title):

        self.root = root
        self.body = body
       
        # Create Label Objects
        self.Userlbl = Label(self.body, text="Customer Details", font=('Helvetica', 30, 'bold'))
        self.Userlbl.grid(column=4, row=2 , columnspan=6, rowspan=2, sticky=(N))
    
        #Label and entry for first and last name
        self.fname = Label(self.body, text = "First Name: ", font = ("Helvetica", 16))
        self.fname.grid(column=4, row=4)
        self.cfirst = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.cfirst.grid(column=5, row=4)
        self.cfirst.insert(0, "Cole")

        self.lname = Label(self.body, text = "Last Name: ", font = ("Helvetica", 16))
        self.lname.grid(column=4, row=5)
        self.clast = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.clast.grid(column=5, row=5)
        self.clast.insert(0, "Ang")

        #Label and entry for address name
        self.addr = Label(self.body, text = "Address: ", font = ("Helvetica", 16))
        self.addr.grid(column=4, row=6)
        self.caddr = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.caddr.grid(column=5, row=6)
        self.caddr.insert(0, "Davao City")

        #Label and entry for mobile
        self.mobile = Label(self.body, text = "Mobile number: ", font = ("Helvetica", 16))
        self.mobile.grid(column=4, row=7)
        self.cmobile = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.cmobile.grid(column=5, row=7)
        self.cmobile.insert(0, "09123456789")

        customerDetails={"customerFirst": self.cfirst.get(), "customerLast": self.clast.get(), "mobile": self.cmobile.get(), "address": self.caddr.get()}

        customerConfirmBtn = Button(self.body, text="Confirm", font = ("Helvetica", 16), command=lambda:confirm_customer(1, customerConfirmBtn, customerDetails, body))
        customerConfirmBtn.grid(column=4, row=8 , columnspan=6, rowspan=2, sticky=(N))
       
    def page_id(self):
        return 1

    def click(self, i):
        pass
