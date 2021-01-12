from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from prompt import prompt_box
from Window import window
import os
import CRUD

class login_user(prompt_box):
	def __init__(self, promptType):
		self.promptWindow = Tk()
		self.promptWindow.resizable(False, False)
		
		super().__init__(promptType, self.promptWindow, self.promptWindow)

		path = os.path.dirname(os.path.abspath(__file__)) + '\logo1.png'
		self.photo = Image.open(r""+path)
		self.promptWindow.title("LOGIN SCREEN")
		self.photo = self.photo.resize((489, 178), Image.ANTIALIAS)
		self.photoImg =  ImageTk.PhotoImage(self.photo)
		self.logo = Label(self.body, image = self.photoImg)
		self.logo.grid(column=0, row=0)

		# Initializes username and password to string; default value is empty string
		self.userName = StringVar()
		self.password = StringVar()

		# Label and entry for username
		self.label = Label(self.body, text = "Username:", font = ("Helvetica", 16))
		self.label.grid(column=0, row=1)
		self.textBox1 = Entry(self.body, textvariable = self.userName, width = 30, font = ("Helvetica", 16))
		self.textBox1.grid(column=0, row=2)
		
		# Label and entry for password
		self.label2 = Label(self.body, text = "Password:", font = ("Helvetica", 16))
		self.label2.grid(column=0, row=3)
		self.textBox2 = Entry(self.body, show = "*" , textvariable = self.password, width = 30, font = ("Helvetica", 16))
		self.textBox2.grid(column=0, row=4)

		# Button for login
		self.button1 = Button(self.body, text = "Login", fg = "black", bg = "#93c47d", relief = "raised", font = ("Helvetica", 16, "bold"), command=self.validate)
		self.button1.grid(column=0, row=5, pady=20)

		# Label for Error Message
		self.label3 = Label(self.body, fg = "red", font = ("Helvetica", 14))

		# Press enter to login
		self.promptWindow.bind("<Return>", self.validate)

	def validate(self, event=None):
		#Dictionary for list of users (username : password)
		userid = {}
		users = {}
		role = {}
		keys = CRUD.retrieve_employee()

		#Saves the input for username and pasword
		username = self.userName.get()
		Pass = self.password.get()

		for key in keys:
			if (username == key[1]):
				if (Pass == key[2]):
					self.promptWindow.destroy()
					home = window(key)
					home.root.mainloop()
				else:
					self.label3.configure(text="Incorrect Password")		# Displays error if incorrect password
					self.label3.grid(column=0, row=6)
		try:	
			self.label3.configure(text="Username does not exist")		# Displays error nonexistent username
			self.label3.grid(column=0, row=6)		
		except TclError:
			pass
		#Checks if the inputted username and password are correct or not
		# if username in users:
		# 	if (users[username] == Pass):				# If username and password are correct, display main window
		# 		self.promptWindow.destroy()
		# 		# If admin, starts window with admin privileges
		# 		user_cred = [userusername, role[username]]
		# 		home = window(user_cred)
		# 		home.root.mainloop()
		# 	else:
		# 		self.label3.configure(text="Incorrect Password")		# Displays error if incorrect password
		# 		self.label3.grid(column=0, row=6)

		# else:
		# 	self.label3.configure(text="Username does not exist")		# Displays error nonexistent username
		# 	self.label3.grid(column=0, row=6)

