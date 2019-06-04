'''
Outlet Selection
Class definition

Component that allows user to choose which outlet
from which to create a projection

Author:
Brian Truong
Edward Cho
'''

import tkinter as tk

from tkinter.constants import RIGHT, END
from tkinter import Frame, Listbox, Entry, Label, Button, StringVar, Scrollbar, Canvas, IntVar, Checkbutton

import data_processing.Locations as location
import gui.bootstrap as gb
from gui.constants import GUI, FONT_BOLD

class OutletSelection(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        ## Search bar

        search = Frame(self)
        search.grid(row=0, column=0, columnspan=2, padx=8)

        self.title = Label(search, text='Location: ').grid(row=0, column=0)

        self.outletVariable = StringVar(self)
        self.outletFilter = Entry(search, textvariable=self.outletVariable)
        self.outletFilter.grid(row=0, column=1, pady=10)
        self.outletFilter.bind('<Return>', lambda e: self._search_callback())

        self.searchButton = Button(search, text="Search", command=self._search_callback)
        self.searchButton.grid(row=0, column=2, padx=(8, 0))

        ## Results list

        # Listbox with search results
        self.outlets = Listbox(self, height=20, width=30)
        self.outlets.grid(row=1, column=0, sticky='nsew')
        self.outlets.bind('<<ListboxSelect>>', self._select_callback)

        # Y scrollbar
        self.yscrollbar = Scrollbar(self, orient="vertical")
        self.yscrollbar.config(command=self.outlets.yview)
        self.yscrollbar.grid(row=1, column=1, sticky="ns")
        self.outlets.config(yscrollcommand=self.yscrollbar.set)

        # X scrollbar
        self.xscrollbar = Scrollbar(self, orient="horizontal")
        self.xscrollbar.config(command=self.outlets.xview)
        self.xscrollbar.grid(row=2, column=0, sticky="ew")
        self.outlets.config(xscrollcommand=self.xscrollbar.set)

        self.locations = []

        ## Option to filter invalid locations

        toggle = Frame(self)
        toggle.grid(row=3, column=0, sticky='w')

        Label(toggle, text='Hide invalid locations').grid(row=0, column=0)

        self.filterInvalid = IntVar(self)
        self.filterInvalid.set(0)
        Checkbutton(toggle,
            variable=self.filterInvalid, command=self._search_callback
        ).grid(row=0, column=1, sticky='w')

        self.refresh()

    def refresh(self):
        '''Refresh the search content'''
        self.outletVariable.set('')
        self._search_callback()

    def _select_callback(self, event):
        '''Select the outlet to be used for creating a projection'''
        if len(self.locations) == 0:
            return

        widget = event.widget
        selection = widget.curselection()
        location = self.locations[selection[0]]

        pInputs = gb.main_window.getComponent(GUI.projectionInputs)
        pInputs.setOutlet(location.get_abbreviation())

    def _search_callback(self):
        '''Get and display the relevant search results'''
        self.outlets.delete(0, END)

        t = str(self.outletVariable.get())
        self.locations = location.search_locations(t)

        if self.filterInvalid.get():
            rm = []
            for loc in self.locations:
                if not loc.get_valid():
                    rm.append(loc)
            for loc in rm:
                self.locations.remove(loc)

        for i in range(len(self.locations)):
            loc = self.locations[i]
            self.outlets.insert(END, loc)
            if not loc.get_valid():
                self.outlets.itemconfig(i, selectbackground='grey80', selectforeground='grey', fg='grey80')
