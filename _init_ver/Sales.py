from tkinter import *
from tkinter import ttk
from tkcalendar import *
import tkinter.font as font
import CRUD
from table import table

class s_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title):

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
            total = 0
            count = 0
            productNames = []
            prod = []
            quan = []
            amount = []
            dic = dict()
            list = []       #final list

            #Convert List Compre to List
            for elem in productNamesRaw:
                productNames.append(elem[0])

            #Split List Compre to seperate List
            for product in orderQuanRaw:
                prod.append(product[0])
                quan.append(product[1])
                amount.append(product[2])

            #Create Dictionary for Product:[total quantity, total amount]
            for x in productNames:
                dic.update({x: [0, 0]})

            for x in productNames:
                for y in prod:
                    if x == y:
                        dic[x][0] = dic[x][0] + quan[count]
                        dic[x][1] = dic[x][1] + amount[count]
                        count = count + 1

            print(prod)
            print(quan)
            print(amount)
            print(dic)
            for x in amount:
                total = total + x
                print(total)

            #print(total)

            for x in dic:
                list.append(x)
                list.append(dic[x][0])
                list.append(dic[x][1])

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

            for x in list:
                if (a < len(list) or b < len(list or c < len(list))):
                    self.Table_.tree.insert('', 'end', values=(list[a], list[b], list[c]))
                    a += 3
                    b += 3
                    c += 3






        def datefrom():
            for widget in body.winfo_children():
                widget.destroy()

            title_nav()

            self.calendar = Calendar(body, selectmode='day', year=2021, month=1)
            self.calendar.grid(column=2, row=4, columnspan=11, rowspan=11, sticky=(N, S, E, W))

            self.SelectBttn = Button(body, text='Select First Date (From)', font=('Helvetica', 18, 'bold'), background='#89aae0', command=dateto)
            self.SelectBttn.grid(column=6, row=16, columnspan=2, rowspan=1, sticky=(N, S, E, W))

        def dateto():
            self.SelectBttn.grid_forget()

            self.SelectBttn = Button(body, text='Select Second Date (To)', font=('Helvetica', 18, 'bold'), background='#89aae0')
            self.SelectBttn.grid(column=6, row=16, columnspan=2, rowspan=1, sticky=(N, S, E, W))

        #Main
        day()



    def page_id(self):
        return 0

    def click(self, i):
        pass