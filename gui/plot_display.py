'''
Plot Display
Class definition

Author:
Ben Lain
Brian Truong
'''

import matplotlib
from Projection import active_projections
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

from tkinter.constants import TOP, BOTH
from tkinter import Frame, Listbox, StringVar, OptionMenu
import plot

class PlotDisplay(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

    def update(self):
        for child in self.winfo_children():
            child.destroy()

        f = plot.create_figure()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
