from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *
from table import table

# All options for roles 
ROLEOPTIONS=["Admin", "Cashier", "Inventory Staff"]

class au_page(ttk.Frame, Tk):

    def __init__(self, root, body, pages, title):

        self.root = root
        self.body = body

        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        lbl = Label(self.body, text=title, font=('Helvetica', 30, 'bold'))
        lbl.grid(column=2, row=0 , columnspan=6, rowspan=2, sticky=(N+S+E+W))

        #Label and entry for first and last name
        self.username_lb = Label(self.body, text = "Username: ", font = ("Helvetica", 16))
        self.username_lb.grid(column=1, row=6)

        self.username_en = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.username_en.grid(column=2, row=6)

        self.pass_lb = Label(self.body, text = "Password: ", font = ("Helvetica", 16))
        self.pass_lb.grid(column=1, row=7)
        self.pass_en = Entry(self.body, show="*", width = 20, font = ("Helvetica", 16))
        self.pass_en.grid(column=2, row=7)

        self.cpass_lb = Label(self.body, text = "Confirm Password: ", font = ("Helvetica", 16))
        self.cpass_lb.grid(column=1, row=8)
        self.cpass_en = Entry(self.body, show="*", width = 20, font = ("Helvetica", 16))
        self.cpass_en.grid(column=2, row=8)

        self.role_lb = Label(self.body, text = "Role: ", font = ("Helvetica", 16))
        self.role_lb.grid(column=4, row=6)
        self.role_cb = ttk.Combobox(self.body, width=20, font=("Helvetica, 16"), values=ROLEOPTIONS)
        self.role_cb.grid(column=5, row=6)

        self.userAddBtn = Button(self.body, text="Add", font = ("Helvetica", 16), command=lambda:self.validate(pages))
        self.userAddBtn.config(height=1, width=8)
        self.userAddBtn.grid(column=2, row=9 , columnspan=6, rowspan=2, sticky=(N))

       	# Label for Error Message
        self.error_lb = Label(self.body, fg = "red", font = ("Helvetica", 14))

    def validate(self, pages):
        us = self.username_en.get()
        pw1 = self.pass_en.get()
        pw2 = self.cpass_en.get()
        role = self.role_cb.get()

        password_confirm=self.cpass_en.get()

        self.userDetails={"username":us, "password": pw1, "role": role}

        if(us == '' or pw1 == '' or pw2 == '' or role == ''):
            self.error_lb.configure(text="Please fill up all fields")		# Displays error if incomplete
            self.error_lb.grid(column=2, row=10)

        else:
            if (pw1 == pw2):
                add_user_prompt = add_user(1, self.userAddBtn, self.userDetails, self.root, self.body, pages)

            else:
                self.error_lb.configure(text="Password mismatch")		# Displays error if incomplete
                self.error_lb.grid(column=2, row=10)