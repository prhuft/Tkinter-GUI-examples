"""
File open example with Tkinter widgets. Opens the File Explorer select file
dialog upon clicking a button, then displays the selected filename in a 
Message widget. 
"""

## Libraries

from tkinter import filedialog
from tkinter import *

## Functions

def fopen(window):
	window.filename =  filedialog.askopenfilename(initialdir = "\C:Users\Preston Huft\Documents",title = 
	"Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	print("well, its working...")

## Main code

root = Tk()
root.geometry('{}x{}'.format(400, 300))

# declare and initialize string variables
flabel = StringVar()
fname = StringVar()
flabel = "File: "
fname = "No file selected yet"

# add a Label
flabel = Label(root,textvariable=flabel).grid(row=0,column=0)

# add a Message box to display the filename
fmsg = Message(root,textvariable=fname,fg='red').grid(row=0,column=1)

# add a button to launch the file opener
fbutton = Button(root, text="Select file",fg="blue",command=fopen(root)).grid(row=0,column=2)

# set the fname
#fname.set(root.filename)

# show/continuously update the window
root.mainloop()