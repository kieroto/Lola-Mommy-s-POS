from tkinter import *
from tkinter import ttk
import tkinter.font as font
from Order_process import order_process
from cs_entry import cs_page

class orderselect(ttk.Frame, Tk):
    
    def __init__(self, root, body, pages):
        
        self.root = root
        self.body = body
        self.pages = pages

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        # Font styles
        menuFont = font.Font(family='Helvetica', size=20, weight='bold')
 
        # Create button objects for top bar
        Short = Button(self.body, text='Short Order', command= lambda: self.click(0, self.pages))
        Bulk = Button(self.body, text='Bulk', width = 10, command= lambda: self.click(1, self.pages))

        # List buttons
        self.buttons = [Short, Bulk]

        # Assign button properties

        for bttn in self.buttons:
            #bttn.configure(background='#89aae0', image=pixelVirtual, width=100, height=100, compound="c")
            bttn.configure(background='#89aae0')
            bttn['font']=menuFont

        # Assign buttons in grid system
        Short.grid(column=3, row=5, columnspan=3, rowspan=5, sticky=(N, S, E, W))
        Bulk.grid(column=8, row=5,  columnspan=3, rowspan=5, sticky=(N, S, E, W))

        # Create Label Objects
        self.Userlbl = Label(self.body, text='ORDER', font=('Helvetica', 30, 'bold'))
        self.Userlbl.grid(column=4, row=2 , columnspan=6, rowspan=2, sticky=(N))

    def page_id(self):
        return 4

    def click(self, i, pages):
        for widget in self.body.winfo_children():
            widget.destroy()
        
        self.i = i
        if(self.i == 1):
            self.pages.append(9)
            self.cspage_ = cs_page(self.root, self.body, pages)
        else:
            self.pages.append(10)
            cs = {"type": 'short'}
            self.orderprocess_= order_process(self.root, self.body, pages, cs)
        pass
        pass
