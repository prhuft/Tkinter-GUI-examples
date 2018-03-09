"""
Experimenting with GUI layouts using the tkinter library. 
"""

## Libraries
from tkinter import *

## Main code

# the root window
root = Tk()
w = 300

# set the default windown dimensions 
root.geometry('{}x{}'.format(int(w*1.618),w))

leftframe = Frame(root)
leftframe.pack(side=LEFT)

button1 = Button(leftframe,text="Button 1")
button1.pack(side=TOP)

button2 = Button(leftframe,text="Button 2")
button2.pack(side=TOP)

root.mainloop()