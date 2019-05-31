'''
Outlet Selection
Class definition

Author:
Brian Truong, Edward Cho
'''

import tkinter as tk

from tkinter.constants import RIGHT, END
from tkinter import Frame, Listbox, Entry, Label, Button, StringVar
import Locations as location

class OutletSelection(Frame):


    def __init__(self, root):
        Frame.__init__(self, root)
        self.rowconfigure(1, weight=1)

        self.title = Label(text='Location: ').grid(row=0, column=0, sticky='nw')

        self.outletVariable = StringVar()
        self.outletFilter = Entry(textvariable=self.outletVariable).grid(row=0, column=1, sticky='ew')


        ## buttons
        self.searchButton = Button(text="search!", command=self.search_callback)
        self.searchButton.grid(row=1, column=1,columnspan=2, sticky='nw')


        ## listbox
        self.outlets = Listbox()#, width=30)
        self.outlets.grid(row=2, column=0, columnspan=2, sticky='s', padx=10, pady=10)


    def search_callback(self):
        self.outlets.delete(0, END)


        t = str(self.outletVariable.get())
        locations = location.search_locations(t)

        for loc in locations:
            print(loc)
            self.outlets.insert(END, loc)



# r = tk.Tk()
# s = OutletSelection(r)
# s.mainloop()
