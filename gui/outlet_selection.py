'''
Outlet Selection
Class definition

Author:
Brian Truong,
Edward Cho
'''

import tkinter as tk

from tkinter.constants import RIGHT, END
from tkinter import Frame, Listbox, Entry, Label, Button, StringVar, Scrollbar, Canvas
import Locations as location

class OutletSelection(Frame):


    def __init__(self, root):
        Frame.__init__(self, root)
        self.rowconfigure(1, weight=1)
        self.title = Label(self, text='Location: ').grid(row=0, column=0, sticky='nw')

        self.outletVariable = StringVar()
        self.outletFilter = Entry(self, textvariable=self.outletVariable).grid(row=0, column=1, sticky='ew')

        ## buttons
        self.searchButton = Button(self, text="search!", command=self.search_callback)
        self.searchButton.grid(row=0, column=2, sticky='nw')

        self.results = Frame(self)
        self.results.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=10, pady=10)


        ## listbox
        self.outlets = Listbox(self.results, height=20, width=30)
        self.outlets.grid(row=0, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)
        self.search_callback()


        # y scrollbar
        self.yscrollbar = Scrollbar(self.results, orient="vertical")
        self.yscrollbar.config(command=self.outlets.yview)
        self.yscrollbar.grid(row=0, column=2, sticky="ns")
        self.outlets.config(yscrollcommand=self.yscrollbar.set)


        # x scrollbar
        self.xscrollbar = Scrollbar(self.results, orient="horizontal")
        self.xscrollbar.config(command=self.outlets.xview)
        self.xscrollbar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.outlets.config(xscrollcommand=self.xscrollbar.set)



    def search_callback(self):
        self.outlets.delete(0, END)

        t = str(self.outletVariable.get())
        locations = location.search_locations(t)

        for loc in locations:
            print(loc)
            self.outlets.insert(END, loc)



