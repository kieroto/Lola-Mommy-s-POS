from tkinter import *
from tkinter import ttk
import tkinter.font as font
from table import table
import time
from prompt import *
import CRUD
class i_page(ttk.Frame, Tk):
    
    # Populate listbox with _list
    _list_inv = CRUD.retrieve_product()

    def __init__(self, root, body, pages):
        
        self.root = root
        self.body = body
        self.pages = pages

        #################################################
        self.menuFont = font.Font(family='Helvetica', size=20)

        # Create frame for scrollpane/buttons and label
        self.labels = ttk.Frame(self.body)
        self.labels.grid(column = 0, row = 0, rowspan=23, columnspan=6, sticky=N+S+E+W)

        # Configure Grid system for scrollpane/buttons and label
        for i in range(0,23):
            self.labels.rowconfigure(i, weight=1)
      
        for i in range(1,6):
            self.labels.columnconfigure(i, weight=1)
        # self.labels.columnconfigure(8, weight=1)

        #self.create_cat()
        self.choose_item(0)
        # Create frame for scrollpane 
        self.tableframe = ttk.Frame(self.body)
        self.tableframe.grid(column = 7, row = 1, rowspan=23, columnspan=8,sticky=N+S+E+W)


        # Configure Grid system for scrollpane
        for i in range(0,23):
            self.tableframe.rowconfigure(i, weight=1)

        for i in range(0,5):
            self.tableframe.columnconfigure(i, weight=1)

        # Create table
        row_place = 10
        col_place = 1
        self.Table_ = table(frame= self.tableframe, tree_row=row_place, tree_col=col_place, 
                        column_id=("ID", "Item Name", "Category", "Price","WSPrice", "Min WS", "Stock"), 
                        rowheight = 80, height = 7, font_size = 18, font = 'Helvetica',
                        tablecol_width = 120, headingfont= 30)
        self.Table_.tree.column("Stock", width = 90)
        self.Table_.tree.column("Price", width = 90)
        self.Table_.tree.column("Min WS", width = 90)
        self.Table_.tree.column("WS price", width = 90)

        for row in self._list_inv:
            self.Table_.tree.insert('', '0', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        # child_id = self.Table_.tree.get_children()[0]
        # self.Table_.tree.focus(child_id)
        # self.Table_.tree.selection_set(child_id)

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
        self.Table_.tree.insert('', 'end', values=('sddsd'))
        
        self.id_e.delete(0, "end")
        self.itemname_e.delete(0, "end")
        self.item_cate.delete(0, "end")
        self.enter_prce.delete(0, "end")
        self.enter_WSprce.delete(0, "end")
        self.enter_minWSe.delete(0, "end")
        self.current_ste.delete(0,"end")
        
        self.id_e.insert(0, self.Table_.tree.item(selected)['values'][0])
        self.itemname_e.insert(0, self.Table_.tree.item(selected)['values'][1])
        self.item_cate.insert(0, self.Table_.tree.item(selected)['values'][2])
        self.enter_prce.insert(0, self.Table_.tree.item(selected)['values'][3])
        self.enter_WSprce.insert(0, self.Table_.tree.item(selected)['values'][4])
        self.enter_minWSe.insert(0, self.Table_.tree.item(selected)['values'][5])
        self.current_ste.insert(0, self.Table_.tree.item(selected)['values'][6])

    def OnDoubleClick(self, event):
        entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
        print(entryIndex)
    #     widget = event.widget
    #     selected=widget.selection()[0]
    #    # print(selected)
    #     print(self.Table_.tree.item(selected)['values'][0])
        history(1, self.body, self.root)

    def page_id(self):
        return 10

    def click(self, i):
        pass

    def choose_item(self, type):
        #self.destroy_button()

        if (type==0):
            self.Add_item_label = Button(self.labels, 
                                        text='Add an item', 
                                        font=('Helvetica', 30, 'bold'),
                                        command= lambda: self.add_update(1))
            self.Add_item_label.grid(column=0, row=0 , columnspan=3, rowspan=1, sticky=N+S+E, pady=(10,10))
        
            self.Delete_item_label = Button(self.labels, 
                                            text='Delete item', 
                                            font=('Helvetica', 30, 'bold'),
                                            command= lambda: self.delete())
            self.Delete_item_label.grid(column=3, row=0 , columnspan=3, rowspan=1, sticky=N+S+E, pady=(10,10))
        else:
            self.Add_item_label.destroy()
            self.Delete_item_label.destroy()

            self.Add_item_label = Button(self.labels, 
                                        text='Update an item', 
                                        font=('Helvetica', 30, 'bold'),
                                        command= lambda: self.add_update(0))
            self.Add_item_label.grid(column=0, row=0 , columnspan=3, rowspan=1, sticky=N+S+E, pady=(10,10))


        self.id = Label(self.labels, text = "ID", font = ("Helvetica", 25, 'bold'))
        self.id.grid(column=0, row=1 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))
        
        self.id_e= Entry(self.labels, width = 12, font = ("Helvetica", 25, 'bold'))
        self.id_e.grid(column=1, row=1 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.itemname = Label(self.labels, text = "Item name", font = ("Helvetica", 25, 'bold'))
        self.itemname.grid(column=0, row=2 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.itemname_e= Entry(self.labels, width = 12, font = ("Helvetica", 25, 'bold'))
        self.itemname_e.grid(column=1, row=2 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.item_cat_list = ["Ready to cook", "Cooked", "Pork", "Chicken"]

        self.item_cate = ttk.Combobox(self.labels, width=12, values=self.item_cat_list, font = ("Helvetica", 22, 'bold'), state='readonly')
        self.item_cate.grid(column=1, row=3 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))
        
        self.item_cat = Label(self.labels, text = "Category", font = ("Helvetica", 25, 'bold'))
        self.item_cat.grid(column=0, row=3 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.current_st = Label(self.labels, text = "Current Stock", font = ("Helvetica", 25, 'bold'))
        self.current_st.grid(column=0, row=4 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.current_ste = Entry(self.labels,width=12, font = ("Helvetica", 25, 'bold'))
        self.current_ste.grid(column=1, row=4 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.enter_prc = Label(self.labels, text = "Enter Price", font = ("Helvetica", 25, 'bold'))
        self.enter_prc.grid(column=0, row=5 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.enter_prce= Entry(self.labels, width = 12, font = ("Helvetica", 25, 'bold'))
        self.enter_prce.grid(column=1, row=5 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.enter_WSprc = Label(self.labels, text = "WS Price", font = ("Helvetica", 25, 'bold'))
        self.enter_WSprc.grid(column=0, row=6 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.enter_WSprce= Entry(self.labels, width = 15, font = ("Helvetica", 25, 'bold'))
        self.enter_WSprce.grid(column=1, row=6 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.enter_minWS = Label(self.labels, text = "Min WS Qty", font = ("Helvetica", 25, 'bold'))
        self.enter_minWS.grid(column=0, row=7 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.enter_minWSe= Entry(self.labels, width = 15, font = ("Helvetica", 25, 'bold'))
        self.enter_minWSe.grid(column=1, row=7 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(10,10))

        self.cancel_ = Button(self.labels, width=15, text='Cancel', font=('Helvetica', 25, 'bold'), command = self.cancel)
        self.cancel_.grid(column=0, row=8 , columnspan=3, rowspan=1,  pady=(15,15), padx=(10,10))

        self.confirm_ = Button(self.labels, width=15, text='Confirm', font=('Helvetica', 25, 'bold'), command= lambda: self.confirm(type))
        self.confirm_.grid(column=3, row=8 , columnspan=3, rowspan=1,  pady=(15,15), padx=(10,10))
 
    def cancel(self):
        # for widget in self.labels.winfo_children():
        #     widget.destroy()
        # print(Toplevel.winfo_exists(self.prompt_.promptWindow))
        # self.choose_item()
        pass

    def confirm(self, type):
        pid=self.id_e.get()
        name=self.itemname_e.get()
        itemcat=self.item_cate.get()
        price=self.enter_prce.get()
        wsprice=self.enter_WSprce.get()
        minws=self.enter_minWSe.get()
        stock=self.current_ste.get()  

        if (type == 1):
            self.prompt_ = confirm_inv(1, self.body, self.labels, self.root)
            if (self.prompt_.confirm_bool==TRUE):
                CRUD.add_product(pid, name, itemcat, price, wsprice,
                                minws, stock)
                #insert = [pid, name, itemcat, price, wsprice, minws, stock]
                self.Table_.tree.insert('', '0', values=(pid, name, itemcat, price, wsprice, minws, stock))
                # self._list_inv.append(insert)
                # self.invtable.set(self._list_inv)
                self.choose_item(0)
        else:
            entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
            self.delete()
            self.Table_.tree.insert('', entryIndex, values=(pid, name, itemcat, price, wsprice, minws, stock))
            pass

    def add_update(self, type):
        for Widget in self.labels.winfo_children():
            Widget.destroy()

        self.choose_item(type)

    def delete(self):
        selected_item = self.Table_.tree.selection() ## get selected item
        print(selected_item)
        self.Table_.tree.delete(selected_item)