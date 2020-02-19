import tkinter as tk
from tkinter.colorchooser import *

root = tk.Tk()

root.title('Color Swatch')
root.minsize(width=450, height=600)

def clr_clicked():
    color = askcolor()
    print(color)
    b_show.configure(bg = color[1],fg = color[1])

def reset_clr() :
    b_show.configure(bg = 'White', text = 'Text Sample')

label1 = tk.Label(root, text = 'Tools')
label1.grid(row = 2, column = 1)

label2 = tk.Label(root, text = 'Text Editor')
label2.grid(row = 1, column = 4)

text_area = tk.Text(root, height = 6)
text_area.grid(row = 3, column = 2, rowspan = 3, columnspan = 5, sticky='S')

b_clr = tk.Button(root, text = "Color", command = clr_clicked, bg="black", fg="purple")
b_clr.grid(row = 2, column = 3)


b_show = tk.Button(root,text = ':)   :)    :)', fg = 'white', command = reset_clr)
b_show.grid(row = 2, column = 5)

root.mainloop()