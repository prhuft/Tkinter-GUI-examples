"""
Tkinter GUI text display example. Prints a non-editable string in a Message
widget. See https://www.tutorialspoint.com/python/tk_message.htm for more
info on this widget. 
"""

## Libraries

from tkinter import *

## Main code

# the main graphical window
root = Tk()

# the text to be displayed is mutable
text = StringVar()

# the widget to display the text, with field width of 80 chars
label = Message(root,textvariable=text)

# default text value
text.set("Oy! Hello from the matrix!")

# fills the Message widget with the text
label.pack()

# while(true): update the window
root.mainloop()