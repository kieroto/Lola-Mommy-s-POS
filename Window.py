from tkinter import *
from tkinter import ttk
import tkinter.font as font
from POS_panel import main_

class window:

    def __init__(self, admin):
 
            #create tk window
            self.root= Tk()
            self.root.geometry("1280x720")
            self.root.title("Lola Mommy's Point of Sale System")
            
        
            menuFont = font.Font(family='Helvetica', size=15, weight='bold')
            s = ttk.Style()
            s.configure('body.TFrame', background = '#c9f3f5')

            # FRAMES
            # Mainframe -- whole window
            # body      -- everything below the top bar
            self.mainframe = ttk.Frame(self.root, padding=(40,40,40,40))
            self.menu = ttk.Frame(self.mainframe)
            self.body = ttk.Frame(self.mainframe)#, style='body.TFrame')

            # Assign the frames in a grid system
            # Resizeable  
            self.mainframe.grid(column=0, row=0, columnspan=14, rowspan=25, sticky=(N, S, E, W))
            self.menu.grid(column=0, row=0,  columnspan=14, rowspan=2, sticky=(N, W, E))
            self.body.grid(column=0, row=2, columnspan=14, rowspan=23, sticky=(N, S, E, W))  


            # Configure grid system
            self.root.columnconfigure(0, weight=1)
            self.root.rowconfigure(0, weight=1)

            for i in range(14):
                self.mainframe.columnconfigure(i, weight=1)
                self.menu.columnconfigure(i, weight=1)
                self.body.columnconfigure(i, weight=1)

            for i in range(25):
                self.mainframe.rowconfigure(i, weight=1)
                if (i>=23):
                    continue    
                self.body.rowconfigure(i, weight=1)

            self.menu.rowconfigure(0, weight=1)
            self.menu.rowconfigure(1, weight=1)

            # Create Menubar object and Home buttons
            self.menubar_buttons = main_(self.root, self.menu, self.body, admin, menuFont)
        
    pass
   