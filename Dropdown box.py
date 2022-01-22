import tkinter
import tkinter as ttk
from tkinter import *
 
root = tkinter.Tk()
root.title("Dropdown box example")
 
mainframe = tkinter.Frame(root)
mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)
 
tkvar = tkinter.StringVar(root)
 
choices = { 'Python','C','C++','PHP','JAVA'}
tkvar.set('Python') 
 
popupMenu = tkinter.OptionMenu(mainframe, tkvar, *choices)
tkinter.Label(mainframe, text="Choose Programming Language").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)
 
def change_dropdown(*args):
    print( tkvar.get() )
 
tkvar.trace('w', change_dropdown)
 
root.mainloop()
