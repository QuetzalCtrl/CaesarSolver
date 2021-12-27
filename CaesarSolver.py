from tkinter import * 
from tkinter.filedialog import *
from tkinter import ttk

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'

def encode():
    result = ""
    currentShift = (int)(shift.get())
    text = plaintext.get(1.0,"end")
    for i in range(len(text)):
        char = text[i]
        if char in UPPER:
            result += UPPER[(UPPER.find(char)+currentShift)%26]
        elif char in LOWER:
            result += LOWER[(LOWER.find(char)+currentShift)%26]
        else:
            result += char
    encoded.delete(1.0,"end")
    encoded.insert(1.0, result)

def decode():
    result = ""
    currentShift = (int)(shift.get())
    text = encoded.get(1.0,"end")
    for i in range(len(text)):
        char = text[i]
        if char in UPPER:
            result += UPPER[(UPPER.find(char)-currentShift)%26]
        elif char in LOWER:
            result += LOWER[(LOWER.find(char)-currentShift)%26]
        else:
            result += char
    plaintext.delete(1.0,"end")
    plaintext.insert(1.0, result)

root = Tk()
root.title("Caesar Solver")
root.geometry("1200x800")

label = Label(root, text="Caesar Cipher Python Text Encoder and Decoder by QuetzalCoatl") 
label.pack(pady=5)

# create the main sections of the layout, 
# and lay them out
top = Frame(root, padx=25, pady=25)
top.pack(side=TOP, fill=BOTH, expand=True)
plabel = Label (root, text="Plain Text")
plabel.pack(in_=top, side=TOP, anchor=NW)
plaintext = Text(root, width=35, height=12)
scrollbar2 = Scrollbar(root)
scrollbar2.config(command=plaintext.yview)
plaintext.config(yscrollcommand=scrollbar2.set)
scrollbar2.pack(in_=top, side=RIGHT, fill=Y)
plaintext.pack(in_=top, side=LEFT, fill=BOTH, expand=True)

shiftFrame = Frame(root)
shiftFrame.pack(pady=15)
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
slabel = Label(root, text="shift : ") 
slabel.pack(in_=shiftFrame)
shift = ttk.Combobox(root, values = list)
shift.current(0)
shift.pack(in_=shiftFrame)

buttons = Frame(root)
buttons.pack()
b = Button(root, text="Encode", width=10, height=2, command=encode)
c = Button(root, text="Decode", width=10, height=2, command=decode)
b.pack(in_=buttons, side=LEFT)
c.pack(in_=buttons, side=LEFT)


bottom = Frame(root, padx=25, pady=25)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
elabel = Label (root, text="Cipher Text")
elabel.pack(in_=bottom, side=TOP, anchor=NW)
encoded = Text(root, width=35, height=12)
scrollbar = Scrollbar(root)
scrollbar.config(command=encoded.yview)
encoded.config(yscrollcommand=scrollbar.set)
scrollbar.pack(in_=bottom, side=RIGHT, fill=Y)
encoded.pack(in_=bottom, side=LEFT, fill=BOTH, expand=True)

root.mainloop()