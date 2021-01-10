from tkinter import *
from tkinter import ttk
import tkinter.font as font
from table import table
import time
from prompt import *
class i_page(ttk.Frame, Tk):
    
    # Populate listbox with _list
    _list=[]
    for i in range(22):
        _list.append('<item> '+ str(i))

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
                        column_id=("ID", "Item Name", "Category", "Stock","Price"), 
                        rowheight = 80, height = 7, font_size = 18, font = 'Helvetica',
                        tablecol_width = 120, headingfont= 30)
        self.Table_.test()

        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)
        
    def OnDoubleClick(self, event):
        item = self.Table_.tree.selection()[0]
        self.Table_.tree.insert('', 'end', values=('sddsd'))
        print("you clicked on", self.Table_.tree.item(item,"text"))
        history(1, self.body, self.root)

    def page_id(self):
        return 10

    def click(self, i):
        pass

    def create_cat(self):
         # Labels
        self.Add_stock = Button(self.labels, text='Add stock', font=('Helvetica', 18, 'bold'), command = self.choose_item)
        self.Add_stock.grid(column=0, row=1 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Add_item = Button(self.labels, text='Add item', font=('Helvetica', 18, 'bold'), command = self.choose_item)
        self.Add_item.grid(column=4, row=1 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Update_item = Button(self.labels, text='Update item', font=('Helvetica', 18, 'bold'), command = self.choose_item)
        self.Update_item.grid(column=0, row=7 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Delete_item = Button(self.labels, text='Delete Item', font=('Helvetica', 18, 'bold'), command = self.choose_item)
        self.Delete_item.grid(column=4, row=7 , columnspan=3, rowspan=6, sticky=N+S+E+W)

    def destroy_button(self):
        self.Add_stock.destroy()
        self.Add_item.destroy()
        self.Update_item.destroy()
        self.Delete_item.destroy()

    def choose_cat(self):
        self.create_cat()


    def choose_item(self, type):
        #self.destroy_button()

        if (type==0):
            self.Add_item_label = Button(self.labels, 
                                        text='Add an item', 
                                        font=('Helvetica', 30, 'bold'),
                                        command= lambda: self.add_update(1))
            self.Add_item_label.grid(column=0, row=0 , columnspan=3, rowspan=1, sticky=N+S+E, pady=(20,20))
        
            self.Delete_item_label = Button(self.labels, 
                                            text='Delete item', 
                                            font=('Helvetica', 30, 'bold'),
                                            command= lambda: self.click(3))
            self.Delete_item_label.grid(column=3, row=0 , columnspan=3, rowspan=1, sticky=N+S+E, pady=(20,20))
        else:
            self.Add_item_label.destroy()
            self.Delete_item_label.destroy()

            self.Add_item_label = Button(self.labels, 
                                        text='Update an item', 
                                        font=('Helvetica', 30, 'bold'),
                                        command= lambda: self.add_update(0))
            self.Add_item_label.grid(column=0, row=0 , columnspan=3, rowspan=1, sticky=N+S+E, pady=(20,20))


        self.id = Label(self.labels, text = "ID", font = ("Helvetica", 25, 'bold'))
        self.id.grid(column=0, row=1 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))
        
        self.id_e= Entry(self.labels, width = 12, font = ("Helvetica", 25, 'bold'))
        self.id_e.grid(column=1, row=1 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.itemname = Label(self.labels, text = "Item name", font = ("Helvetica", 25, 'bold'))
        self.itemname.grid(column=0, row=2 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.itemname_e= Entry(self.labels, width = 12, font = ("Helvetica", 25, 'bold'))
        self.itemname_e.grid(column=1, row=2 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.item_cat_list = ["Ready to cook", "Cooked", "Pork", "Chicken"]

        self.item_cat = ttk.Combobox(self.labels, width=12, values=self.item_cat_list, font = ("Helvetica", 22, 'bold'), state='readonly')
        self.item_cat.grid(column=1, row=3 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))
        
        self.item_cat = Label(self.labels, text = "Category", font = ("Helvetica", 25, 'bold'))
        self.item_cat.grid(column=0, row=3 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.current_st = Label(self.labels, text = "Current Stock", font = ("Helvetica", 25, 'bold'))
        self.current_st.grid(column=0, row=4 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.current_ste = Entry(self.labels,width=12, font = ("Helvetica", 25, 'bold'))
        self.current_ste.grid(column=1, row=4 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.enter_stock = Label(self.labels, text = "Enter Price", font = ("Helvetica", 25, 'bold'))
        self.enter_stock.grid(column=0, row=5 , columnspan=1, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.enter_stock= Entry(self.labels, width = 12, font = ("Helvetica", 25, 'bold'))
        self.enter_stock.grid(column=1, row=5 , columnspan=5, rowspan=1, sticky=(E), pady=(15,15), padx=(20,20))

        self.cancel_ = Button(self.labels, width=12, text='Cancel', font=('Helvetica', 18, 'bold'), command = self.cancel)
        self.cancel_.grid(column=0, row=6 , columnspan=3, rowspan=1,  pady=(15,15), padx=(20,20))

        self.confirm_ = Button(self.labels, width=12, text='Confirm', font=('Helvetica', 18, 'bold'), command = self.confirm)
        self.confirm_.grid(column=3, row=6 , columnspan=3, rowspan=1,  pady=(15,15), padx=(20,20))

        pass

    def cancel(self):
        # for widget in self.labels.winfo_children():
        #     widget.destroy()
        # print(Toplevel.winfo_exists(self.prompt_.promptWindow))
        # self.choose_item()
        pass
    def confirm(self):
        self.prompt_ = confirm_inv(1, self.body, self.labels, self.root)
        print("ha")
        if (self.prompt_.confirm_bool==TRUE):
            self.choose_item(0)

    def add_update(self, type):
        for Widget in self.labels.winfo_children():
            Widget.destroy()

        self.choose_item(type)
