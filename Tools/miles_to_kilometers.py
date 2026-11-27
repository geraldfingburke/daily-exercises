from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(miles.get())
        kilometers.set(round(1.60934 * value, 4))
    except ValueError:
        pass
root = Tk()
root.title("Miles to Kilometers")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

miles = StringVar()
miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)
miles_entry.grid(column=2, row=1, sticky=(W, E))

kilometers = StringVar()
ttk.Label(mainframe, textvariable=kilometers).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="miles").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="kilometers").grid(column=3, row=2, sticky=W)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

miles_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()