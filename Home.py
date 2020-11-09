from tkinter import *
from tkinter import ttk
import tkinter.font as font
from order import orderselect

class home_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title, pages):
    
        self.root = root
        self.body = body

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        # Create Label Objects
        Userlbl = Label(self.body, text='', font=('Helvetica', 30, 'bold'))
        Userlbl.grid(column=4, row=2 , columnspan=6, rowspan=2, sticky=(N))

        #create button
        self.order_page= Button(self.body, text='ORDER', command= lambda: self.click(pages))
        self.order_page.grid(column=4, row=5 , columnspan=6, rowspan=5, sticky=(N,S,W,E))
        self.order_page.configure(background='#89aae0')
        self.order_page['font']=menuFont 


    def click(self, pages):
        for widget in self.body.winfo_children():
            widget.destroy()

        pages.append(4)
        self.order_= orderselect(self.root, self.body, pages)
        pass

    def page_id(self):
        return -1