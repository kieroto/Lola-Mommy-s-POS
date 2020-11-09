from tkinter import *
from tkinter import ttk
import tkinter.font as font

class cs_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title):

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        
        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        # Create Label Objects
        Userlbl = Label(body, text=title, font=('Helvetica', 30, 'bold'))
        Userlbl.grid(column=4, row=2 , columnspan=6, rowspan=2, sticky=(N))

    def page_id(self):
        return 1

    def click(self, i):
        pass