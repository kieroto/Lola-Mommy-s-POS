from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox 
from table import table
from prompt import *
import CRUD
import util

class h_page(ttk.Frame, Tk): 
    def __init__(self, root, body, title, Page_tracker):

        menuFont = font.Font(family='Helvetica', size=15, weight='bold')
        Page_tracker.pages.append(11)
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

        self.Orderonly =  Button(self.title, text='Show orders only', font=('Helvetica', 13, 'bold'), command=self.view_orders)
        self.Orderonly.grid(column=12, row=0 , columnspan=1, rowspan=1, sticky=(N+S+E+W))

        self.Table_ = table(frame= self.table_frame, tree_row=3, tree_col=5, 
                        column_id=("User ID", "Action", "Date", "Time"), 
                        rowheight = 40 ,height = 10, font_size = 12, font = 'Helvetica',
                        tablecol_width = 250, headingfont= 30)   
        self.body = body
    
        # Populate listbox with _list
        list_his = CRUD.retrieve_history()
        
        for x in list_his:
            self.Table_.tree.insert('', 'end', values=(x))

    def OnDoubleClick(self, event):
        item = self.Table_.tree.selection()[0]
        selected_item = self.Table_.tree.selection() ## get selected item
        entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
        if messagebox.askyesno("message", "Void order of\n" + str(self.list_or[entryIndex][7]) + "?"):
            if messagebox.askyesno("message", "Are you sure?"):
                util.void_order(str(self.list_or[entryIndex][0]))
                util.delete_history_entry(str(self.list_or[entryIndex][6]))
                self.Table_.tree.delete(selected_item)

    def page_id(self):
        return 3

    def click(self, i):
        pass
    def view_orders(self):
            for widget in self.body.winfo_children():
                widget.destroy()

            ids = (util.retrieve_orderids())
            ids = list(set(ids))
            
            # for oid in ids:
            #     util.retrieve_order_single(oid)
            self.table_frame = ttk.Frame(self.body)
            self.table_frame.grid(row=7, column=0, columnspan=14, rowspan=8, sticky=N + S + E + W)

            for i in range(0, 13):
                self.table_frame.columnconfigure(i, weight=1)

            for i in range(0, 18):
                self.table_frame.rowconfigure(i, weight=1)

            list_ = util.retrieve_order_from_history()
            self.list_or = []
            for item in list_:
                item = list(item)
                item.pop(1)
                split_ = item[2].split("\n")
                oid = split_.pop(0)
                hid = item[0]
                item[0]=oid 
                a = split_.pop()
                b = split_.pop()
                item[2]= b 
                item.insert(3, a)
                item[1]= split_[0]
               
                info = "\n".join(split_) + "\n" + a 
                item.append(hid)
                item.append(info)
                self.list_or.append(item)

            # Create Label Objects

            # Create table
            self.Table_ = table(frame=self.table_frame, tree_row=1, tree_col=5,
                                column_id=("Order ID", "Customer", "Items", "Amount", "Date", "Time"),
                                rowheight=60, height=7, font_size=12, font='Helvetica',
                                tablecol_width=200)
            # self.Table_.tree.column("Product ID", width = 90)
            # self.Table_.tree.column("Quantity", width = 90)
            # self.Table_.tree.column("Amount", width = 90)

            for x in self.list_or:
                self.Table_.tree.insert('', 'end', values=(x))

            self.Table_.tree.bind("<<TreeviewSelect>>", self.select_row)
            self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)
            # self.orderDelBtn = Button(self.table_frame, text="Void Order", font = ("Helvetica", 16), command=self.void_order)
            # self.orderDelBtn.config(height=1, width=8, background='#93c47d', state=DISABLED)
            # self.orderDelBtn.grid(column=6, row=15 , columnspan=2, rowspan=1)
        
    def select_row(self, event):
        # self.orderDelBtn.config(background='#93c47e', state=NORMAL)
        
        try:
            widget = event.widget
            selected=widget.selection()
        except IndexError:
            return
    
    # def void_order(self):
    #     selected_item = self.Table_.tree.selection() ## get selected item
    #     entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
    #     #print(selected_item)
    #     CRUD.delete_records( self.list_or[}[6],  self.list_or[7])
    #     self.Table_.tree.delete(selected_item)
