from tkinter import *
from tkinter import ttk
from tkcalendar import *
import tkinter.font as font
import CRUD
from table import table
from datetime import timedelta, date
import calendar
from babel.dates import format_date, parse_date, get_day_names, get_month_names
from babel.numbers import * 

class s_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title, Page_tracker):

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        
        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        def title_nav():
            # Create Title
            self.Userlbl = Label(body, text=title, font=('Helvetica', 25, 'bold'))
            self.Userlbl.grid(column=4, row=0, columnspan=6, rowspan=2, sticky=(N))

            # Create Button Objects
            self.DayBttn = Button(body, text='Day', font=('Helvetica', 16, 'bold'), background='#89aae0', command=day)
            self.MultipleBttn = Button(body, text='Multiple', font=('Helvetica', 16, 'bold'), background='#89aae0', command=datefrom)

            # Assign buttons in grid system
            self.DayBttn.grid(column=3, row=2, columnspan=3, rowspan=1, sticky=(N, S, E, W))
            self.MultipleBttn.grid(column=8, row=2, columnspan=3, rowspan=1, sticky=(N, S, E, W))

        # Functions
        def day():
            for widget in body.winfo_children():
                widget.destroy()

            title_nav()

            self.calendar = Calendar(body, selectmode='day', year=2021, month=1)
            self.calendar.grid(column=2, row=4, columnspan=11, rowspan=11, sticky=(N, S, E, W))

            self.SelectBttn = Button(body, text='Select Day', font=('Helvetica', 18, 'bold'),background='#89aae0', command= lambda: view_day(self.calendar.get_date()))
            self.SelectBttn.grid(column=6, row=16, columnspan=2, rowspan=1, sticky=(N, S, E, W))

        def view_day(date):
            for widget in body.winfo_children():
                widget.destroy()

            self.title = ttk.Frame(body)
            self.title.grid(row=0, column=0, columnspan=14, rowspan=1, sticky=N + S + E + W)
            self.title.rowconfigure(0, weight=1)

            for i in range(0, 14):
                self.title.columnconfigure(i, weight=1)

            self.table_frame = ttk.Frame(body)
            self.table_frame.grid(row=7, column=0, columnspan=14, rowspan=8, sticky=N + S + E + W)

            for i in range(0, 13):
                self.table_frame.columnconfigure(i, weight=1)

            for i in range(0, 18):
                self.table_frame.rowconfigure(i, weight=1)

            title_nav()
            productNamesRaw = CRUD.retrieve_productName()
            orderQuanRaw = CRUD.retrieve_Prod_Quantity(date)

            # Variables
            total, count = 0, 0
            productNames, prod, quan, amount, list_ = [], [], [], [], []
            dic = dict()

            #Convert List Compre to List
            for elem in productNamesRaw:
                productNames.append(elem[0])

            #Split List Compre to seperate List
            for product in orderQuanRaw:
                prod.append(product[0])     #Product
                quan.append(product[1])     #Quantity
                amount.append(product[2])   #Amount

            #Create Dictionary for Product:[total quantity, total amount]
            for x in productNames:
                dic.update({x: [0, 0]})

            print(productNames)
            print(prod)
            print(quan)
            print(amount)

            # Compile all orders in date x to dictionary
            for x in productNames:
                for y in prod:
                    if count < len(prod):
                        if x == prod[count]:
                            dic[x][0] = dic[x][0] + quan[count]
                            dic[x][1] = dic[x][1] + amount[count]
                        else:
                            print('\tPair Not Equal')
                        count += 1
                count = 0

            print(dic)

            # Total Amount
            for x in amount:
                total += x

            #Final List for Insert
            for x in dic:
                list_.append(x)
                list_.append(dic[x][0])
                list_.append(dic[x][1])

            # Label for Total
            Total = Label(self.table_frame, text='Total: ' + str(total), font=('Helvetica', 20, 'bold'))
            Total.grid(column=6, row=15, columnspan=5, rowspan=1, sticky=(N + S + E + W))

            # Label for Date
            Date = Label(self.table_frame, text='Date: ' + date, font=('Helvetica', 20, 'bold'))
            Date.grid(column=2, row=15, columnspan=5, rowspan=1, sticky=(N + S + E + W))

            # Create table
            self.Table_ = table(frame=self.table_frame, tree_row=3, tree_col=5,
                                column_id=("Item", "Quantity", "Amount"),
                                rowheight=30, height=8, font_size=15, font='Helvetica',
                                tablecol_width=200)

            a, b, c = 0, 1, 2
          
            for x in list_:
                if (a < len(list_) or b < len(list_ or c < len(list_))):
                    if not (list_[b]==0):
                        self.Table_.tree.insert('', 'end', values=(list_[a], list_[b], list_[c]))
                    a += 3
                    b += 3
                    c += 3

        def datefrom():
            for widget in body.winfo_children():
                widget.destroy()

            title_nav()

            self.calendar = Calendar(body, selectmode='day', year=2021, month=1)
            self.calendar.grid(column=2, row=4, columnspan=11, rowspan=11, sticky=(N, S, E, W))

            self.SelectBttn = Button(body, text='Select First Date (From)', font=('Helvetica', 18, 'bold'), background='#89aae0', command= lambda: dateto(self.calendar.get_date()))
            self.SelectBttn.grid(column=6, row=16, columnspan=2, rowspan=1, sticky=(N, S, E, W))

        def dateto(datefrom):
            self.SelectBttn.grid_forget()

            self.SelectBttn = Button(body, text='Select Second Date (To)', font=('Helvetica', 18, 'bold'), background='#89aae0', command= lambda: view_multiple(datefrom, self.calendar.get_date()))
            self.SelectBttn.grid(column=6, row=16, columnspan=2, rowspan=1, sticky=(N, S, E, W))

            self.fromLbl = Label(body, text='From: ' + datefrom, font=('Helvetica', 20, 'bold'))
            self.fromLbl.grid(column=2, row=16, columnspan=2, rowspan=1, sticky=(N + S + E + W))

        def view_multiple(datefrom, dateto):
            for widget in body.winfo_children():
                widget.destroy()

            self.title = ttk.Frame(body)
            self.title.grid(row=0, column=0, columnspan=14, rowspan=1, sticky=N + S + E + W)
            self.title.rowconfigure(0, weight=1)

            for i in range(0, 14):
                self.title.columnconfigure(i, weight=1)

            self.table_frame = ttk.Frame(body)
            self.table_frame.grid(row=10, column=0, columnspan=14, rowspan=8, sticky=N + S + E + W)

            for i in range(0, 13):
                self.table_frame.columnconfigure(i, weight=1)

            for i in range(0, 18):
                self.table_frame.rowconfigure(i, weight=1)

            title_nav()

            #Variables
            total, count = 0, 0
            productNames, prod, quan, amount, list_, datesInBtwn, orderQuanRaw = [], [], [], [], [], [], []
            dic = dict()

            # Convert string to list_ with format 'List = [month, day, year]' for comparison
            datefromList = (datefrom.split('/'))
            datetoList = (dateto.split('/'))

            # Retrieve all dates in between datefrom and dateto
            def daterange(date1, date2):
                for n in range(int((date2 - date1).days) + 1):
                    yield date1 + timedelta(n)

            start_dt = date(int('20' + datefromList[2]), int(datefromList[0]), int(datefromList[1]))
            end_dt = date(int('20'+datetoList[2]), int(datetoList[0]), int(datetoList[1]))

            #Append all dates to list_
            for dt in daterange(start_dt, end_dt):
                datesInBtwn.append(dt.strftime("%m/%d/%y"))

            #----------------------------------------------------------------------

            #Fetch all product names
            productNamesRaw = CRUD.retrieve_productName()

            #Fetch all orders in all dates
            for x in datesInBtwn:
                orderQuanRaw = orderQuanRaw + CRUD.retrieve_Prod_Quantity(x)

            # -------------------------------------------------------------------

            # Convert List Compre to List
            for elem in productNamesRaw:
                productNames.append(elem[0])

            # Convert List Compre to List
            for elem in productNamesRaw:
                    productNames.append(elem[0])

            # Split List Compre to seperate List
            for product in orderQuanRaw:
                prod.append(product[0])  # Product
                quan.append(product[1])  # Quantity
                amount.append(product[2])  # Amount

            count = 0
            print(productNames)
            print(prod)
            print(quan)
            print(amount)

            # Create Dictionary for Product:[total quantity, total amount]
            for x in productNames:
                dic.update({x: [0, 0]})

            # Compile all orders in date x to dictionary
            for x in productNames:
                for y in prod:
                    if count < len(prod):
                        if x == prod[count]:
                            dic[x][0] = dic[x][0] + quan[count]
                            dic[x][1] = dic[x][1] + amount[count]
                        else:
                            print('\tPair Not Equal')
                        count += 1
                count = 0

            print(dic)

            # Total Amount
            for x in amount:
                total += x

            # Final List for Insert
            for x in dic:
                list_.append(x)
                list_.append(dic[x][0])
                list_.append(dic[x][1])


            # Label for Total
            Total = Label(self.table_frame, text='Total: ' + str(total), font=('Helvetica', 20, 'bold'))
            Total.grid(column=7, row=15, columnspan=1, rowspan=1, sticky=(N + S + E + W))

            # Label for Date
            fromDate = Label(self.table_frame, text='From: ' + datefrom, font=('Helvetica', 20, 'bold'))
            fromDate.grid(column=5, row=15, columnspan=1, rowspan=1, sticky=(N + S + E + W))
            toDate = Label(self.table_frame, text='To: ' + dateto, font=('Helvetica', 20, 'bold'))
            toDate.grid(column=6, row=15, columnspan=1, rowspan=1, sticky=(N + S + E + W))

            # Create table
            self.Table_ = table(frame=self.table_frame, tree_row=3, tree_col=5,
                                column_id=("Item", "Quantity", "Price"),
                                rowheight=30, height=8, font_size=15, font='Helvetica',
                                tablecol_width=200)

            a, b, c = 0, 1, 2
            print(list_)
            for x in list_:
                if (a < len(list_) or b < len(list_ or c < len(list_))):
                    if not (list_[b]==0):
                        self.Table_.tree.insert('', 'end', values=(list_[a], list_[b], list_[c]))
                    a += 3
                    b += 3
                    c += 3

        #Main
        day()


    def page_id(self):
        return 0

    def click(self, i):
        pass