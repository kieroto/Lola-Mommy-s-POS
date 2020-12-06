from tkinter import *
from tkinter import ttk

# To use <table class>
# Declare as table_name = table(frame = aTkFrame, tree_row = 0, tree_col = 0, column_id = ('ColumnLabel1', 'ColumnLabel2'), height = 20)
# frame: (ttk.Frame), tree_row, tree_col: table position(int,int), column_id: List of column headings/Label(list), height: height of the table(int)
class table():
    def __init__(self, **kwargs):
        # Default values incase argument doesn't exist
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
    
        # Configure column weights
        for i in range(0, (len(column_id)-1)):
            tree.columnconfigure(i, weight=1)

        # Initialize headings
        for label in tree['columns']:
            if (label == "ID"):
                tree.heading(label, anchor = CENTER, text=label)
            else: 
                tree.heading(label, anchor = W, text=label)

        # tree.column("Name", anchor = W, minwidth=75, stretch = 0)
        # tree.insert('', 'end', values=('literal'+ str(var), var_int)

    # def handle_click(event):
    #     if (treeview.identify_region(event.x, event.y) == "separator"):
    #         return "break"

    def test(self):
        pass

