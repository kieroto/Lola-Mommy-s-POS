from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *
from table import table
import sqlite3
import CRUD

# All options for roles 
ROLEOPTIONS=["Admin", "Cashier", "Inventory Staff"]

class u_page(ttk.Frame, Tk):

    
    

    def __init__(self, root, body, pages, title):

        self.root = root
        self.body = body

        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        self._list_employees = CRUD.retrieve_employee()
        self._list_roles = CRUD.retrieve_privileges()

        # Assign roles and privileges to lists
        self.roleList=[]
        for row in self._list_roles:
            self.roleList.append(row[1])    

        #Setting up title Frame
        self.title = ttk.Frame(body)
        self.title.grid(row=0, column=0, columnspan=14, rowspan=1, sticky=N+S+E+W)

        self.title.rowconfigure(0, weight=1)
        for i in range(0, 14):
            self.title.columnconfigure(i, weight=1)

        #Setting up table Frame
        self.table_frame = ttk.Frame(body)
        self.table_frame.grid(row=1, column=0, columnspan=6, rowspan=19, sticky=N+S+E+W)

        for i in range(0, 6):
            self.table_frame.columnconfigure(i, weight=1)
        
        for i in range(0, 19):
            self.table_frame.rowconfigure(i, weight=1)

        #Setting up add_user Frame
        self.add_user_frame = ttk.Frame(body)
        self.add_user_frame.grid(row=1, column=8, columnspan=6, rowspan=19, sticky=N+S+E+W)

        for i in range(8, 14):
            self.table_frame.columnconfigure(i, weight=1)
        
        for i in range(0, 19):
            self.table_frame.rowconfigure(i, weight=1)

        # Title Label
        title_lb = Label(self.title, text=title, font=('Helvetica', 30, 'bold'))
        title_lb.grid(column=4, row=0 , columnspan=6, rowspan=1, sticky=(N+S+E+W))

        # Create User Table
        row_place = 1
        col_place = 1
        self.UserTable_ = table(frame= self.table_frame, tree_row=row_place, tree_col=col_place, 
                        column_id=("Username", "Role", "Remove"), 
                        rowheight = 40 ,height = 10, font_size = 12, font = 'Helvetica',
                        tablecol_width = 100, headingfont= 30) 

        for row in self._list_employees:
            self.UserTable_.tree.insert('', '0', values=(row[1], row[3]))

        # Add User Label
        self.add_user_lb = Label(self.add_user_frame, text="Add User", font=('Helvetica', 15, 'bold'))
        self.add_user_lb.grid(column=11, row=4 , columnspan=2, rowspan=2, pady=15, sticky=(N+S+E+W))

        # Label and entry for username
        self.username_lb = Label(self.add_user_frame, text = "Username: ", font = ("Helvetica", 16))
        self.username_lb.grid(column=10, row=6, columnspan=1, rowspan=2, pady=5)

        self.username_en = Entry(self.add_user_frame, width = 20, font = ("Helvetica", 16))
        self.username_en.grid(column=12, row=6, columnspan=1, rowspan=2, pady=5)

        self.pass_lb = Label(self.add_user_frame, text = "Password: ", font = ("Helvetica", 16))
        self.pass_lb.grid(column=10, row=8, pady=5)
        self.pass_en = Entry(self.add_user_frame, show="*", width = 20, font = ("Helvetica", 16))
        self.pass_en.grid(column=12, row=8, pady=5)

        self.cpass_lb = Label(self.add_user_frame, text = "Confirm Password: ", font = ("Helvetica", 16))
        self.cpass_lb.grid(column=10, row=10, pady=5)
        self.cpass_en = Entry(self.add_user_frame, show="*", width = 20, font = ("Helvetica", 16))
        self.cpass_en.grid(column=12, row=10, pady=5)

        self.role_lb = Label(self.add_user_frame, text = "Role: ", font = ("Helvetica", 16))
        self.role_lb.grid(column=10, row=12, pady=20)
        self.role_cb = ttk.Combobox(self.add_user_frame, width=20, font=("Helvetica, 16"), values=self.roleList)
        self.role_cb.grid(column=12, row=12, pady=20)

        self.userAddBtn = Button(self.add_user_frame, text="Add", font = ("Helvetica", 16), command=lambda:self.validate(pages))
        self.userAddBtn.config(height=1, width=8, background='#93c47d')
        self.userAddBtn.grid(column=11, row=13 , columnspan=6, rowspan=2, sticky=(N))

       	# Label for Error Message
        self.error_lb = Label(self.add_user_frame, fg = "red", font = ("Helvetica", 14))

    def validate(self, pages):
        us = self.username_en.get()
        pw1 = self.pass_en.get()
        pw2 = self.cpass_en.get()
        role = self.role_cb.get()

        password_confirm=self.cpass_en.get()

        self.userDetails={"username":us, "password": pw1, "role": role}

        if(us == '' or pw1 == '' or pw2 == '' or role == ''):
            self.error_lb.configure(text="Please fill up all fields")		# Displays error if incomplete
            self.error_lb.grid(column=12, row=20)

        else:
            if (pw1 == pw2):
                update_employee = CRUD.add_employee(us, pw1, role)
                add_user_prompt = add_user(1, self.userAddBtn, self.userDetails, self.root, self.body, pages)
                # update_employee = CRUD.add_employee(us, pw1, role)

            else:
                self.error_lb.configure(text="Password mismatch")		# Displays error if incomplete
                self.error_lb.grid(column=12, row=20)