from tkinter import *
from tkinter import ttk
import tkinter.font as font
from datetime import date, datetime
import _tkinter
from tkinter import messagebox 
from table import table
from prompt import *
import CRUD
import util

class h_page(ttk.Frame, Tk):

    def treeview_sort_column(self, tv, col, reverse):
        try:
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)
        except IndexError:
            return
        
        try:
            l = [(int(s[0]), s[1]) for s in l]
            l.sort(reverse=reverse)
        except ValueError:
            pass

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

        # reverse sort next time
        tv.heading(col, text=col, command=lambda _col=col: \
                    self.treeview_sort_column(tv, _col, not reverse)) 

    def __init__(self, root, body, title, Page_tracker):

        menuFont = font.Font(family='Helvetica', size=15, weight='bold')
        Page_tracker.pages.append(11)
        self.tracker =Page_tracker
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
        self.Orderonly.grid(column=12, row=0 , columnspan=1, rowspan=1, sticky=(N+S+E+W), pady=(10,10), padx=(10,10))
        self.Inventory =  Button(self.title, text='Show inventory only', font=('Helvetica', 13, 'bold'), command=self.inventory)
        self.Inventory.grid(column=11, row=0 , columnspan=1, rowspan=1, sticky=(N+S+E+W), pady=(10,10), padx=(10,10))
        self.All =  Button(self.title, text='Show all', font=('Helvetica', 13, 'bold'), command=self.all)
        self.All.grid(column=10, row=0 , columnspan=1, rowspan=1, sticky=(N+S+E+W), pady=(10,10), padx=(10,10))
        self.Table_ = table(frame= self.table_frame, tree_row=3, tree_col=5,
                        column_id=("historyID", "Action Type", "User ID", "Action", "Date", "Time"), 
                        rowheight = 40 ,height = 10, font_size = 12, font = 'Helvetica',
                        tablecol_width = 180, headingfont= 30)   
        self.body = body
    
        # Populate listbox with _list
        if self.tracker.bin[0] == '0':
            if self.tracker.bin[7] == '0':
                list_his = CRUD.retrieve_history_byaction_exception("SELECT * FROM history WHERE action_type != 'order' AND action_type != 'inventory'")
            else:
                list_his = CRUD.retrieve_history_byaction_exception("SELECT * FROM history WHERE action_type != 'inventory'")
        else:
            list_his = CRUD.retrieve_history()
        list_his.reverse()
        self.Table_.tree.bind("<<TreeviewSelect>>", self.select_row)
        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)
        
        for x in list_his:
            self.Table_.tree.insert('', 'end', values=(x))

    def inventory(self):
        if self.tracker.bin[0] == '0':
            messagebox.showwarning("showwarning", "Your account doesn't have this privilege")
            return
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        self.Table_ = table(frame= self.table_frame, tree_row=3, tree_col=5,
                column_id=("historyID", "Action Type", "User ID", "Action", "Date", "Time"), 
                rowheight = 40 ,height = 10, font_size = 12, font = 'Helvetica',
                tablecol_width = 180, headingfont= 30)   
        list_his = CRUD.retrieve_history_byaction('inventory')
        list_his.reverse()
        self.Table_.tree.bind("<<TreeviewSelect>>", self.select_row)
        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)

        for x in list_his:
            self.Table_.tree.insert('', 'end', values=(x))

    def all(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        self.Table_ = table(frame= self.table_frame, tree_row=3, tree_col=5,
                column_id=("historyID", "Action Type", "User ID", "Action", "Date", "Time"), 
                rowheight = 40 ,height = 10, font_size = 12, font = 'Helvetica',
                tablecol_width = 180, headingfont= 30)   
        list_his = CRUD.retrieve_history()
        list_his.reverse()
        self.Table_.tree.bind("<<TreeviewSelect>>", self.select_row)
        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)

        for x in list_his:
            self.Table_.tree.insert('', 'end', values=(x))
    

    def OnDoubleClick(self, event):

        region = self.Table_.tree.identify("region", event.x, event.y)
        if region == "heading":
            columns = ('Order ID', 'Customer', 'Items', 'Amount', 'Date', 'Time')
            try:
                for col in columns:
                    self.Table_.tree.heading(col, text=col, command=lambda _col=col: \
                                self.treeview_sort_column(self.Table_.tree, _col, False))
            except TclError:
                columns = ('historyID', 'Action Type', 'User ID', 'Action', 'Date', 'Time')
                for col in columns:
                    self.Table_.tree.heading(col, text=col, command=lambda _col=col: \
                                self.treeview_sort_column(self.Table_.tree, _col, False))
                return

        selected_item = self.Table_.tree.selection() ## get selected item
        info = self.Table_.tree.item(selected_item)['values']
        
        name = ''
        index = 0

        if info[1] == 'order' or info[1] == 'sign' or info[1] == 'inventory' or info[1] == 'customer' or info[1] == 'void':
            messagebox.showinfo("message", str(info[3]))
            return
        for i in range(0,len(self.list_or)):
            if (int(info[0]) == int(self.list_or[i][0])):
                name = self.list_or[i][7]
                index = i
                break
 

        row = self.Table_.tree.item(selected_item)['values'][0]
        
        if messagebox.askyesno("message", "Void order of\n" + name+ "?"):
            if(self.tracker.bin[8] == '0'):
                    messagebox.showwarning("showwarning", "Your account doesn't have this privilege")
                    return
            if messagebox.askyesno("message", "Are you sure?"):
        
                util.void_order(str(self.list_or[index][0]))
                util.delete_history_entry(str(self.list_or[index][6]))
                self.list_or.pop(index)
                _time = datetime.now().strftime("%H:%M:%S")
                _date = date.today().strftime("%m/%d/%y")
                _date = util.date_split(_date)
                hid = util.history()
            
                CRUD.add_history(str(hid), 'void', 1, 'VOIDED order' + name, _date, _time)
                self.Table_.tree.delete(selected_item)

    def page_id(self):
        return 3

    def click(self, i):
        pass
    def view_orders(self):

        if(self.tracker.bin[7] == '0'):
            messagebox.showwarning("showwarning", "Your account doesn't have this privilege")
            return
            
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        ids = (util.retrieve_orderids())
        ids = list(set(ids))
        
        # for oid in ids:
        #     util.retrieve_order_single(oid)

        list_ = util.retrieve_order_from_history()
        self.list_or = []
        try:
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
        except IndexError:
            pass

        # Create Label Objects

        # Create table
        self.Table_ = table(frame=self.table_frame, tree_row=1, tree_col=5,
                            column_id=("Order ID", "Customer", "Items", "Amount", "Date", "Time"),
                            rowheight=60, height=7, font_size=12, font='Helvetica',
                            tablecol_width=420)
        self.Table_.tree.column("Order ID", width = 90)
        self.Table_.tree.column("Amount", width = 90)
        self.Table_.tree.column("Date", width = 70)
        self.Table_.tree.column("Time", width = 70)
        self.Table_.tree.column("Customer", width = 150)


        self.list_or.reverse()
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
