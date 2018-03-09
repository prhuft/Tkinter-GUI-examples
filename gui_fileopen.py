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
	return window.filename

## Main code

root = Tk()
root.geometry('{}x{}'.format(400, 300))

# declare and set a string for the filename
fname = StringVar()
fname = "filename will go here"

# add a Message box
flabel = Message(root,textvariable=fname)
flabel.pack(anchor = 'nw')

# add a button to launch the file opener
fbutton = Button(root, text="Select file",fg="blue",command=fopen(root))
fbutton.pack()

# set the fname
fname.set(root.filename)

# show/continuously update the window
root.mainloop()