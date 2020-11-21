from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font

class prompt_confirm_customer():
	def __init__(self, root,btn, customerFirst, customerLast, mobile, address):
		# customerConfirm.configure(state="disabled")
		promptWindow = Toplevel(root, padx=10, pady=10)
		promptWindow.title("Confirm Customer")

		customerName = customerFirst + " " + customerLast
		Usrlb1 = Label(promptWindow, text = "Processing order for: ", font=('Helvetica', 20, 'bold'))
		Usrlb2 = Label(promptWindow, text = customerName, font=('Helvetica', 10))
		Usrlb3 = Label(promptWindow, text = mobile, font=('Helvetica', 10))
		Usrlb4 = Label(promptWindow, text = address, font=('Helvetica', 10))
		space = Label(promptWindow, text = " ")
		cancelBtn = Button(promptWindow, text="Cancel", command=promptWindow.destroy)
		okBtn = Button(promptWindow, text="OK")

		Usrlb1.grid(column=0, row=0, columnspan=9, rowspan=2, sticky=(N, S, E, W))
		Usrlb2.grid(column=0, row=2, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		Usrlb3.grid(column=0, row=3, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		Usrlb4.grid(column=0, row=4, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		space.grid(column=0, row=5, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		cancelBtn.grid(column=2, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=5, row=6, columnspan=2, rowspan=1, sticky=(N, S, E, W))
		
class prompt_select_quantity():
	def __init__(self, root, btn, item):
		promptWindow = Toplevel(root, padx=10, pady=10)
		promptWindow.title("Quantity")

		quantity = 1
		Usrlb1 = Label(promptWindow, text = item, font=('Helvetica', 10, 'bold'))
		Usrlb2 = Label(promptWindow, text = "Quantity", font=('Helvetica', 10))
		space = Label(promptWindow, text = " ")
		cancelBtn = Button(promptWindow, text="Cancel", command=promptWindow.destroy)
		okBtn = Button(promptWindow, text="OK")

		quantityInput = Entry(promptWindow, width=5)
		quantityInput.insert(END, quantity)

		subtractBtn = Button(promptWindow, text="-", command=lambda:self.click(0,quantityInput,int(quantityInput.get()),subtractBtn))
		addBtn = Button(promptWindow, text="+",command=lambda:self.click(1,quantityInput,int(quantityInput.get()), subtractBtn))

		if(quantity==1):
			subtractBtn['state'] = DISABLED

		Usrlb1.grid(column=0, row=0, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		Usrlb2.grid(column=0, row=2, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		quantityInput.grid(column=4, row=3, columnspan=1, rowspan=1,sticky=(N, S, E, W))
		subtractBtn.grid(column=2, row=3, columnspan=1, rowspan=1, sticky=(N, S, E, W))
		addBtn.grid(column=6, row=3, columnspan=1, rowspan=1, sticky=(N, S, E, W))
		space.grid(column=0, row=4, columnspan=9, rowspan=1, sticky=(N, S, E, W))
		cancelBtn.grid(column=1, row=5, columnspan=3, rowspan=1, sticky=(N, S, E, W))
		okBtn.grid(column=5, row=5, columnspan=3, rowspan=1, sticky=(N, S, E, W))

	def click(self, change, quantityInput, quantity, subtractBtn):
		quantityInput.delete(0,END)
		if(change == 0):
			quantity-=1
		else:
			quantity+=1
		if(quantity>1):
			subtractBtn['state'] = NORMAL
		else:
			subtractBtn['state'] = DISABLED
		quantityInput.insert(0,quantity)

class prompt_order_place():
	def __init__(self, root, btn):
		promptWindow = Toplevel(root, padx=10, pady=10)
		promptWindow.title("Place Order")

		Usrlb1 = Label(promptWindow, text = "Order Success!", font=('Helvetica', 10)).pack()
		okBtn = Button(promptWindow, text="OK", command=promptWindow.destroy).pack()


root = Tk()
customerFirst="Cole"
customerLast="Ang"
mobile="09123456789"
address="Davao City"

# messagebox.askokcancel(title=None, message=None)
lb1 = Label(root, text="Slide 10: Confirm Customer").pack()
customerConfirmBtn = Button(root, text="Confirm", command=lambda:prompt_confirm_customer(root, customerConfirmBtn, customerFirst, customerLast, mobile, address))
customerConfirmBtn.pack()

lb2 = Label(root, text="Slide 13: Select Quantity").pack()
item="Skinless Pork Longaniza"
quantitySelectBtn = Button(root, text="Skinless Pork Longaniza", command=lambda:prompt_select_quantity(root, quantitySelectBtn, item))
quantitySelectBtn.pack()

lb3 = Label(root, text="Slide 17: Order Success/Fail").pack()
orderPlaceBtn = Button(root, text="Place Order", command=lambda:prompt_order_place(root, orderPlaceBtn))
orderPlaceBtn.pack()

root.mainloop()
