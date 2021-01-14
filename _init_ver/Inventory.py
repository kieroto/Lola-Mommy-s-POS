from tkinter import *
from tkinter import ttk
import tkinter.font as font
from datetime import date, datetime
from tkinter import messagebox 
from table import table
import time
from prompt import *
import util
import sqlite3
import CRUD
class i_page(ttk.Frame, Tk):
    
    # Populate listbox with _list
    def callback_entry(self, P):
        if str.isdigit(P) or P == "":
            if P != "":
                return True if int(P) >= 0 else False
            else:
                return True
            return True
        else:
            return False

    def __init__(self, root, body, Page_tracker):
        self._list_inv = CRUD.retrieve_product()
        self.root = root
        self.body = body
        self.vcmd = (self.body.register(self.callback_entry))
        self.tracker=Page_tracker

        #################################################
        self.menuFont = font.Font(family='Helvetica', size=20)
        

        # Create frame for scrollpane/buttons and label
        self.labels = ttk.Frame(self.body)
        self.labels.grid(column = 0, row = 0, rowspan=23, columnspan=2, sticky=N+S+E+W)

        # Configure Grid system for scrollpane/buttons and label
        for i in range(0,23):
            self.labels.rowconfigure(i, weight=1)
      
        for i in range(0,8):
            self.labels.columnconfigure(i, weight=1)
        # self.labels.columnconfigure(8, weight=1)

        #self.create_cat()
        
        self.Add_item_label = Button(self.labels, 
                            width = 10,
                            text='Add\nan item', 
                            font=('Helvetica', 22, 'bold'),
                            command= lambda: self.add_update(1))
        self.Add_item_label.grid(column=0, row=0 , columnspan=1, rowspan=1, sticky=N+S+E+W, pady=(10,10))

        self.Update_item_label = Button(self.labels,
                                width = 10, 
                                text='Update\nan item', 
                                font=('Helvetica', 22, 'bold'),
                                command= lambda: self.add_update(0))
        self.Update_item_label.grid(column=1, row=0 , columnspan=1, rowspan=1, sticky=N+S+E+W, pady=(10,10))
        self.choose_item(0)
        # Create frame for scrollpane 
        self.tableframe = ttk.Frame(self.body)
        self.tableframe.grid(column = 2, row = 1, rowspan=23, columnspan=8,sticky=N+S+E+W)


        # Configure Grid system for scrollpane
        for i in range(0,23):
            self.tableframe.rowconfigure(i, weight=1)

        for i in range(0,5):
            self.tableframe.columnconfigure(i, weight=1)

        # Create table
        row_place = 10
        col_place = 1
        self.Table_ = table(frame= self.tableframe, tree_row=row_place, tree_col=col_place, 
                        column_id=("ID", "Item Name", "Category", "Price", "WS Price", "Min WS", "Stock"), 
                        rowheight = 80, height = 7, font_size = 18, font = 'Helvetica',
                        tablecol_width = 230, headingfont= 30)
        self.Table_.tree.column("ID", width = 60)
        self.Table_.tree.column("Price", width = 70)
        self.Table_.tree.column("Category", width = 230)
        self.Table_.tree.column("Stock", width = 70)
        self.Table_.tree.column("WS Price", width = 70)
        self.Table_.tree.column("Min WS", width = 70)

        for row in self._list_inv:
            self.Table_.tree.insert('', '0', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        child_id = self.Table_.tree.get_children()[0]
        self.Table_.tree.focus(child_id)
        self.Table_.tree.selection_set(child_id)

        #self.Table_.tree.bind("<Key>", self.select)
        self.Table_.tree.bind("<<TreeviewSelect>>", self.select_row)
        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)
        
    def select_row(self, event):
        entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
        print(entryIndex)
        try:
            widget = event.widget
            selected=widget.selection()
        except IndexError:
            return
    
        self.id_e.delete(0, "end")
        self.itemname_e.delete(0, "end")
        self.item_cate.delete(0, "end")
        self.enter_prce.delete(0, "end")
        self.enter_WSprce.delete(0, "end")
        self.enter_minWSe.delete(0, "end")
        self.current_ste.delete(0,"end")
        
        self.id_e.insert(0, self.Table_.tree.item(selected)['values'][0])
        self.itemname_e.insert(0, self.Table_.tree.item(selected)['values'][1])
        for i in range(0,4):
            if (self.item_cat_list[i] == (self.Table_.tree.item(selected)['values'][2])):
                self.item_cate.current(i)
        self.enter_prce.insert(0, self.Table_.tree.item(selected)['values'][3])
        self.enter_WSprce.insert(0, self.Table_.tree.item(selected)['values'][4])
        self.enter_minWSe.insert(0, self.Table_.tree.item(selected)['values'][5])
        self.current_ste.insert(0, self.Table_.tree.item(selected)['values'][6])

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

    def OnDoubleClick(self, event):
        region = self.Table_.tree.identify("region", event.x, event.y)
        if region == "heading":
            columns = ('ID', 'Item Name', 'Category', 'Price', 'WS Price', 'Min WS', 'Stock')
            for col in columns:
                self.Table_.tree.heading(col, text=col, command=lambda _col=col: \
                            self.treeview_sort_column(self.Table_.tree, _col, False))
            return
        entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
        print(entryIndex)
        try:
            widget = event.widget
            selected=widget.selection()
        except IndexError:
            return
        
        pid=self.Table_.tree.item(selected)['values'][0]
        name=self.Table_.tree.item(selected)['values'][1]
        itemcat=self.Table_.tree.item(selected)['values'][2]
        price=self.Table_.tree.item(selected)['values'][3]
        wsprice=self.Table_.tree.item(selected)['values'][4]
        minws=self.Table_.tree.item(selected)['values'][5]
        stock=self.Table_.tree.item(selected)['values'][6]

        
        messagebox.showinfo("showinfo", "Product Information\n" +
                            "ID " + str(pid) + "\n " + str(name) + "\n " +str(itemcat)+
                            "\nReg price: P" +str(price) +"\nWholesale price: P" + str(wsprice) +
                            "\nMinimum wholesale: "+ str(minws) + "\nStock : " + str(stock)) 
    #     widget = event.widget
    #     selected=widget.selection()[0]
    #    # print(selected)
    #     print(self.Table_.tree.item(selected)['values'][0])

    def page_id(self):
        return 10

    def click(self, i):
        pass
    def cancel(self):
        pass
    
    def choose_item(self, type):
        #self.destroy_button()

        if (type==0):
            self.Update_item_label.configure(background = '#93c47d')
            self.Add_item_label.configure(background = '#f0f0f0')
        else:
            self.Update_item_label.configure(background = '#f0f0f0')
            self.Add_item_label.configure(background = '#93c47d')

        self.id = Label(self.labels, text = "ID", font = ("Helvetica", 21, 'bold'))
        self.id.grid(column=0, row=1 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))
        
        self.id_e= Entry(self.labels, width=7, font = ("Helvetica", 21, 'bold'), validate='key', validatecommand=(self.vcmd, '%P'))
        self.id_e.grid(column=1, row=1 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.itemname = Label(self.labels, text = "Item name", font = ("Helvetica", 21, 'bold'))
        self.itemname.grid(column=0, row=2 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.itemname_e= Entry(self.labels, width = 12, font = ("Helvetica", 21, 'bold'))
        self.itemname_e.grid(column=1, row=2 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.item_cat_list = ["Ready to cook", "Cooked", "Pork", "Chicken"]

        self.item_cate = ttk.Combobox(self.labels, width=12, values=self.item_cat_list, font = ("Helvetica", 20, 'bold'), state='readonly')
        self.item_cate.grid(column=1, row=3 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))
        
        self.item_cat = Label(self.labels, text = "Category", font = ("Helvetica", 21, 'bold'))
        self.item_cat.grid(column=0, row=3 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.current_st = Label(self.labels, text = "Current Stock", font = ("Helvetica", 21, 'bold'))
        self.current_st.grid(column=0, row=4 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.current_ste = Entry(self.labels,width=4, font = ("Helvetica", 21, 'bold'), validate='key', validatecommand=(self.vcmd, '%P'))
        self.current_ste.grid(column=1, row=4 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.enter_prc = Label(self.labels, text = "Enter Price", font = ("Helvetica", 21, 'bold'))
        self.enter_prc.grid(column=0, row=5 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.enter_prce= Entry(self.labels, width=7, font = ("Helvetica", 21, 'bold'), validate='key', validatecommand=(self.vcmd, '%P'))
        self.enter_prce.grid(column=1, row=5 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.enter_WSprc = Label(self.labels, text = "WS Price", font = ("Helvetica", 21, 'bold'))
        self.enter_WSprc.grid(column=0, row=6 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.enter_WSprce= Entry(self.labels, width=7, font = ("Helvetica", 21, 'bold'), validate='key', validatecommand=(self.vcmd, '%P'))
        self.enter_WSprce.grid(column=1, row=6 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.enter_minWS = Label(self.labels, text = "Min WS Qty", font = ("Helvetica", 21, 'bold'))
        self.enter_minWS.grid(column=0, row=7 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.enter_minWSe= Entry(self.labels, width=7, font = ("Helvetica", 21, 'bold'), validate='key', validatecommand=(self.vcmd, '%P'))
        self.enter_minWSe.grid(column=1, row=7 , columnspan=1, rowspan=1, sticky=(E), pady=(10,10), padx=(10,10))

        self.cancel_ = Button(self.labels, width=10, text='Delete', font=('Helvetica', 21, 'bold'), command = self.delete)
        self.cancel_.grid(column=0, row=8 , columnspan=1, rowspan=1,  pady=(10,10), padx=(10,10))

        self.confirm_ = Button(self.labels, width=10, text='Confirm', font=('Helvetica', 21, 'bold'), command= lambda: self.confirm(type))
        self.confirm_.grid(column=1, row=8 , columnspan=1, rowspan=1,  pady=(10,10), padx=(10,10))



    def confirm(self, type):
        if(self.tracker.bin[1] == '0'):
            messagebox.showwarning("showwarning", "Your account doesn't have this privilege")
            return
        pid=self.id_e.get()
        name=self.itemname_e.get()
        itemcat=self.item_cate.get()
        price=self.enter_prce.get()
        wsprice=self.enter_WSprce.get()
        minws=self.enter_minWSe.get()
        stock=self.current_ste.get()  

        hid = util.history()
        _time = datetime.now().strftime("%H:%M:%S")
        _date = date.today().strftime("%m/%d/%y")
        _date = util.date_split(_date)
        jelly =  "ID " + str(pid) + "\n " + str(name) + "\n " +str(itemcat) + "\nReg price: P" + str(price) +"\nWholesale price: P" + str(wsprice) + "\nMinimum wholesale: "+ str(minws) + "\nStock : " + str(stock)
        
        if (type == 1):
            #self.prompt_ = confirm_inv(1, self.body, self.labels, self.root)
            #if (self.prompt_.confirm_bool==TRUE):
            if messagebox.askyesno("message", "Add Product?"):
                try:
                    CRUD.add_product(pid, name, itemcat, price, wsprice,
                                    minws, stock)
                except sqlite3.IntegrityError:
                    messagebox.showwarning("showwarning", "Can't add, Product ID already exist")
                    return
                #insert = [pid, name, itemcat, price, wsprice, minws, stock]
                self.Table_.tree.insert('', '0', values=(pid, name, itemcat, price, wsprice, minws, stock))
                jelly = "Added product\n" +jelly
                CRUD.add_history(str(hid), 'inventory', self.tracker.user[0], jelly, _date, _time)
                # self._list_inv.append(insert)
                # self.invtable.set(self._list_inv)
            else:
                pass
        else:
            if messagebox.askyesno("message", "Confirm change?"):
                entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
                CRUD.update_product(pid, name, itemcat, price, wsprice,
                            minws, stock)
                self.Table_.tree.delete(self.Table_.tree.selection())
                jelly = "Updated product\n" + jelly
                CRUD.add_history(str(hid), 'inventory', self.tracker.user[0], jelly, _date, _time)
                self.Table_.tree.insert('', entryIndex, values=(pid, name, itemcat, price, wsprice, minws, stock))
            else:
                pass
            pass

    def add_update(self, type):
        # for Widget in self.labels.winfo_children():
        #     Widget.destroy()
        
        self.choose_item(type)

    def delete(self):
        if(self.tracker.bin[1] == '0'):
            messagebox.showwarning("showwarning", "Your account doesn't have this privilege")
            return
        selected_item = self.Table_.tree.selection() ## get selected item
        print(selected_item)
        row=self.Table_.tree.item(selected_item)['values']
        if messagebox.askyesno("message", "Delete Product?"):
            CRUD.delete_product(str(row[0]))
            self.Table_.tree.delete(selected_item)

            _time = datetime.now().strftime("%H:%M:%S")
            _date = date.today().strftime("%m/%d/%y")
            _date = util.date_split(_date)

            hid = util.history()
            jelly = " Deleted Product\n" + "ID " + str(row[0]) + "\n " + str(row[1]) + "\n " +str(row[2])+"\nReg price: P" +str(row[3]) +"\nWholesale price: P" + str(row[4]) +"\nMinimum wholesale: "+ str(row[5]) + "\nStock : " + str(row[6])
            CRUD.add_history(str(hid), 'inventory', self.tracker.user[0], jelly, _date, _time)
        else:
            pass