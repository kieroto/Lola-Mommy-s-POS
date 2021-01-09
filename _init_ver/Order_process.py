from tkinter import *
from tkinter import ttk
import tkinter.font as font
from table import table
from prompt import *
class order_process(ttk.Frame, Tk):
    
    def __init__(self, root, body, pages):
        
        self.root = root
        self.body = body

        #################################################
        self.menuFont = font.Font(family='Helvetica', size=20)

        # Create frame for scrollpane/buttons and label
        self.labels = ttk.Frame(self.body)
        self.labels.grid(column = 0, row = 0, rowspan=8, columnspan=6, sticky=N+S+E+W)

        self.scrollpane = ttk.Frame(self.body)
        self.scrollpane.grid(column = 0, row = 8, rowspan=12, columnspan=6, sticky=N+S+E+W)

        # Configure Grid system for scrollpane/buttons and label
        for i in range(0,8):
            self.labels.rowconfigure(i, weight=1)
      
        for i in range(0,6):
            self.labels.columnconfigure(i, weight=1)
       # self.labels.columnconfigure(8, weight=1)

        for i in range(0,12):
            self.scrollpane.rowconfigure(i, weight=1)
      
        for i in range(0,6):
            self.scrollpane.columnconfigure(i, weight=1)

        self.create_cat()

        # Create frame for scrollpane 
        self.tableframe = ttk.Frame(self.body)
        self.tableframe.grid(column = 7, row = 2, rowspan=23, columnspan=8,sticky=N+S+E+W)

        # Button
        Place_order = Button(self.body, text='Place Order ', font=('Helvetica', 30, 'bold'), command = self.place_order)
        Place_order.grid(column=8, row=0 , columnspan=3, rowspan=1, sticky=N+S+E+W)


        # Configure Grid system for scrollpane
        for i in range(0,23):
            self.tableframe.rowconfigure(i, weight=1)

        for i in range(0,5):
            self.tableframe.columnconfigure(i, weight=1)

        # Create table
        row_place = 10
        col_place = 1
        self.Table_ = table(frame= self.tableframe, tree_row=row_place, tree_col=col_place, 
                        column_id=("Item", "Quantity", "Price", "Total"), 
                        rowheight = 80, height = 5, font_size = 20, font = 'Helvetica',
                        tablecol_width = 175, headingfont= 30)
        self.Table_.test()

       # Total
        Total = Label(self.tableframe, text='Total:    <>', font=('Helvetica', 20, 'bold'))
        Total.grid(column=2, row=23, columnspan=5, rowspan =1, sticky=N+S+E)

        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)
        
    def OnDoubleClick(self, event):
        item = self.Table_.tree.selection()[0]
        print("you clicked on", self.Table_.tree.item(item,"text"))
        history(1, self.body)

    def page_id(self):
        return 4

    def click(self, i):
        pass

    def place_order(self):
        print('prompt')

    def create_cat(self):
         # Labels
        ordernum = Label(self.labels, text='Order : #8000', font=('Helvetica', 25, 'bold'))
        ordernum.grid(column=0, row=0, rowspan=3, columnspan=6, sticky=N+W)
        cust = Label(self.labels, text='Customer : Cole Ang', font=('Helvetica', 25, 'bold'))
        cust.grid(column=0, row=3, rowspan=3,  columnspan=6,  sticky=N+W)
        Items = Label(self.labels, text='Items', font=('Helvetica', 25, 'bold'))
        Items.grid(column=0, row=7, rowspan=1, columnspan=3,  sticky=N+W)
        #
        self.Ready_cook = Button(self.scrollpane, text='Ready \nto Cook', font=('Helvetica', 20, 'bold'), command = self.choose_item)
        self.Ready_cook.grid(column=0, row=0 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Cooked = Button(self.scrollpane, text='Cooked', font=('Helvetica', 30, 'bold'), command = self.choose_item)
        self.Cooked.grid(column=4, row=0 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Chicken = Button(self.scrollpane, text='Chicken', font=('Helvetica', 25, 'bold'), command = self.choose_item)
        self.Chicken.grid(column=0, row=6 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Pork = Button(self.scrollpane, text='Pork', font=('Helvetica', 30, 'bold'), command = self.choose_item)
        self.Pork.grid(column=4, row=6 , columnspan=3, rowspan=6, sticky=N+S+E+W)

    def destroy_button(self):
        self.Ready_cook.destroy()
        self.Cooked.destroy()
        self.Chicken.destroy()
        self.Pork.destroy()

    def choose_cat(self):
        self.scrollbar_.destroy()
        self.listbox_.destroy()
        self.create_cat()

    def choose_item(self):
        self.destroy_button()
        # Create scrollbar widget
        self.scrollbar_ = Scrollbar(self.scrollpane, orient="vertical")
        self.scrollbar_.grid(row=0, column=7, rowspan=12, sticky=N+S+E+W)

        # Back button
        self.Back_items = Button(self.labels, text='back', font=('Helvetica', 20, 'bold'), command = self.choose_cat)
        self.Back_items.grid(column=3, row=7 , columnspan=3, rowspan=6)

        
        # Create Listbox widget
        self.listbox_ = Listbox(self.scrollpane, width=10)
        # Attach scrollbar to the listbox widget
        self.listbox_.config(yscrollcommand=self.scrollbar_.set)
        self.listbox_.grid(row=0, column=0, columnspan=7, rowspan=12, sticky=N+S+E+W)    
        self.scrollbar_.config(command=self.listbox_.yview)

        # Populate listbox with _list
        self._list=[]
        for i in range(22):
            self._list.append('<item> '+ str(i))
        for item in self._list:
        # insert each new item to the end of the listbox
            self.listbox_.insert('end', item)
        # optionally scroll to the bottom of the listbox
        self.listbox_['font']=self.menuFont
