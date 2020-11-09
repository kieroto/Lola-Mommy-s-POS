from tkinter import *
from tkinter import ttk
import tkinter.font as font
from Sales import s_page
from History import h_page
from Inventory import i_page
from Customers import cs_page
from Home import home_page
from order import orderselect

class main_(ttk.Frame, Tk):
    
    def __init__(self, root, menu, body, admin, menuFont):
       
        self.root = root
        self.menu = menu
        self.body = body
        self.body_ = body
        self.page_toggle = 0
        self.pages = [] 

        # Virtual pixels to help resize button in pixels
        # pixelVirtual = PhotoImage(width=1, height=1)
        # Font styles
 
        # Create button objects for top bar
        Sales = Button(self.menu, text='  Sales  ', command= lambda: self.click(0))
        Customer = Button(self.menu, text='Customer ', command= lambda: self.click(1))
        Inventory = Button(self.menu, text='Inventory', command= lambda: self.click(2))
        History = Button(self.menu, text=' History ', command= lambda: self.click(3))
        Order = Button(self.menu, text=' Orders ', command= lambda: self.click(4))
        
        Add_user = Button(self.menu, text='Add User', command= lambda: self.test)
        Adj_priv = Button(self.menu, text='Adjust Privileges', command= lambda: self.test)
        Log_out = Button(self.menu, text='Logout', command= self.test)
        Back = Button(self.menu, text='Back', command= lambda: self.click(7))

        # List buttons
        self.buttons = [Sales, Customer, Inventory, History, Order, Add_user, Adj_priv, Log_out, Back]

        # Assign button properties
        for bttn in self.buttons:
            #bttn.configure(background='#93c47d', image=pixelVirtual, width=190, height=65, compound="c")
            if (bttn == Add_user or bttn == Adj_priv):
                bttn.configure(background='#89aae0')
            else :
                bttn.configure(background='#93c47d')
            bttn['font']=menuFont


        # Assign buttons in grid system
        Sales.grid(column=0, row=0, columnspan=2, rowspan=2, sticky=(N, S, E, W))
        Customer.grid(column=2, row=0, columnspan=2, rowspan=2,  sticky=(N, S, E, W))
        Inventory.grid(column=4, row=0, columnspan=2, rowspan=2,  sticky=(N, S, E, W))
        History.grid(column=6, row=0, columnspan=2, rowspan=2,  sticky=(N, S, E, W))
        Order.grid(column=8, row=0, columnspan=2, rowspan=2,  sticky=(N, S, E, W))

        # Admin privileges
        if (admin== TRUE):
            Add_user.grid(column=10, row=0, columnspan=2, rowspan=1, sticky=(N, S, E, W))
            Adj_priv.grid(column=10, row=1, columnspan=2, rowspan=1, sticky=(N, S, E, W))
            Log_out.grid(column=13, row=1, columnspan=2, rowspan=1, sticky=(N, S, E, W))
            Back.grid(column=13, row=2, columnspan=2, rowspan=1, sticky=(N, S, E, W))

        # Create Label Objects
        self.Userlbl = Label(self.menu, text='User : <name>', font=('Helvetica', 25, 'bold'))
        self.Userlbl.grid(column=13, row=0, sticky=(N, E))
        
        # Create Home
        # Create pages list stack for tracking pages
        self.pages.append(-1)
        self.home_ = home_page(self.root, self.body, 'Home', self.pages)
        
   
    def click(self, i_):
        # Button color change
        for n in range(9):   
            if (n == i_):
                self.buttons[n].configure(background='#eeeeee')
                continue
            self.buttons[n].configure(background='#93c47d')

        # Short hand IF
        self.shift_(self.pages[-1], i_) if i_ < 8 else self.test

    # Method for resetting widgets inside body frame
    def reset_body(self):
        for widget in self.body.winfo_children():
            widget.destroy()
    
    # Method for navigating through pages 
    def shift_(self, current, i):
        if (current == i):
            pass
        else: 
            self.reset_body()
            self.pages.append(i)
            if (i == 0):
                self.sales = s_page(self.root, self.body, 'Sales')
            elif (i == 1):
                self.customer = cs_page(self.root, self.body, 'Customer')
            elif (i == 2):
                self.inventory = i_page(self.root, self.body, 'Inventory')
            elif (i == 3):
                self.history = h_page(self.root, self.body, 'History')
            elif (i == 4):
                self.order_ = orderselect(self.root, self.body, self.pages)
                pass
                #self.sales = s_page(self.root, self.body, 'Sales')
            elif (i == 5):
                pass
                #self.sales = s_page(self.root, self.body, 'Sales')
            elif (i == 6):
                pass
            elif (i == 7):
                self.page_back()
                #self.sales = s_page(self.root, self.body, 'Sales')
            elif (i == 8):
                self.order_.click(0, self.pages)
                pass
                #self.sales = s_page(self.root, self.body, 'Sales')
    
    # Method for pressing back
    def page_back(self):
        for i in range(2):
            try:
                self.pages.pop()
                e = self.pages[1]
            except IndexError:
                self.home_ = home_page(self.root, self.body, 'Home', self.pages)
                return
        
        self.shift_(-2, self.pages.pop())
             
        
    def create_body(self):
        pass

    def test(self):
        pass
