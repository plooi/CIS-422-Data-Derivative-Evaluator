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
import gui_bootstrap as gb
from constants import GUI

class OutletSelection(Frame):


    def __init__(self, root):
        Frame.__init__(self, root)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.title = Label(self, text='Location: ').grid(row=0, column=0, sticky='nw')

        self.outletVariable = StringVar()
        self.outletFilter = Entry(self, textvariable=self.outletVariable)
        self.outletFilter.bind('<Return>', self._search_callback)
        self.outletFilter.grid(row=0, column=1, sticky='ew')

        # Buttons
        self.searchButton = Button(self, text="Search", command=self._search_callback)
        self.searchButton.grid(row=0, column=2, sticky='nwe', padx=15)

        # Listbox frame and scrollbars parent
        self.results = Frame(self)
        self.results.rowconfigure(0, weight=1)
        self.results.columnconfigure(0, weight=1)
        self.results.grid(row=1, column=0, columnspan=3, sticky='nsew')

        # Listbox with search results
        self.outlets = Listbox(self.results, height=20, width=30)
        self.outlets.grid(row=0, column=0, columnspan=2, sticky='nsew')
        self.outlets.bind('<<ListboxSelect>>', self._select_callback)

        # Y scrollbar
        self.yscrollbar = Scrollbar(self.results, orient="vertical")
        self.yscrollbar.config(command=self.outlets.yview)
        self.yscrollbar.grid(row=0, column=2, sticky="ns")
        self.outlets.config(yscrollcommand=self.yscrollbar.set)

        # X scrollbar
        self.xscrollbar = Scrollbar(self.results, orient="horizontal")
        self.xscrollbar.config(command=self.outlets.xview)
        self.xscrollbar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.outlets.config(xscrollcommand=self.xscrollbar.set)

        self.locations = []

    def refresh(self):
        self._search_callback()

    def _select_callback(self, event):
        widget = event.widget
        selection = widget.curselection()
        code = self.locations[selection[0]].get_abbreviation()

        pInputs = gb.main_window.getComponent(GUI.projectionInputs)
        pInputs.setOutlet(code)

    def _search_callback(self, event=None):
        self.outlets.delete(0, END)

        t = str(self.outletVariable.get())
        self.locations = location.search_locations(t)

        for loc in self.locations:
            self.outlets.insert(END, loc)

