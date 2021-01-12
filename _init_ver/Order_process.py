from tkinter import *
from tkinter import ttk
import tkinter.font as font
from table import table
from prompt import *
import CRUD
import util
from datetime import date, datetime
from tkinter import messagebox 

_customerID = 0
_userID = 1

class order_cred():
    def __init__(self, ids, row, pn, details, uid):
        self.pid = ids[0]
        self.oid = ids[1]
        self.userID = uid
        self.customerID = details['id']
        self.productid = CRUD.retreive_name('"'+pn+'"')[0][0]
        self.pn = pn
        self.qty = row[1]
        self.ttl = row[3]
        self.date = details['date']
        self.time = details['time']
    
class quantity_change():
    def __init__(self, flag, qty_s, qty_c):
        self.confirm_flag = flag
        self.qty_s = qty_s
        self.qty_change = qty_c
        self.qty_ref = qty_c
class order_process(ttk.Frame, Tk):

    def callback(self, event):
        print('updated')
        util.undo_order(self.order_list, self.order_qty)
    
    def __init__(self, root, body, Page_tracker, cdetails):
        Page_tracker.pages.append(10)
        self.root = root
        self.body = body
        self.order_list = []
        self.order_qty = []
        self.order_price = []
        self.item_list = []
        self.c_details = cdetails
        self._userID = Page_tracker.user[0]
    
        #################################################
        self.menuFont = font.Font(family='Helvetica', size=20)

        # Create frame for scrollpane/buttons and label
        self.labels = ttk.Frame(self.body)
        self.labels.grid(column = 0, row = 0, rowspan=8, columnspan=6, sticky=N+S+E+W)
        self.labels.bind("<Destroy>", self.callback)

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
        Place_order = Button(self.body, text='Place Order ', font=('Helvetica', 30, 'bold'), command = lambda: self.place_order(Page_tracker))
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
        #self.Table_.test()
        print(type(self.Table_))
        # self.Table_.tree.insert('', '0', values=('sddsd'))
       # Total
        Total = Label(self.tableframe, text='Total:    <>', font=('Helvetica', 20, 'bold'))
        Total.grid(column=2, row=23, columnspan=5, rowspan =1, sticky=N+S+E)

        self.Table_.tree.bind("<Double-1>", self.OnDoubleClick)
        
    def OnDoubleClick(self, event):
        selected_item = self.Table_.tree.selection()[0]
        entryIndex = self.Table_.tree.index(self.Table_.tree.focus())
        print(self.order_list[entryIndex])
        product = self.order_list[entryIndex]

        product_ = CRUD.retreive_name("'"+product+"'")
        qty_s =  product_[0][6]
        self.Tracker = quantity_change(False, qty_s ,int(self.Table_.tree.item(selected_item)['values'][1]))
        quantity(1, self.root, self.body, self.Tracker)
                
        if (self.Tracker.confirm_flag == True):
            for i in range(0, len(product)):
                if (product[i]==')'):
                    product=product[i+1:]
                    break
            self.add_to_cart(product)
        
        if(self.current_cat == product_[0][2]):
            s = ("("+str(qty_s)+")"+product)
            new = ("("+str(self.Tracker.qty_s - (self.Tracker.qty_change - self.Tracker.qty_ref))+")"+product)
            i = 0
            for line in self._list:
                if (line == s):
                    self._list[i] = new
                    print(self._list)
                    self.list_var.set(self._list)
                    print(self._list)
                    break 
                i = i + 1

    def page_id(self):
        return 10

    def click(self, i):
        pass

    def create_cat(self):
         # Labels
        ordernum = Label(self.labels, text='Order : #8000', font=('Helvetica', 25, 'bold'))
        ordernum.grid(column=0, row=0, rowspan=3, columnspan=6, sticky=N+W)
        cust = Label(self.labels, text='Customer : Cole Ang', font=('Helvetica', 25, 'bold'))
        cust.grid(column=0, row=3, rowspan=3,  columnspan=6,  sticky=N+W)
        Items = Label(self.labels, text='Items', font=('Helvetica', 25, 'bold'))
        Items.grid(column=0, row=7, rowspan=1, columnspan=3,  sticky=N+W)
        #
        self.Ready_cook = Button(self.scrollpane, text='Ready \nto Cook', font=('Helvetica', 20, 'bold'), command=lambda:self.choose_item('rdy'))
        self.Ready_cook.grid(column=0, row=0 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Cooked = Button(self.scrollpane, text='Cooked', font=('Helvetica', 30, 'bold'), command=lambda:self.choose_item('ckd'))
        self.Cooked.grid(column=4, row=0 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Chicken = Button(self.scrollpane, text='Chicken', font=('Helvetica', 25, 'bold'), command=lambda:self.choose_item('chc'))
        self.Chicken.grid(column=0, row=6 , columnspan=3, rowspan=6, sticky=N+S+E+W)

        self.Pork = Button(self.scrollpane, text='Pork', font=('Helvetica', 30, 'bold'), command=lambda:self.choose_item('prk'))
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

    def choose_item(self, cat):
        self.destroy_button()
        # Create scrollbar widget
        self.scrollbar_ = Scrollbar(self.scrollpane, orient="vertical")
        self.scrollbar_.grid(row=0, column=7, rowspan=12, sticky=N+S+E+W)
        
        self.create_listbox(cat)
        # Back button
        self.Back_items = Button(self.labels, text='back', font=('Helvetica', 20, 'bold'), command = self.choose_cat)
        self.Back_items.grid(column=3, row=7 , columnspan=3, rowspan=6)   

    def retrieve_list(self,cat):
        if (cat == 'rdy'):
            self.current_cat='Ready to cook'
        elif (cat == 'ckd'):
            self.current_cat='Cooked'
        elif (cat == 'chc'):
            self.current_cat='Chicken'
        elif (cat == 'prk'):
            self.current_cat='Pork'

        row=CRUD.retrieve_category('"'+self.current_cat+'"')
        ylist = []
        flag = 0

        for i in range(0, len(self.item_list)): 
         
            if(util.check_if_exists(self.current_cat, self.item_list[i])):
                flag=1
                for j in range(1, len(self.item_list[i])):
                    row=CRUD.retreive_name("'"+self.item_list[i][j]+"'")
                    print(len(self.item_list[i]))
                    self._list.append("(" + str(row[0][6]) + ")" +  row[0][1] )
                break
        if(flag==0):
            for i in range(0, len(row) + 1):
                ylist.append(self.current_cat) if (i<1) else ylist.append(row[i-1][1] )
                try: self._list.append("(" + str(row[i][6]) + ")" +  row[i][1] )
                except IndexError: pass
            self.item_list.append(ylist)


    def create_listbox(self, cat):
        # Create Listbox widget
        self._list=[]
        self.retrieve_list(cat)
        self.list_var = StringVar(value=self._list)   
        self.list_var.set(self._list) 
        self.listbox_ = Listbox(self.scrollpane, width=10, listvariable=self.list_var)
        # Attach scrollbar to the listbox widget
        self.listbox_.config(yscrollcommand=self.scrollbar_.set)
        self.listbox_.grid(row=0, column=0, columnspan=7, rowspan=12, sticky=N+S+E+W)    
        self.scrollbar_.config(command=self.listbox_.yview)

        self.list_var.set(self._list)
        # for item in self._list:
        # # insert each new item to the end of the listbox
        #     self.listbox_.insert('end', item)
        # optionally scroll to the bottom of the listbox
        self.listbox_['font']=self.menuFont

        self.listbox_.bind("<Double-Button-1>", self.OnDouble_listbox)

    def OnDouble_listbox(self, event):
        widget = event.widget
        selection=widget.curselection()
        product=self._list[selection[0]]
        for i in range(0, len(product)):
            if (product[i]==')'):
                product=product[i+1:]
                break
        #value = widget.get(selection[0])
        import re
        qty=(re.findall('\d+', self._list[selection[0]] ))
        qty=int(qty[0])

        if(util.check_if_exists(product, self.order_list)):
            util.focus_item(util.get_index(product, self.order_list), self.Table_)
            qty_c =  int(self.Table_.tree.item(self.Table_.tree.selection())['values'][1])
            self.r = 0
        else:   
            qty_c = 1
            self.r = 1
        self.Tracker = quantity_change(False, qty-self.r, qty_c)
        quantity(1, self.root, self.body, self.Tracker)
        
        if (self.Tracker.confirm_flag == True):
            self.add_to_cart(product)
            s = self.Tracker.qty_s - (self.Tracker.qty_change - self.Tracker.qty_ref)
            self._list[selection[0]]=("("+str(s)+")"+product)
            self.list_var.set(self._list)

    def add_to_cart(self, product):
        product_ = CRUD.retreive_name("'"+product+"'")

        if(util.check_if_exists(product, self.order_list)):
            index = util.get_index(product, self.order_list)
            self.order_qty[index] = self.Tracker.qty_change
            util.replace(index, self.Table_)
            s = str(index)
        else:
            self.order_list.append(product)
            self.order_qty.append(self.Tracker.qty_change)
            s = 'end'

        qty = self.Tracker.qty_change
        price = util.wholesale_check(qty, product_)
        total = price * qty
        stock = self.Tracker.qty_s - (self.Tracker.qty_change - self.Tracker.qty_ref)
        CRUD.update_stock(str(product), int(stock))
        
        if(qty == 0):
            a = int(util.get_index(product, self.order_list))
            self.order_list.pop(a)
            self.order_qty.pop(a)
            # self.focus_item(a)
            # self.Table_.tree.delete(self.Table_.tree.selection())
        else:
            product=product.replace(" ", "")
            product=(product+" "+str(qty)+" " + str(price) + " "+ str(total))
            self.Table_.tree.insert('', s, values=(product))

        print(self.order_list)

    def place_order(self, Page_tracker):
        if not self.order_list:
            messagebox.showwarning("showwarning", "No Item listed") 
            print("No item")
            return

        _time = datetime.now().strftime("%H:%M:%S")
        _date = date.today().strftime("%m/%d/%y")
        _date = util.date_split(_date)
        self.csid = util.customer_check(self.c_details)
        sdetails={"id": self.csid, "date": _date, "time": _time}

        jelly_items=''
        for item in self.order_list:
            jelly_items=jelly_items+item+', '    

        history_text = []
        total = 0

        self.Tracker=quantity_change(False, 0, 0)
        place_order(1, self.root, self.body, self.Tracker)

        if(self.Tracker.confirm_flag == True):
            ids=util.extract_orderprev()
            ids[1] = ids[1] + 1
            try:
                for i in range(0, len(self.order_list)):
                    ids[0] = ids[0] + 1
                    util.focus_item(0, self.Table_)
                    row=self.Table_.tree.item(self.Table_.tree.selection())['values']
                    pn = self.order_list.pop(0)

                    history_text.append(pn + ' (' + str(row[1]) + ') - P' + str(row[3]))
                    total = total + int(row[3])
                    _order_cred = order_cred(ids, row, pn, sdetails, self._userID)
                    util.update_order(_order_cred)
                    self.Table_.tree.delete(self.Table_.tree.selection())
    
                jelly=''
                
                for item in history_text:
                    jelly=(jelly + item + '\n')

                if sdetails['id'] != -1:
                    jelly = (self.c_details['customerFirst'] + ' ' + 
                            self.c_details['customerLast'] + '\n' + jelly)
                else:
                     jelly = ('Short Order \n'+ jelly )

                if CRUD.retrieve_history():
                    hid = int(CRUD.retrieve_history_last()[0][0]) + 1  
                else:
                    hid = 0
                
                jelly = (jelly + '\n' + jelly_items  +'\n'+ str(total) )
                CRUD.add_history(ids[1], 'order', ids[1], jelly, _date, _time)


                for widget in self.body.winfo_children():
                    widget.destroy()
                from Home import home_page
                Page_tracker.pages=[]
                Page_tracker.pages.append(-1)
                self.home_ = home_page(self.root, self.body, 'Home', Page_tracker)
            except IndexError:
                print("No item")


            
