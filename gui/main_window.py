'''
Main Window
Class definition

Author:
Ben Lain
Brian Truong
'''

from typing import Union

from tkinter.constants import BOTH, RIGHT, END, TOP, BOTTOM
from tkinter import Tk, Frame, Button, Listbox, Menu

from gui.outlet_selection import OutletSelection
from gui.file_porter_menu import FilePorterMenu
from gui.projections_list import ProjectionsList
from gui.projection_inputs import ProjectionInputs
from gui.plot_display import PlotDisplay
from constants import GUI

# Main window class definition
class MainWindow(Tk):
    def __init__(self, master=None):
        Tk.__init__(self)
        self.geometry("1024x576")
        self._init_window()

    # Initialize the main window and its child components
    def _init_window(self):
        self.title("Hydroclimate Change Data Visualizer")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        # self.oSelection = OutletSelection(self)
        # self.oSelection.grid(row=0, column=0, rowspan=2, sticky='ns')

        self.fpMenu = FilePorterMenu(self)
        self.config(menu=self.fpMenu)

        self.pInputs = ProjectionInputs(self)
        self.pInputs.grid(row=0, column=1, columnspan=2, sticky='w')

        # self.pList = ProjectionsList(self)
        # self.pList.grid(row=1, column=2, sticky='ns')

        self.pDisp = PlotDisplay(self)
        self.pDisp.grid(row=1, column=1, sticky='nswe')

    # Get a component currently maintained in the GUI
    def getComponent(self, component: GUI
        ) -> Union[OutletSelection,
                   FilePorterMenu,
                   ProjectionInputs,
                   ProjectionsList,
                   PlotDisplay,
                   None]:
        if component == GUI.outletSelection:
            return self.oSelection
        elif component == GUI.filePorterMenu:
            return self.fpMenu
        elif component == GUI.projectionInputs:
            return self.pInputs
        elif component == GUI.projectionsList:
            return self.pList
        elif component == GUI.plotDisplay:
            return self.pDisp
        else:
            return None