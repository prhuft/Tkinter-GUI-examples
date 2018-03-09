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

# the default dimensions of the root window
w = 300
root.geometry('{}x{}'.format(int(w*1.618),w))

# the text to be displayed is mutable
text = StringVar()

# the widget to display the text, with field width of 80 chars
label = Message(root,textvariable=text)

# default text value
text.set("Oy! Hello from the matrix!")

# packs the label onto the root window at the top center, unless a positional
# argument is specified
label.pack(anchor = 'nw')

# essentially, while(true): update the window
root.mainloop()