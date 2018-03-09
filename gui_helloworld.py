"""
A simple "Hello World" application using the tkinter library.
"""

# import tkinter as tk
from tkinter import *

class Application(Frame): #tk.Frame):
	def __init__(self, master=None):
	
		# Call super() to inherit Frame base class __init__ method
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there = Button(self) #tk.Button(self)
		
		# Configure button options individually
		self.hi_there["text"] = "Hello World\n(click me)"
		self.hi_there["command"] = self.say_hi
		self.hi_there.pack(side="top")

		# Alternative way to configure button options
		self.quit = Button(self, text="QUIT", fg="red", #tk.Button(self, text="QUIT", fg="red",
							command=root.destroy)
		self.quit.pack(side="bottom")

	def say_hi(self):
		print("hi there, everyone!")

root = Tk()#tk.Tk()

# Set the root window dimensions
root.geometry('{}x{}'.format(400, 300)) 

# Call app with the root window as the master
app = Application(master=root)

# app has mainloop method inherited from Frame base class
app.mainloop()