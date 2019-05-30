'''
Main Window
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter.constants import BOTH, RIGHT, END, TOP, BOTTOM
from tkinter import Tk, Frame, Button, Listbox, Menu

from gui.outlet_selection import OutletSelection
from gui.file_porter_menu import FilePorterMenu
from gui.projections_list import ProjectionsList
from gui.projection_inputs import ProjectionInputs
from gui.plot_display import PlotDisplay

class MainWindow(Tk):
    def __init__(self, master=None):
        Tk.__init__(self)
        self.geometry("1024x576")
        self.init_window()

    def init_window(self):
        self.title("Hydroclimate Change Data Visualizer")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        self.oSelection = OutletSelection(self)
        self.oSelection.grid(row=0, column=0, rowspan=2, sticky='ns')

        self.fpMenu = FilePorterMenu(self)
        self.config(menu=self.fpMenu)

        self.pInputs = ProjectionInputs(self)
        self.pInputs.grid(row=0, column=1, sticky='w')

        self.pList = ProjectionsList(self)
        self.pList.grid(row=0, column=2, rowspan=2, sticky='ns')

        self.pDisp = PlotDisplay(self)
        self.pDisp.grid(row=1, column=1, sticky='nswe')