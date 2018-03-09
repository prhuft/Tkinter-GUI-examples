# Code to open the file explorer file open dialog

# Libraries
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "\C:Users\Preston Huft\Documents",title = 
"Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
print (root.filename)
