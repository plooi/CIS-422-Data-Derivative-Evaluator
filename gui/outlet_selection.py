'''
Outlet Selection
Class definition

Author:
Brian Truong
'''

from tkinter.constants import RIGHT, END
from tkinter import Frame, Listbox, Entry, Label

class OutletSelection(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.rowconfigure(1, weight=1)

        Label(text='Filter: ').grid(row=0, column=0, sticky='nw')
        outletFilter = Entry(self)
        outletFilter.grid(row=0, column=1, sticky='ew')

        outlets = Listbox(self, width=30)
        outlets.grid(row=1, column=0, columnspan=2, sticky='ns')
        outlets.insert(END, "CODE1 Location description 1")
        outlets.insert(END, "CODE2 Description of location 2")
        outlets.insert(END, "CODE3 Location description 3")