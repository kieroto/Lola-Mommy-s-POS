from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *
from table import table
import sqlite3
import CRUD

import re
import itertools
from itertools import chain

def matches(fieldValue, acListEntry):
    pattern = re.compile(re.escape(fieldValue) + '.*', re.IGNORECASE)
    return re.match(pattern, acListEntry)

class c_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, title, Page_tracker):

        self.root = root
        self.body = body

        # Virtual pixels to help resize button in pixels
        #pixelVirtual = PhotoImage(width=1, height=1)
        
        self._list_cus = CRUD.retrieve_customer()

        # Font styles
        menuFont = font.Font(family='Helvetica', size=15, weight='bold')

        #Create label and entry for search box


        # Create table
        self.CusTable_ = table(frame= body, tree_row=5, tree_col=5, 
                        column_id=("Name", "Address", "Mobile Number"), 
                        rowheight = 30, height = 15, font_size = 15, font = 'Helvetica',
                        tablecol_width = 200)

        for row in self._list_cus:
            self.CusTable_.tree.insert('', '0', values=(row[1] + " " + row[2], row[4], row[3]))

        self.search_box = SuggestionEntry(self.CusTable_, self._list_cus, self.body, width=25, matchesFunction=matches, font = ("Helvetica", 16))
        self.search_box.grid(column=5, row=2, columnspan=6, rowspan=2)
        self.search_label = Label(self.body, text="Search Customer:", font = ("Helvetica", 16))
        self.search_label.grid(column=1, row=2, columnspan=6, rowspan=2)

    def page_id(self):
        return 1

    def click(self, i):
        pass

class SuggestionEntry(Entry):
    def __init__(self, CusTable_, _list_cus, *args, **kwargs):

        if 'matchesFunction' in kwargs:
            self.matchesFunction = kwargs['matchesFunction']
            del kwargs['matchesFunction']
        else:
            def matches(fieldValue, acListEntry):
                pattern = re.compile('.*' + re.escape(fieldValue) + '.*', re.IGNORECASE)
                return re.match(pattern, acListEntry)
                
            self.matchesFunction = matches

        Entry.__init__(self, *args, **kwargs)

        self._list_cus = _list_cus
        self.CusTable_ = CusTable_

        self.customerList=[]
        for row in self._list_cus:
            self.customerList.append(str(row[1]) + " " + str(row[2]))

        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)

    def changed(self, name, index, mode):
        for row in self.CusTable_.tree.get_children():
                self.CusTable_.tree.delete(row)

        if self.var.get() == '':
            for row in self._list_cus:
                self.CusTable_.tree.insert('', '0', values=(row[1] + " " + row[2], row[4], row[3]))
        else:
            self.words = self.comparison()

            for row in self.flat:
                self.CusTable_.tree.insert('', '0', values=(row[1] + " " + row[2], row[4], row[3]))

    def comparison(self):
        self.name=[]
        for w in self.customerList:
            self.name.append(w.split())
        self.flatName = list(chain.from_iterable(self.name))
        self.flatName = list(dict.fromkeys(self.flatName))

        key = self.var.get()
        self.flat = CRUD.retrieve_customer_search(key)
        # self.customerList = self.name
        # return [ w for w in self.flatName if self.matchesFunction(self.var.get(), w) ]