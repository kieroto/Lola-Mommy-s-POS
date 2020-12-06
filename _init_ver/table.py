from tkinter import *
from tkinter import ttk

class test():
    def __init__(self, **kwargs):
        print1 = kwargs['rock']
        print2 = kwargs['plant']

        print(print1)

class table():
    def __init__(self, **kwargs):
        frame = ttk.Frame()
        tree_row = 0
        tree_col = 0
        column_id = ('Name', 'ID')
        height_ = 20
        try:
            frame = kwargs['frame']
        except KeyError:
            print("Argument is missing1")

        try:
            tree_row = kwargs['tree_row']
        except KeyError:
            print("Argument is missing2")

        try:
            tree_col = kwargs['tree_col']
        except KeyError:
            print("Argument is missing3")

        try:
            column_id = kwargs['column_id']
        except KeyError:
            print("Argument is missing4")

        try:
            height_ = kwargs['height']
        except KeyError:
            print("Argument is missing5")

        #initialize treeview
        tree = ttk.Treeview(frame, columns= column_id, show="headings", height=height_)
        tree.grid(row=tree_row, column=tree_col, columnspan=len(column_id), sticky=N+S+E+W)

        
        # initialize column heads
        tree['columns'] = column_id
        # tree['columns'] = ("Name", "ID")#, "Address", "Mobile Number", "Bus Name")
        
    
        for i in range(0, (len(column_id)-1)):
            tree.columnconfigure(i, weight=1)

        # tree.rowconfigure(0, weight=1)
        # for i in range(0, rows-1):
        #     tree.rowconfigure(i, weight=1)

            
        # tree.column("#0", minwidth=75, stretch = 0)
        # tree.column("Name", anchor = W, minwidth=75, stretch = 0)
        # tree.column("ID", anchor = CENTER, minwidth=75, stretch = 0)
        # tree.column("Address", anchor = W, minwidth=75, stretch = 0)
        # tree.column("Mobile Number", anchor = W, minwidth=75, stretch = 0)
        # tree.column("Bus Name", anchor = W, minwidth=75, stretch = 0)
        
        # Initialize headings
        # tree.heading("#0", text="Label", anchor=W)
        # tree.heading("Name", text="Name", anchor=W)
        # tree.heading("ID", text="ID", anchor=CENTER)    
        # tree.heading("Address", text="Address", anchor=W)
        # tree.heading("Mobile Number", text="Mobile #", anchor=W)
        # tree.heading("Bus Name", text="Bus Name", anchor=W)

        for label in tree['columns']:
            if (label == "ID"):
                tree.heading(label, anchor = CENTER, text=label)
            else: 
                tree.heading(label, anchor = W, text=label)


        # for i in range(0, 30):
        #     tree.insert('', 'end',
        #         values=('aaaaaaaaaaaaaa'+ str(i),'bbbbbbbbbbbbbbbbbb'+ str(i),
        #         'cccccccccccccccc'+ str(i),'ddddddddddddddddd'+ str(i),
        #         'eeeeeeeeeeeeeeeeee'+ str(i)))

    # def handle_click(event):
    #     if (treeview.identify_region(event.x, event.y) == "separator"):
    #         return "break"

    def test(self):
        pass

