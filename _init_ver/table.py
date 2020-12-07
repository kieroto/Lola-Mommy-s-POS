from tkinter import *
from tkinter import ttk

# To use <table class>
# Declare as table_name = table(frame = aTkFrame, tree_row = 0, 
#                           tree_col = 0, column_id = ('ColumnLabel1', 'ColumnLabel2'), 
#                           height = 20, rowheight = 20, font = "Helvetica", fontsize = 20)

# frame: (ttk.Frame), tree_row, tree_col: table position(int,int), column_id: List of column headings/Label(list), height: height of the table(int)
# rowheight: height of row, fontsize: fontsize, font: fontstyle
class table():
    import table_init

    def __init__(self, **kwargs):
        # Default values incase argument doesn't exist
        self.init_set(**kwargs)

        # Create style for tree
        style = ttk.Style()
        style.theme_use("vista") # clam, alt
        style.configure("Treeview",
            background = "silver",
            foreground = "black",
            rowheight = self.rowheight_, 
            font=(self.font, self.font_size)
            )
        
        style.map("Treeview",
                    background=[('selected', 'green')])

        # initialize treeview 
        tree = ttk.Treeview(self.frame, columns= self.column_id, show="headings", height=self.height_)
        tree.grid(row=self.tree_row, column=self.tree_col, columnspan=len(self.column_id), sticky=N+S+E+W)

        
        # initialize column heads
        tree['columns'] = self.column_id
    
        # Configure column weights
        for i in range(0, (len(self.column_id)-1)):
            tree.columnconfigure(i, weight=1)

        # Initialize headings
        for label in tree['columns']:
            if (label == "ID"):
                tree.heading(label, anchor = CENTER, text=label)
            else: 
                tree.heading(label, anchor = W, text=label)

        for head in tree['columns']:
            tree.column(head, width = self.tablecol_width)

        # tree.column("Name", anchor = W, minwidth=75, stretch = 0)
        # tree.insert('', 'end', values=('literal'+ str(var), var_int)

        for i in range(0, 15):
            tree.insert('', 'end', values=('literal'+ str(i), 'item_' +str(i)))

    # def handle_click(event):
    #     if (treeview.identify_region(event.x, event.y) == "separator"):
    #         return "break"

    def test(self):
        pass

    def init_set(self, **kwargs):

            self.frame = ttk.Frame()
            self.tree_row = 0
            self.tree_col = 0
            self.column_id = ('Name', 'ID')
            self.height_ = 20
            self.rowheight_ = 20
            self.font_size = 10
            self.font = "Helvetica"
            self.tablecol_width = 20

            try:
                self.frame = kwargs['frame']
            except KeyError:
                print("Argument is missing1")

            try:
                self.tree_row = kwargs['tree_row']
            except KeyError:
                print("Argument is missing2")

            try:
                self.tree_col = kwargs['tree_col']
            except KeyError:
                print("Argument is missing3")

            try:
                self.column_id = kwargs['column_id']
            except KeyError:
                print("Argument is missing4")

            try:
                self.height_ = kwargs['height']
            except KeyError:
                print("Argument is missing5")

            try:
                self.rowheight_ = kwargs['rowheight']
            except KeyError:
                print("Argument is missing6")

            try:
                self.font_size = kwargs['font_size']
            except KeyError:
                print("Argument is missing7")

            try:
                self.font = kwargs['font']
            except KeyError:
                print("Argument is missing8")

            try:
                self.tablecol_width = kwargs['tablecol_width']
            except KeyError:
                print("Argument is missing9")


######
'''
root = Tk()
frame = ttk.Frame(root)
frame.grid(rowspan=10, columnspan=10, sticky=N+S+E+W)
for i in range(0, 10):
    frame.rowconfigure(i, weight=1)
    frame.columnconfigure(i, weight=1)

Table = table(frame = frame, tree_row = 0, tree_col = 0, column_id = ('ColumnLabel1', 'ColumnLabel2'), 
                height = 5, rowheight= 80, fontsize=30, font="Times New Roman")
Table.test()

root.mainloop()
'''
######
