from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import ImageTk, Image
import tkinter.messagebox
# Default settings for prompts
class prompt_box():
	def __init__(self, promptType, master, root):
		# if prompt is login, make root window
		if(promptType==0):
			# self.promptWindow = Tk()
			# set login prompt dimensions
			prompt_width = 600
			prompt_height = 500
			
		# else, make toplevel window instead 	
		else:
			self.master = master
			self.root = root
			self.var = IntVar()
			self.var.set(0)

			self.promptWindow = Toplevel(self.master, padx=10, pady=10)
			self.promptWindow.protocol("WM_DELETE_WINDOW", self.callback)
			#self.root.protocol("WM_DELETE_WINDOW", self.callback_root)
			prompt_width = 400
			prompt_height = 300
			# root.eval(f'tk::PlaceWindow {str(second_win)} center')
		# Set default configrations for prompts here
		#1-------------------------------------------------------------#	
		# stylePrompt = ttk.Style()
		# stylePrompt.configure("All", font="Helvetica", fontsize=15)
		# To set window to center of screen
		screen_width = self.promptWindow.winfo_screenwidth()
		screen_height = self.promptWindow.winfo_screenheight()
		x = (screen_width / 2 - prompt_width / 2)
		y = (screen_height / 2 - prompt_height / 2)
		self.promptWindow.geometry(f'{prompt_width}x{prompt_height}+{int(x)}+{int(y)}')
		
		# Set Prompt Frame
		self.body = ttk.Frame(self.promptWindow, padding=(40,40,40,40))
		self.body.grid(column=0, row=0, columnspan=9, rowspan=9, sticky=(N, S, E, W))
		
		# Configure grid system
		self.promptWindow.columnconfigure(0, weight=1)
		self.promptWindow.rowconfigure(0, weight=1)
		for i in range(9):
			self.body.columnconfigure(i, weight=1)
			self.body.rowconfigure(i, weight=1)

	def callback_root(self):
		pass#print('went')
		# self.var.set(1)
		# self.callback()
		# self.root.destroy()
	def callback(self):
		self.var.set(1)
		self.promptWindow.destroy()
		#1end-------------------------------------------------------------#

class history(prompt_box):
		
	def __init__(self, promptType, body, root):
		# btn.configure(state="disabled")
		super().__init__(promptType, body, root)
		self.promptWindow.title("Confirm Customer")

class place_order(prompt_box):
		
	def __init__(self, promptType, root, body, Tracker):
		# btn.configure(state="disabled")
		super().__init__(promptType, body, root)
		self.body_ = body
		self.root = root
		self.Tracker = Tracker

		self.promptWindow.grab_set()
		self.promptWindow.title("Confirm Customer")
		cancelBtn = Button(self.body, text="Cancel", command=self.cancel)
		okBtn = Button(self.body, text="OK", command=lambda:self.confirm( Tracker))
		# dropdown = OptionMenu()

		cancelBtn.grid(column=2, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=5, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))

		print("waiting...")
		okBtn.wait_variable(self.var)
		print("done waiting./")

	def confirm(self,  Tracker):
		# for widget in self.master.winfo_children():
		# 	widget.destroy()
		self.var.set(1)
		Tracker.confirm_flag = True
		self.promptWindow.grab_release()
		self.promptWindow.destroy()
		
		

	def cancel(self):
		self.var.set(1)
		self.promptWindow.grab_release()
		self.promptWindow.destroy()
class confirm_inv(prompt_box):		
	def __init__(self, promptType, body, labels, root):
		# btn.configure(state="disabled")
		super().__init__(promptType, body, root)
		self.body_ = body
		self.confirm_bool=FALSE
		self.promptWindow.title("Confirm Customer")
	
		cancelBtn = Button(self.body, text="Cancel", command=self.cancel)
		okBtn = Button(self.body, text="OK", command=lambda:self.confirm(labels))
		# dropdown = OptionMenu()
		
		cancelBtn.grid(column=2, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=5, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))

		print("waiting...")
		self.promptWindow.wait_variable(self.var)
		print("done waiting./")

	def confirm(self, labels):
		for widget in labels.winfo_children():
			widget.destroy()
		self.confirm_bool=TRUE
		self.var.set(1)
		self.promptWindow.destroy()
	
	def cancel(self):
		self.var.set(1)
		self.promptWindow.destroy()

class quantity(prompt_box):
		
	def __init__(self, promptType, root, body, Tracker):
		# btn.configure(state="disabled")
		super().__init__(promptType, body, root)
		self.body_ = body
		self.root = root
		self.Tracker = Tracker
		self.past = Tracker.qty_change
		self.max = self.Tracker.qty_s + self.Tracker.qty_change
		vcmd = (self.body.register(self.callback_entry))

		self.promptWindow.grab_set()
		self.promptWindow.title("Confirm Customer")
		plus = Button(self.body, text="-", command=lambda:self.add(0))
		minus = Button(self.body, text="+", command=lambda:self.add(1))
		self.qty_e= Entry(self.body, validate='key', validatecommand=(vcmd, '%P'))


		cancelBtn = Button(self.body, text="Cancel", command=self.cancel)
		okBtn = Button(self.body, text="OK", command=lambda:self.confirm( Tracker))
		# dropdown = OptionMenu()


		cancelBtn.grid(column=2, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=4, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		
		plus.grid(column=1, row=4, columnspan=3, rowspan=1, sticky=(N, S, E, W))
		minus.grid(column=5, row=4, columnspan=3, rowspan=1, sticky=(N, S, E, W))
		self.qty_e.grid(column=4, row=4 , columnspan=1, rowspan=1, sticky=(N+S+E+W))
		self.qty_e.insert(0, Tracker.qty_change)

		print("waiting...")
		okBtn.wait_variable(self.var)
		print("done waiting./")

	def callback_entry(self, P):
		if str.isdigit(P) or P == "":
			if P != "":
				return True if int(P) <= self.max and int(P) >= 0 else False
			else:
				return True
		else:
			return False

	def confirm(self, Tracker):
		self.var.set(1)
		Tracker.confirm_flag = True
		Tracker.qty_change = int(self.qty_e.get())
		self.promptWindow.grab_release()
		self.promptWindow.destroy()
		pass

	def cancel(self):
		self.var.set(1)
		self.promptWindow.grab_release()
		self.promptWindow.destroy()

	def add(self, op):
		try:
			s=int(self.qty_e.get())
			self.past=s
		except ValueError:
			s=self.past
		max = self.Tracker.qty_s + self.Tracker.qty_change
		self.qty_e.delete(0, "end")
		if (op==0):
			if((s-1<0)):
				self.qty_e.insert(0, s)
			else:
				self.qty_e.insert(0, s-1)
		else:
			if (s+1>max): 
				self.qty_e.insert(0, s)
			else:
				self.qty_e.insert(0, s+1)
		pass

class confirm_customer(prompt_box):
		
	def __init__(self, promptType, btn, customerDetails, root, body):
		# btn.configure(state="disabled")
		super().__init__(promptType, body, root)
		self.root = root
		self.promptWindow.title("Confirm Customer")
		customerName = customerDetails['customerFirst'] + " " + customerDetails['customerLast']
		# Set Labels and Buttons
		lb1 = Label(self.body, text = "Processing order for: ", font=('Helvetica', 20, 'bold'))
		lb2 = Label(self.body, text = customerName, font=('Helvetica', 10))
		lb3 = Label(self.body, text = customerDetails['mobile'], font=('Helvetica', 10))
		lb4 = Label(self.body, text = customerDetails['address'], font=('Helvetica', 10))
		lb5 = Label(self.body, text = " ")
		cancelBtn = Button(self.body, text="Cancel", command=self.promptWindow.destroy)
		okBtn = Button(self.body, text="OK", command=lambda:self.confirm())
		# dropdown = OptionMenu()

		# Place Labels and Buttons on grid
		lb1.grid(column=0, row=0, columnspan=9, rowspan=2, sticky=(N, S, E, W))
		lb2.grid(column=0, row=2, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		lb3.grid(column=0, row=3, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		lb4.grid(column=0, row=4, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		lb5.grid(column=0, row=5, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		cancelBtn.grid(column=2, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=5, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))

		print("waiting...")
		self.promptWindow.wait_variable(self.var)
		print("done waiting./")

	def confirm(self):
		for widget in self.master.winfo_children():
			widget.destroy()
		self.promptWindow.destroy()
		self.var.set(1)


class add_user(prompt_box):

	def __init__(self, promptType, btn, userDetails, root, body):
		super().__init__(promptType, body, root)
		self.root = root

		self.promptWindow.title("User Added")

		lb1 = Label(self.body, text = userDetails['username'], font=('Helvetica', 15, 'bold'))
		lb2 = Label(self.body, text = "has been added to list of", font=('Helvetica', 10))
		lb3 = Label(self.body, text = userDetails['role'] + "s", font=('Helvetica', 10, 'bold'))
		okBtn = Button(self.body, text="OK", command=lambda:self.confirm())
		# lb2 = Label(self.body, text = customerName, font=('Helvetica', 10))

		lb1.grid(column=0, row=0, columnspan=9, rowspan=2, sticky=(N, S, E, W))
		lb2.grid(column=0, row=2, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		lb3.grid(column=0, row=3, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=5, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))


		print("waiting...")
		okBtn.wait_variable(self.var)
		print("done waiting./")

	def confirm(self):
		# for widget in self.master.winfo_children():
		# 	widget.destroy()
		self.var.set(1)
		self.promptWindow.destroy()

class order_exit(prompt_box):
		
	def __init__(self, promptType, root, body, Page_tracker):
		# btn.configure(state="disabled")
		super().__init__(promptType, body, root)
		self.body_ = body
		self.root = root
		
		self.promptWindow.grab_set()
		self.promptWindow.title("Confirm Exit")
	
		cancelBtn = Button(self.body, text="No", command=self.cancel)
		okBtn = Button(self.body, text="Yes", command=lambda:self.confirm(Page_tracker))
		# dropdown = OptionMenu(
		Label(self.body, text="Discard order?").grid(column=2, row=5, columnspan = 4)
		cancelBtn.grid(column=2, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=4, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		
		print("waiting...")
		okBtn.wait_variable(self.var)
		print("done waiting./")

	def confirm(self,Page_tracker):
		self.var.set(1)
		Page_tracker.confirm_flag = True
		self.promptWindow.grab_release()
		self.promptWindow.destroy()

	def cancel(self):
		self.var.set(1)
		self.promptWindow.grab_release()
		self.promptWindow.destroy()

#IGNORE THIS SECTION
#3-------------------------------------------------------------#		
# class select_quantity(prompt_box):

# 	def __init__(self, promptType, btn, item):
# 		btn.configure(state="disabled")
# 		super().__init__(promptType)

# 		promptWindow.title("Quantity")
# 		quantity = 1
# 		Usrlb1 = Label(promptWindow, text = item, font=('Helvetica', 10, 'bold'))
# 		Usrlb2 = Label(promptWindow, text = "Quantity", font=('Helvetica', 10))
# 		space = Label(promptWindow, text = " ")
# 		cancelBtn = Button(promptWindow, text="Cancel", command=promptWindow.destroy)
# 		okBtn = Button(promptWindow, text="OK")

# 		quantityInput = Entry(promptWindow, width=5)
# 		quantityInput.insert(END, quantity)

# 		subtractBtn = Button(promptWindow, text="-", command=lambda:self.click(0,quantityInput,int(quantityInput.get()),subtractBtn))
# 		addBtn = Button(promptWindow, text="+",command=lambda:self.click(1,quantityInput,int(quantityInput.get()), subtractBtn))

# 		if(quantity==1):
# 			subtractBtn['state'] = DISABLED

# 		Usrlb1.grid(column=0, row=0, columnspan=9, rowspan=1, sticky=(N, S, E, W))
# 		Usrlb2.grid(column=0, row=2, columnspan=9, rowspan=1, sticky=(N, S, E, W))
# 		quantityInput.grid(column=4, row=3, columnspan=1, rowspan=1,sticky=(N, S, E, W))
# 		subtractBtn.grid(column=2, row=3, columnspan=1, rowspan=1, sticky=(N, S, E, W))
# 		addBtn.grid(column=6, row=3, columnspan=1, rowspan=1, sticky=(N, S, E, W))
# 		space.grid(column=0, row=4, columnspan=9, rowspan=1, sticky=(N, S, E, W))
# 		cancelBtn.grid(column=1, row=5, columnspan=3, rowspan=1, sticky=(N, S, E, W))
# 		okBtn.grid(column=5, row=5, columnspan=3, rowspan=1, sticky=(N, S, E, W))

# 	def click(self, change, quantityInput, quantity, subtractBtn):
# 		quantityInput.delete(0,END)
# 		if(change == 0):
# 			quantity-=1
# 		else:
# 			quantity+=1
# 		if(quantity>1):
# 			subtractBtn['state'] = NORMAL
# 		else:
# 			subtractBtn['state'] = DISABLED
# 		quantityInput.insert(0,quantity)

# class order_place(prompt_box):
# 	def __init__(self, root, btn):
# 		promptWindow = Toplevel(root, padx=10, pady=10)
# 		promptWindow.title("Place Order")

# 		Usrlb1 = Label(promptWindow, text = "Order Success!", font=('Helvetica', 10)).pack()
# 		okBtn = Button(promptWindow, text="OK", command=promptWindow.destroy).pack()
# #

# # root = Tk()
# # # messagebox.askokcancel(title=None, message=None)

# # lb1 = Label(root, text="Slide 10: Confirm Customer").grid(column=0,row=0)
# # cFirst=Entry(root)
# # cFirst.grid(column=0,row=1)
# # cFirst.insert(0, "Cole")
# # cLast=Entry(root)
# # cLast.grid(column=0,row=2)
# # cLast.insert(0, "Ang")
# # cmobile=Entry(root)
# # cmobile.grid(column=0,row=3)
# # cmobile.insert(0, "09123456789")
# # caddress=Entry(root)
# # caddress.grid(column=0,row=4)
# # caddress.insert(0, "Davao City")
# # customerDetails={"customerFirst": cFirst.get(), "customerLast":cLast.get(), "mobile":cmobile.get(), "address":caddress.get()}

# # customerConfirmBtn = Button(root, text="Confirm", command=lambda:prompt_(1, root, customerDetails))
# # customerConfirmBtn.grid(column=0, row=5)

# # # # lb2 = Label(root, text="Slide 13: Select Quantity").grid(column=0,row=6)
# # # # item="Skinless Pork Longaniza"
# # # # quantitySelectBtn = Button(root, text="Skinless Pork Longaniza", command=lambda:prompt_(root, quantitySelectBtn, item))
# # # # quantitySelectBtn.pack()

# # # # lb3 = Label(root, text="Slide 17: Order Success/Fail").pack()
# # # # orderPlaceBtn = Button(root, text="Place Order", command=lambda:prompt_order_place(root, orderPlaceBtn))
# # # # orderPlaceBtn.pack()

# # root.mainloop()
# #3end-------------------------------------------------------------#