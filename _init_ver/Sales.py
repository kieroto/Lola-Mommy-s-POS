from tkinter import *
from tkinter import ttk
from tkcalendar import *
import tkinter.font as font

class s_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title, Page_tracker):

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        
        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        # Functions
        def day():
            self.SelectBttn.grid_forget()

            self.SelectBttn = Button(body, text='Select Date', font=('Helvetica', 18, 'bold'), background='#89aae0')
            self.SelectBttn.grid(column=6, row=16, columnspan=3, rowspan=1, sticky=(N, S, E, W))

        def dateto():
            self.SelectBttn.grid_forget()

            self.SelectBttn = Button(body, text='Select Second Date (To)', font=('Helvetica', 18, 'bold'), background='#89aae0')
            self.SelectBttn.grid(column=6, row=16, columnspan=3, rowspan=1, sticky=(N, S, E, W))

        def datefrom():
            self.SelectBttn.grid_forget()

            self.SelectBttn = Button(body, text='Select First Date (From)', font=('Helvetica', 18, 'bold'), background='#89aae0', command=dateto)
            self.SelectBttn.grid(column=6, row=16, columnspan=3, rowspan=1, sticky=(N, S, E, W))



        # Create Label Objects
        self.Userlbl = Label(body, text=title, font=('Helvetica', 25, 'bold'))
        self.Userlbl.grid(column=4, row=0 , columnspan=6, rowspan=2, sticky=(N))

        # Create Button Objects
        self.DayBttn = Button(body, text='Day', font=('Helvetica', 18, 'bold'), background='#89aae0', command=day)
        self.MultipleBttn = Button(body, text='Multiple', font=('Helvetica', 18, 'bold'), background='#89aae0', command=datefrom)

        # Assign buttons in grid system
        self.DayBttn.grid(column=4, row=2, columnspan=3, rowspan=1, sticky=(N, S, E, W))
        self.MultipleBttn.grid(column=8, row=2, columnspan=3, rowspan=1, sticky=(N, S, E, W))

        #Default - Daily
        self.calendar = Calendar(body, selectmode='day', year=2021, month=1)
        self.calendar.grid(column=2, row=4, columnspan=11, rowspan=11, sticky=(N, S, E, W))

        self.SelectBttn = Button(body, text='Select Date', font=('Helvetica', 18, 'bold'), background='#89aae0')
        self.SelectBttn.grid(column=6, row=16, columnspan=3, rowspan=1, sticky=(N, S, E, W))


    def page_id(self):
        return 0

    def click(self, i):
        pass