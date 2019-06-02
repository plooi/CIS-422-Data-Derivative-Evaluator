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
from tkinter import Frame, Listbox, StringVar, OptionMenu, filedialog, messagebox
import plot
from constants import OS_HOME_DIR

class PlotDisplay(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.update()

    def update(self):
        for child in self.winfo_children():
            child.destroy()

        f = plot.create_figure()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        toolbar = PlotToolbar(canvas, self)
        toolbar.update()

'''Overwrite Toolbar functions to fix errors'''
class PlotToolbar(NavigationToolbar2Tk):
    def __init__(self, canvas, window):
        NavigationToolbar2Tk.__init__(self, canvas, window)

    def save_figure(self, *args):
        '''Save function for it to work on Windows'''
        filetypes = self.canvas.get_supported_filetypes().copy()
        default_filetype = self.canvas.get_default_filetype()
        default_filetype_name = filetypes.pop(default_filetype)
        sorted_filetypes = ([(default_filetype, default_filetype_name)]
                            + sorted(filetypes.items()))
        tk_filetypes = [(name, '*.%s' % ext) for ext, name in sorted_filetypes]

        fname = filedialog.asksaveasfilename(
            title='Save the figure',
            initialdir=OS_HOME_DIR,
            initialfile=self.canvas.get_default_filename(),
            filetypes=tk_filetypes,
        )

        if fname in ["", ()]:
            return

        try:
            self.canvas.figure.savefig(fname)
        except Exception as e:
            messagebox.showerror("Error saving file", str(e))

    def set_cursor(self, cursor):
        '''Do nothing'''
        return
