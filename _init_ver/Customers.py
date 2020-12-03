from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *

class cs_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title):

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        
        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        # Create Label Objects
        Userlbl = Label(body, text=title, font=('Helvetica', 30, 'bold'))
        Userlbl.grid(column=4, row=2 , columnspan=6, rowspan=2, sticky=(N))

        # To test confirm_customer Button
        #1-------------------------#
        lb1 = Label(body, text="Slide 10: Confirm Customer").grid(column=0,row=0)
        cFirst=Entry(body)
        cFirst.grid(column=0,row=1)
        cFirst.insert(0, "Cole")
        cLast=Entry(body)
        cLast.grid(column=0,row=2)
        cLast.insert(0, "Ang")
        cmobile=Entry(body)
        cmobile.grid(column=0,row=3)
        cmobile.insert(0, "09123456789")
        caddress=Entry(body)
        caddress.grid(column=0,row=4)
        caddress.insert(0, "Davao City")
        customerDetails={"customerFirst": cFirst.get(), "customerLast":cLast.get(), "mobile":cmobile.get(), "address":caddress.get()}

        customerConfirmBtn = Button(body, text="Confirm", command=lambda:confirm_customer(1, customerConfirmBtn, customerDetails, body))
        customerConfirmBtn.grid(column=0, row=5)
        #1end-----------------------#

    def page_id(self):
        return 1

    def click(self, i):
        pass