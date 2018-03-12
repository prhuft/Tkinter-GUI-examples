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

## Method 1: using the 'grid' layout manager

# declare variable strings
defaulttext="default text"
text1 = StringVar()
text1.set(defaulttext)
text2 = StringVar()
text2.set(defaulttext)

label1 = Label(root,text="Text 1:").grid(row=0,column=0)
label2 = Label(root,text="Text 2:").grid(row=1,column=0)

entry1 = Entry(root,textvariable=text1,width=30).grid(row=0,column=1)
entry2 = Entry(root,textvariable=text2,width=30).grid(row=1,column=1)

button1 = Button(root,text="Button 1").grid(row=0,column=2)
button2 = Button(root,text="Button 2").grid(row=1,column=2)

## Method 2: using the 'pack' layout manager
# create two frames, stacking downward from the top
# topframe1 = Frame(root)
# topframe1.pack(side=TOP,anchor='nw')

# topframe2 = Frame(root)
# topframe2.pack(side=TOP,anchor='nw')

# populate each frame with two labels and a button
# label1 = Label(topframe1,text="Text 1:")
# label1.pack(side=LEFT)

# label2 = Label(topframe2,text="Text 2:")
# label2.pack(side=LEFT)

# txt1 = Message(topframe1,text="The first text!")
# txt1.pack(side=LEFT)

# txt2 = Message(topframe2,text="The second text!")
# txt2.pack(side=LEFT)

# button1 = Button(topframe1,text="Button 1",)
# button1.pack(side=LEFT)

# button2 = Button(topframe2,text="Button 2")
# button2.pack(side=LEFT)

root.mainloop()