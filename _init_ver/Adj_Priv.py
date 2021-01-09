from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *
from table import table

# All options for roles 
ROLEOPTIONS=["Admin", "Cashier", "Inventory Staff"]

class adj_priv(ttk.Frame, Tk):

    def __init__(self, root, body, pages, title):

        self.root = root
        self.body = body

        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        lbl = Label(self.body, text=title, font=('Helvetica', 20, 'bold'))
        lbl.grid(column=3, row=0 , columnspan=6, rowspan=1, sticky=(N+S+E+W))

        #Dropdown menu for roles
        self.lb = Label(self.body, text="Role:", font=('Helvetica', 16))
        self.lb.grid(column=1, row=3)
        self.role = ttk.Combobox(self.body, width=15,font=("Helvetica, 16"), values=ROLEOPTIONS)
        self.role.grid(column=2, row=3)

        Checkbutton1 = IntVar()
        Checkbutton2 = IntVar()
        Checkbutton3 = IntVar()
        Checkbutton4 = IntVar()
        Checkbutton5 = IntVar()
        Checkbutton6 = IntVar()
        Checkbutton7 = IntVar()
        Checkbutton8 = IntVar()
        Checkbutton9 = IntVar()

        #Checkbuttons for privileges
        self.btn1 = Checkbutton(self.body, text="View inventory", variable=Checkbutton1, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn2 = Checkbutton(self.body, text="Edit inventory", variable=Checkbutton2, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn3 = Checkbutton(self.body, text="View history", variable=Checkbutton3, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn4 = Checkbutton(self.body, text="View sales", variable=Checkbutton4, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn5 = Checkbutton(self.body, text="Process orders", variable=Checkbutton5, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn6 = Checkbutton(self.body, text="View customer database", variable=Checkbutton6, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=20)
        self.btn7 = Checkbutton(self.body, text="Edit customer", variable=Checkbutton7, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn8 = Checkbutton(self.body, text="View orders", variable=Checkbutton8, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn9 = Checkbutton(self.body, text="Void/Edit orders", variable=Checkbutton9, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=20)

        self.btn1.grid(column=4, row=2)
        self.btn2.grid(column=4, row=3)
        self.btn3.grid(column=4, row=4)
        self.btn4.grid(column=4, row=5)
        self.btn5.grid(column=4, row=6)
        self.btn6.grid(column=5, row=2)
        self.btn7.grid(column=5, row=3)
        self.btn8.grid(column=5, row=4)
        self.btn9.grid(column=5, row=5)

        #Save button
        self.savebtn = Button(self.body, text="Save Changes", font = ("Helvetica", 16), command=lambda:self.test) 
        self.savebtn.config(height=1, width=15, background='#93c47d')
        self.savebtn.grid(column=5, row=7)