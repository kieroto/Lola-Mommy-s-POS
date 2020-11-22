from tkinter import *
from PIL import ImageTk, Image

class Login:

	def __init__(self):

		self.loginwindow = Tk()
		self.top = Toplevel()
		self.top.title("LOGIN SCREEN")
		self.top.geometry("1280x720")

		self.photo = Image.open('logo1.png')
		self.photo = self.photo.resize((480, 220), Image.ANTIALIAS)
		self.photoImg =  ImageTk.PhotoImage(self.photo)
		self.logo = Label(self.top, image = self.photoImg)
		self.logo.place(x = 390, y = 45)

		#Initializes username and password to string; default value is empty string
		self.userName = StringVar()
		self.password = StringVar()

		#Label and entry for username
		self.label = Label(self.top, text = "Username:", font = ("Helvetica", 16))
		self.label.place(x = 570, y = 310)
		self.textBox1 = Entry(self.top, textvariable = self.userName, width = 30, font = ("Helvetica", 16))
		self.textBox1.place(x = 450, y = 340)
		
		#Label and entry for password
		self.label2 = Label(self.top, text = "Password:", font = ("Helvetica", 16))
		self.label2.place(x = 570, y = 390)
		self.textBox2 = Entry(self.top, show = "*" , textvariable = self.password, width = 30, font = ("Helvetica", 16))
		self.textBox2.place(x = 450, y = 420)

		#Button for login
		self.button1 = Button(self.top, text = "Login", fg = "black", bg = "#93c47d", relief = "raised", font = ("Helvetica", 16, "bold"), command = self.validate)
		self.button1.place(x = 590, y = 510)

	def validate(self):

		#Dictionary for list of users (username : password)
		users = {'admin': 'admin', 'dev': '2000', 'client': '3000', 'employee': '4000'}

		#Saves the input for username and pasword
		username = self.userName.get()
		Pass = self.password.get()
		
		#Checks if the inputted username and password are correct or not
		if username in users:
			if (users[username] == Pass): #If username and password are correct, display main window
				self.loginwindow.deiconify()
				self.top.destroy()
			else:
				self.label3 = Label(self.top, text = "Incorrect Password", fg = "red", font = ("Helvetica", 14))
				self.label3.place(x = 525, y = 460)
		else:
			self.label3 = Label(self.top, text = "Username does not exist", fg = "red", font = ("Helvetica", 14))
			self.label3.place(x = 530, y = 460)

	def run(self):
		self.loginwindow.withdraw()
		self.loginwindow.mainloop()

app = Login()
app.run()


