from tkinter import *
from tkinter import ttk
import tkinter.font as font
from order import orderselect
from PIL import ImageTk, Image
import os
class home_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title, Page_tracker):
    
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
        # self.order_page= Button(self.body, text='ORDER', command= lambda: self.click(pages))
        # self.order_page.grid(column=4, row=5 , columnspan=6, rowspan=5, sticky=(N,S,W,E))
        # self.order_page.configure(background='#89aae0')
        # self.order_page['font']=menuFont 

        path = os.path.dirname(os.path.abspath(__file__)) + '\logo1.png'
        self.photo = Image.open(r""+path)
        self.photo = self.photo.resize((600, 218), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(self.photo)
        self.logo = Label(self.body, image = self.photoImg)
        self.logo.grid(column=6, row=7)

    def click(self, Page_tracker):
        for widget in self.body.winfo_children():
            widget.destroy()

    
        self.order_= orderselect(self.root, self.body, Page_tracker)
        pass

    def page_id(self):
        return -1