from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *
from table import table

class c_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title, Page_tracker):

        self.root = root
        self.body = body

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        
        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        #Create label and entry for search box
        self.search_box = Entry(self.body, width=25, font = ("Helvetica", 16))
        self.search_box.grid(column=5, row=2, columnspan=6, rowspan=2)
        self.search_label = Label(self.body, text="Search Customer:", font = ("Helvetica", 16))
        self.search_label.grid(column=1, row=2, columnspan=6, rowspan=2)

        # Create table
        self.Table_ = table(frame= body, tree_row=5, tree_col=5, 
                        column_id=("Name", "Address", "Mobile Number"), 
                        rowheight = 30, height = 15, font_size = 15, font = 'Helvetica',
                        tablecol_width = 200)

    def page_id(self):
        return 1

    def click(self, i):
        pass