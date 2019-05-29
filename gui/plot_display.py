'''
Plot Display
Class definition

Author:
Ben Lain
Brian Truong
'''

import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

from tkinter.constants import TOP, BOTH
from tkinter import Frame, Listbox, StringVar, OptionMenu

class PlotDisplay(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)
        # canvas.get_tk_widget().grid(stick=S)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        # canvas._tkcanvas.grid(sticky=S, expand=True)