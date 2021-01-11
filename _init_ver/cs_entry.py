from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *
import CRUD

import sqlite3
import re
import itertools

# Dictionary list for testing
lista = ['Abba', 'Cole', 'Franz', 'Gab', 'Kaye', 'Zian']

# Ambot para asa ni, basta kailangan ni siya
def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.match(pattern, acListEntry)

class cs_page(ttk.Frame, Tk):

    # Populate listbox with _list
    _list_cus = CRUD.retrieve_customer()

    def __init__(self, root, body, pages):

        self.root = root
        self.body = body
        self.pages = pages 

        # Loop thru results
        customerList=[]
        # customerListSwitch=[]
        for row in self._list_cus:
            customerList.append(str(row[1]) + " " + str(row[2]))
            # customerListSwitch.append(str(row[2]) + " " + str(row[1]))   

        # Customer Search Label and Autocomplete Entry
        self.Userlbl = Label(self.body, text="Search Customer", font=('Helvetica', 16))
        self.Userlbl.grid(column=4, row=2)

        # Create Label Objects
        self.Userlb2 = Label(self.body, text="Customer Details", font=('Helvetica', 30, 'bold'))
        self.Userlb2.grid(column=4, row=4 , columnspan=6, rowspan=2, sticky=(N))
    
        #Label and entry for first and last name
        self.fname = Label(self.body, text = "First Name: ", font = ("Helvetica", 16))
        self.fname.grid(column=4, row=6)
        self.cfirst = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.cfirst.grid(column=5, row=6)
        # self.cfirst.insert(0, "Cole")

        self.lname = Label(self.body, text = "Last Name: ", font = ("Helvetica", 16))
        self.lname.grid(column=4, row=7)
        self.clast = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.clast.grid(column=5, row=7)
        # self.clast.insert(0, "Ang")

        #Label and entry for address name
        self.addr = Label(self.body, text = "Address: ", font = ("Helvetica", 16))
        self.addr.grid(column=4, row=8)
        self.caddr = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.caddr.grid(column=5, row=8)
        # self.caddr.insert(0, "Davao City")

        #Label and entry for mobile
        self.mobile = Label(self.body, text = "Mobile number: ", font = ("Helvetica", 16))
        self.mobile.grid(column=4, row=9)
        self.cmobile = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.cmobile.grid(column=5, row=9)
        # self.cmobile.insert(0, "09123456789")

        # Autocomplete class widget
        self.entry = AutocompleteEntry(customerList, self._list_cus, self.cfirst, self.clast, self.caddr, self.cmobile, self.body, listboxLength=6, width=20, matchesFunction=matches, font=('Helvetica', 16))
        self.entry.grid(column=5, row=2)


        self.customerConfirmBtn = Button(self.body, text="Confirm", font = ("Helvetica", 16), command=self.confirm_click)
        self.customerConfirmBtn.grid(column=4, row=10 , columnspan=6, rowspan=2, sticky=(N))

        self.customerClearBtn = Button(self.body, text="Clear", font = ("Helvetica", 16), command=self.clear_click)
        self.customerClearBtn.grid(column=2, row=10 , columnspan=6, rowspan=2, sticky=(N))

        # Label for Error Message
        self.error_lb = Label(self.body, fg = "red", font = ("Helvetica", 14))
        
    def page_id(self):
        return 9

    def confirm_click(self):
        self.entry.listbox.destroy()
        self.entry.listboxUp = False
        self.entry.icursor(END)

        if(self.cfirst.get() != '' or self.clast.get() != ''):
            self.error_lb.configure(text=" ")
            self.customerDetails={"customerFirst": self.cfirst.get(), "customerLast": self.clast.get(), "mobile": self.cmobile.get(), "address": self.caddr.get()}
            Confirm_prompt = confirm_customer(1, self.customerConfirmBtn, self.customerDetails, self.root, self.body, self.pages)
        else:
            self.error_lb.configure(text="Fill up first and last name")       # Displays error if incomplete
            self.error_lb.grid(column=5, row=14)

    def clear_click(self):
        self.entry.delete(0,END)
        self.cfirst.delete(0, END)
        self.clast.delete(0, END)
        self.caddr.delete(0, END)
        self.cmobile.delete(0, END)
        
    def click(self, i):
        pass

# New source, Autocomplete class taken from : https://gist.github.com/uroshekic/11078820
# Remaining Bugs:
# - First entry is defaultly selected, but not highlighted
# - Cant search based on last name
class AutocompleteEntry(Entry):
    def __init__(self, customerList, _list_cus, cfirst, clast, caddr, cmobile, *args, **kwargs):

        if 'listboxLength' in kwargs:
            self.listboxLength = kwargs['listboxLength']
            del kwargs['listboxLength']
        else:
            self.listboxLength = 8

        # Custom matches function
        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)
                
            self.matchesFunction = matches

        Entry.__init__(self, *args, **kwargs)
        self.focus()

        self.customerList = customerList
        self.cfirst = cfirst
        self.clast = clast
        self.caddr = caddr
        self.cmobile = cmobile
        self._list_cus = _list_cus
        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.moveUp)
        self.bind("<Down>", self.moveDown)
        self.bind("<Return>", self.selection)

        self.listboxUp = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.listboxUp:
                self.listbox.destroy()
                self.listboxUp = False
        else:
            words = self.comparison()
            if words:
                if not self.listboxUp:
                    self.listbox = Listbox(width=self["width"], height=self.listboxLength)
                    self.listbox.bind("<Button-1>", self.selection)
                    self.listbox.bind("<Right>", self.selection)
                    self.listbox.place(x=self.winfo_x(), y=self.winfo_y() + self.winfo_height())
                    self.listboxUp = True
                    # self.listbox.selection_set(first=0) #this is the olonemdosjkmpkmsodkvnsokvnfkbmfbmfoskbmkgobmkgombkgomd,lbmg,blmdkobmg,bmlsdsdsdsdsdsdsdsdsdsdfrff
                
                self.listbox.delete(0, END)
                for w in words:
                    self.listbox.insert(END,w)
            else:
                if self.listboxUp:
                    self.listbox.destroy()
                    self.listboxUp = False

    def selection(self, event):
        if self.listboxUp:
            self.var.set(self.listbox.get(ACTIVE))
            # print(self.listbox.get(ACTIVE))

            for row in self._list_cus:
                if str(str(row[1]) + " " + str(row[2])) == str(self.listbox.get(ACTIVE)):
                    customer_id = row[0]

            detailList=[]
            for rec in self._list_cus[customer_id - 1]:
                detailList.append(rec)

            self.listbox.destroy()
            self.listboxUp = False
            self.icursor(END)

            self.cfirst.delete(0, END)
            self.clast.delete(0, END)
            self.caddr.delete(0, END)
            self.cmobile.delete(0, END)

            self.cfirst.insert(0, detailList[1])
            self.clast.insert(0, detailList[2])
            self.caddr.insert(0, detailList[3])
            self.cmobile.insert(0, detailList[4])

    def moveUp(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != '0':                
                self.listbox.selection_clear(first=index)
                index = str(int(index) - 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index)

    def moveDown(self, event):
        if self.listboxUp:
            if self.listbox.curselection() == ():
                index = '0'
            else:
                index = self.listbox.curselection()[0]
                
            if index != END:                        
                self.listbox.selection_clear(first=index)
                index = str(int(index) + 1)
                
                self.listbox.see(index) # Scroll!
                self.listbox.selection_set(first=index)
                self.listbox.activate(index) 


    def comparison(self):

        # self.splitAll=[]
        # for c in self.customerList:
        #     splitName = c.split(" ")
        #     for s in splitName:
        #         self.splitAll.append(s)
        # print(self.splitAll)

        return [ w for w in self.customerList if self.matchesFunction(self.var.get(), w) ]

# Autocomplete class and def taken from https://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/
# Temp sa ni, kay stylize pa langman. Not sure how this works v: 
# BUGS: 
# 1) When clicking <Down>, skips first entry
# 2) When typing 'a', only shows results with 'a', does not show 'A'
# 3) Leaving the suggestions displayed, then clicking Confirm below, does not destroy the suggestions
# class AutocompleteEntry(Entry):
#     def __init__(self, lista, *args, **kwargs):
    
#         Entry.__init__(self, *args, **kwargs)
#         self.lista = lista        
#         self.var = self["textvariable"]
#         if self.var == '':
#             self.var = self["textvariable"] = StringVar()

#         self.var.trace('w', self.changed)
#         self.bind("<Return>", self.selection)
#         self.bind("<Up>", self.up)
#         self.bind("<Down>", self.down)
        
#         self.lb_up = False

#     def changed(self, name, index, mode):  

#         if self.var.get() == '':
#             self.lb.destroy()
#             self.lb_up = False
#         else:
#             words = self.comparison()
#             if words:            
#                 if not self.lb_up:
#                     self.lb = Listbox()
#                     self.lb.bind("<Double-Button-1>", self.selection)
#                     self.lb.bind("<Right>", self.selection)
#                     self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
#                     self.lb_up = True
                
#                 self.lb.delete(0, END)
#                 for w in words:
#                     self.lb.insert(END,w)
#             else:
#                 if self.lb_up:
#                     self.lb.destroy()
#                     self.lb_up = False
        
#     def selection(self, event):

#         if self.lb_up:
#             self.var.set(self.lb.get(ACTIVE))
#             self.lb.destroy()
#             self.lb_up = False
#             self.icursor(END)

#     def up(self, event):

#         if self.lb_up:
#             if self.lb.curselection() == ():
#                 index = '0'
#             else:
#                 index = self.lb.curselection()[0]
#             if index != '0':                
#                 self.lb.selection_clear(first=index)
#                 index = str(int(index)-1)                
#                 self.lb.selection_set(first=index)
#                 self.lb.activate(index) 

#     def down(self, event):

#         if self.lb_up:
#             if self.lb.curselection() == ():
#                 index = '0'
#             else:
#                 index = self.lb.curselection()[0]
#             if index != END:                        
#                 self.lb.selection_clear(first=index)
#                 index = str(int(index)+1)        
#                 self.lb.selection_set(first=index)
#                 self.lb.activate(index) 

#     def comparison(self):
#         pattern = re.compile('.*' + self.var.get() + '.*')
#         return [w for w in self.lista if re.match(pattern, w)]


# if __name__ == '__main__':
#     root = Tk()

#     entry = AutocompleteEntry(lista, root)
#     entry.grid(row=0, column=0)

#     root.mainloop()