from tkinter import *
from tkinter import ttk
import tkinter.font as font

class order_process(ttk.Frame, Tk):
    
    def __init__(self, root, body, pages):
        
        self.root = root
        self.body = body

        #################################################
        menuFont = font.Font(family='Helvetica', size=20)

        # Create frame for scrollpane
        self.scrollpane = ttk.Frame(self.body)
        self.scrollpane.grid(column = 0, row = 0, rowspan=23, columnspan=2, sticky=N+S+E+W)

        # Configure Grid system for scrollpane
        for i in range(23):
            self.scrollpane.rowconfigure(i, weight=1)
      
        #
        self.scrollpane.columnconfigure(0, weight=10)
        self.scrollpane.columnconfigure(1, weight=1)
        
        # Create scrollbar widget
        scrollbar = Scrollbar(self.scrollpane, orient="vertical")
        scrollbar.grid(row=0, column=1, rowspan=23, sticky=N+S+E+W)
        
        # Create Listbox widget
        self.listbox = Listbox(self.scrollpane, width=8)
        # Attach scrollbar to the listbox widget
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.grid(row=0, column=0, columnspan=1, rowspan=23, sticky=N+S+E+W)
        scrollbar.config(command=self.listbox.yview)

        # Populate listbox with _list
        _list=[]
        for i in range(22):
            _list.append('<item> '+ str(i))
        for item in _list:
        # insert each new item to the end of the listbox
            self.listbox.insert('end', item)
        # optionally scroll to the bottom of the listbox
        self.listbox['font']=menuFont

 
    def page_id(self):
        return 4

    def click(self, i):
        pass
