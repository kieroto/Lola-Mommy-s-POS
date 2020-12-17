from tkinter import *
from tkinter import ttk
import tkinter.font as font
from prompt import *

# Temp Dictionary list to test autocomplete while no database yet
lista = ['Abba', 'Cole', 'Franz', 'Gab', 'Kaye','Zian']
class cs_page(ttk.Frame, Tk):
    
    def __init__(self, root, body, pages):

        self.root = root
        self.body = body
       
        # Customer Search Label and Autocomplete Entry
        self.Userlbl = Label(self.body, text="Search Customer", font=('Helvetica', 16))
        self.Userlbl.grid(column=4, row=2)
        entry = AutocompleteEntry(lista, self.body, width = 20, font = ("Helvetica", 16))
        entry.grid(column=5, row=2)

        # Create Label Objects
        self.Userlb2 = Label(self.body, text="Customer Details", font=('Helvetica', 30, 'bold'))
        self.Userlb2.grid(column=4, row=4 , columnspan=6, rowspan=2, sticky=(N))
    
        #Label and entry for first and last name
        self.fname = Label(self.body, text = "First Name: ", font = ("Helvetica", 16))
        self.fname.grid(column=4, row=6)
        self.cfirst = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.cfirst.grid(column=5, row=6)
        self.cfirst.insert(0, "Cole")

        self.lname = Label(self.body, text = "Last Name: ", font = ("Helvetica", 16))
        self.lname.grid(column=4, row=7)
        self.clast = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.clast.grid(column=5, row=7)
        self.clast.insert(0, "Ang")

        #Label and entry for address name
        self.addr = Label(self.body, text = "Address: ", font = ("Helvetica", 16))
        self.addr.grid(column=4, row=8)
        self.caddr = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.caddr.grid(column=5, row=8)
        self.caddr.insert(0, "Davao City")

        #Label and entry for mobile
        self.mobile = Label(self.body, text = "Mobile number: ", font = ("Helvetica", 16))
        self.mobile.grid(column=4, row=9)
        self.cmobile = Entry(self.body, width = 20, font = ("Helvetica", 16))
        self.cmobile.grid(column=5, row=9)
        self.cmobile.insert(0, "09123456789")

        self.customerDetails={"customerFirst": self.cfirst.get(), "customerLast": self.clast.get(), "mobile": self.cmobile.get(), "address": self.caddr.get()}

        customerConfirmBtn = Button(self.body, text="Confirm", font = ("Helvetica", 16), command=lambda:confirm_customer(1, customerConfirmBtn, self.customerDetails, self.root, self.body, pages))
        customerConfirmBtn.grid(column=4, row=10 , columnspan=6, rowspan=2, sticky=(N))
       
    def page_id(self):
        return 1

    def click(self, i):
        pass

# Autocomplete class and def taken from https://code.activestate.com/recipes/578253-an-entry-with-autocompletion-for-the-tkinter-gui/
# Temp sa ni, kay stylize pa langman. Not sure how this works v: 
# BUGS: 
# 1) When clicking <Down>, skips first entry
# 2) When typing 'a', only shows results with 'a', does not show 'A'
# 3) Leaving the suggestions displayed, then clicking Confirm below, does not destroy the suggestions
class AutocompleteEntry(Entry):
    def __init__(self, lista, *args, **kwargs):
    
        Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Return>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
            self.lb.destroy()
            self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, END)
                for w in words:
                    self.lb.insert(END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]


# if __name__ == '__main__':
#     root = Tk()

#     entry = AutocompleteEntry(lista, root)
#     entry.grid(row=0, column=0)

#     root.mainloop()