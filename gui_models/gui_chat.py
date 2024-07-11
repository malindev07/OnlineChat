from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x150")

message = StringVar()

label = ttk.Label(textvariable = message)
label.pack(anchor = NW, padx = 6, pady = 6)

entry = ttk.Entry(textvariable = message)
entry.pack(anchor = NW, padx = 6, pady = 6)

button = ttk.Button(textvariable = message)
button.pack(side = LEFT, anchor = N, padx = 6, pady = 6)

root.mainloop()

##rest
