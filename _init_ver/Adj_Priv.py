from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *
from table import table
import sqlite3
from tkinter import messagebox 
import CRUD

# All options for roles 
ROLEOPTIONS=["Admin", "Cashier", "Inventory Staff"]

class adj_priv(ttk.Frame, Tk):

    def __init__(self, root, body, Page_tracker, title):

        self.root = root
        self.body = body

        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        self.records = CRUD.retrieve_privileges()

        # Assign roles and privileges to lists
        self.roleList=[]
        self.privList=[]
        for row in self.records:
            self.roleList.append(row[0])
            self.privList.append(row[1])

        lbl = Label(self.body, text=title, font=('Helvetica', 20, 'bold'))
        lbl.grid(column=3, row=0 , columnspan=6, rowspan=1, sticky=(N+S+E+W))

        #Dropdown menu for roles
        self.lb = Label(self.body, text="Role:", font=('Helvetica', 16))
        self.lb.grid(column=1, row=3)
        self.role = ttk.Combobox(self.body, width=15,font=("Helvetica, 16"), values=self.roleList)
        self.role.bind("<<ComboboxSelected>>", self.selection)
        self.role.grid(column=2, row=3)

        self.Checkbutton1 = IntVar()
        self.Checkbutton2 = IntVar()
        self.Checkbutton3 = IntVar()
        self.Checkbutton4 = IntVar()
        self.Checkbutton5 = IntVar()
        self.Checkbutton6 = IntVar()
        self.Checkbutton7 = IntVar()
        self.Checkbutton8 = IntVar()
        self.Checkbutton9 = IntVar()

        #Checkbuttons for privileges
        self.btn1 = Checkbutton(self.body, text="View inventory", variable=self.Checkbutton1, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn2 = Checkbutton(self.body, text="Edit inventory", variable=self.Checkbutton2, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn3 = Checkbutton(self.body, text="View history", variable=self.Checkbutton3, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn4 = Checkbutton(self.body, text="View sales", variable=self.Checkbutton4, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn5 = Checkbutton(self.body, text="Process orders", variable=self.Checkbutton5, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn6 = Checkbutton(self.body, text="View customer database", variable=self.Checkbutton6, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=20)
        self.btn7 = Checkbutton(self.body, text="Edit customer", variable=self.Checkbutton7, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn8 = Checkbutton(self.body, text="View orders", variable=self.Checkbutton8, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=15)
        self.btn9 = Checkbutton(self.body, text="Void/Edit orders", variable=self.Checkbutton9, onvalue=1, offvalue=0, font=("Helvetica", 16), height=2, width=20)
        self.buttons=[self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, 
                    self.btn6, self.btn7, self.btn8, self.btn9 ]

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
        self.savebtn = Button(self.body, text="Save Changes", font = ("Helvetica", 16), command=self.save_changes) 
        self.savebtn.config(height=1, width=15, background='#93c47d')
        self.savebtn.grid(column=5, row=7)

    # function for when a role is selected
    def selection(self, event):
        self.roleActive = self.role.get()
        if(self.roleActive == 'Admin'):
            for button in self.buttons:
                button.config(state=DISABLED)
        else:
            for button in self.buttons:
                button.config(state=ACTIVE)

            pass
        # take id of selected role
        i = 0
        for row in self.records:
            if row[0] == self.roleActive:
                break
            i = i + 1

        # take privilege binary and split it into nine character. Assign them to toggle list
        self.toggleList=[char for char in self.privList[i]]
        print(self.toggleList)
        # Change toggle of each checkbutton
        self.Checkbutton1.set(self.toggleList[0])
        self.Checkbutton2.set(self.toggleList[1])
        self.Checkbutton3.set(self.toggleList[2])
        self.Checkbutton4.set(self.toggleList[3])
        self.Checkbutton5.set(self.toggleList[4])
        self.Checkbutton6.set(self.toggleList[5])
        self.Checkbutton7.set(self.toggleList[6])
        self.Checkbutton8.set(self.toggleList[7])
        self.Checkbutton9.set(self.toggleList[8])

    def save_changes(self):
        if messagebox.askyesno("message", "Confirm changes?"):
            pass
        else:
            return
        role = self.role.get()
        result = [] #array of privileges
        c1=self.Checkbutton1.get()
        c2=self.Checkbutton2.get()
        c3=self.Checkbutton3.get()
        c4=self.Checkbutton4.get()
        c5=self.Checkbutton5.get()
        c6=self.Checkbutton6.get()
        c7=self.Checkbutton7.get()
        c8=self.Checkbutton8.get()
        c9=self.Checkbutton9.get()
        result.append(c1)
        result.append(c2)
        result.append(c3)
        result.append(c4)
        result.append(c5)
        result.append(c6)
        result.append(c7)
        result.append(c8)
        result.append(c9)

        #convert array to string
        listToStr = ' '.join([str(elem) for elem in result])
        role_priv = ''.join(listToStr.split())

        #updates database
        CRUD.update_priv(role, role_priv)

        self.records = CRUD.retrieve_privileges()
        # Assign roles and privileges to lists
        self.roleList = []
        self.privList = []
        for row in self.records:
            self.roleList.append(row[0])
            self.privList.append(row[1])