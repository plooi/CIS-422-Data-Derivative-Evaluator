'''
Main Window
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter.constants import BOTH, RIGHT, END, TOP, BOTTOM
from tkinter import Tk, Frame, Button, Listbox, Menu

from gui.projections_list import ProjectionsList
from gui.projection_inputs import ProjectionInputs
from gui.plot_display import PlotDisplay
from gui.file_porter_menu import FilePorterMenu

class MainWindow(Tk):
    def __init__(self, master=None):
        Tk.__init__(self)
        self.geometry("1024x576")
        self.init_window()

    def init_window(self):

        self.title("Hydroclimate-Change-Data-Visualizer")

        self.pInputs = ProjectionInputs(self)
        self.pInputs.grid(row=0, column=0)

        self.pList = ProjectionsList(self)
        self.pList.grid(row=0, column=1, rowspan=2)

        self.pDisp = PlotDisplay(self)
        self.pDisp.grid(row=1, column=0)

        self.menus = FilePorterMenu(self)