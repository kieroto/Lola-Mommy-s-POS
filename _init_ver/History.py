from tkinter import *
from tkinter import ttk
import tkinter.font as font
from table import table
from prompt import *
class h_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title):

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        
        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        self.title = ttk.Frame(body)
        self.title.grid(row=0, column=0, columnspan=14, rowspan=1, sticky=N+S+E+W)

        self.title.rowconfigure(0, weight=1)
        for i in range(0, 14):
            self.title.columnconfigure(i, weight=1)


        self.table_frame = ttk.Frame(body)
        self.table_frame.grid(row=4, column=0, columnspan=14, rowspan=19, sticky=N+S+E+W)

        for i in range(0, 14):
            self.table_frame.columnconfigure(i, weight=1)
        
        for i in range(0, 19):
            self.table_frame.rowconfigure(i, weight=1)

        # Create Label Objects
        Userlbl = Label(self.title, text=title, font=('Helvetica', 30, 'bold'))
        Userlbl.grid(column=4, row=0 , columnspan=6, rowspan=1, sticky=(N+S+E+W))

        Date =  Label(self.title, text='Date 8/10/20', font=('Helvetica', 20, 'bold'))
        Date.grid(column=0, row=0 , columnspan=2, rowspan=1, sticky=(N+S+E+W))

        self.Orderonly =  Button(self.title, text='Show orders only', font=('Helvetica', 13, 'bold'))
        self.Orderonly.grid(column=12, row=0 , columnspan=1, rowspan=1, sticky=(N+S+E+W))

        self.Table_ = table(frame= self.table_frame, tree_row=3, tree_col=5, 
                        column_id=("ID", "Username", "Action", "Action ID", "Dates"), 
                        rowheight = 40 ,height = 10, font_size = 12, font = 'Helvetica',
                        tablecol_width = 250, headingfont= 30)   
        self.body = body
        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)

    def OnDoubleClick(self, event):
        item = self.Table_.tree.selection()[0]
        print("you clicked on", self.Table_.tree.item(item,"text"))
        history(1, self.body)

    def page_id(self):
        return 3

    def click(self, i):
        pass