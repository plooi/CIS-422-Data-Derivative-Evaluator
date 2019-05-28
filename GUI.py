import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure
matplotlib.use("TkAgg")

# Made by Benjamin Lain
# Used the information on this page as a guideline
# https://pythonprogramming.net/tkinter-python-3-tutorial-adding-buttons/?completed=/python-3-tkinter-basics-tutorial/

LARGE_FONT = ("Verdana", 12)


class GraphFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph here", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class DropDowns(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        RCP = [
            "RCP 4.5",
            "RCP 8.5"
                ]
        variable = tk.StringVar(self.master)
        rcp = tk.OptionMenu(self.master, variable, *RCP)
        # rcp.pack(anchor=tk.N, side=tk.TOP, fill=tk.BOTH)
        rcp.grid(sticky=tk.N)


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Hydroclimate-Change-Data-Visualizer")

        locationlist = tk.Listbox(self)
        locationlist.pack(side=tk.RIGHT, fill=tk.Y)
        locationlist.insert(tk.END, "Test location 1")
        locationlist.insert(tk.END, "Test location 2")

        self.build_dropdowns()
        # This section defines and builds the graph

        # container = tk.Frame(self)
        # container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weigh=1)

        # graph = GraphFrame(self)
        # graph.grid(row=0, column=1)
        self.pack(fill=tk.BOTH, expand=1)
        self.graph()

        # This section is for buttons and drop down menus
        self.build_menus()

    def graph(self):
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # canvas.get_tk_widget().grid(stick=tk.S)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # canvas._tkcanvas.grid(sticky=tk.S, expand=True)

    def build_menus(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        file = tk.Menu(menu)

        file.add_command(label="Exit", command=self.client_exit)
        file.add_command(label="Import")
        file.add_command(label="Export")

        menu.add_cascade(label="File", menu=file)

    def build_dropdowns(self):

        # self.dropDown = DropDowns(self)
        # self.dropDown.grid(row=0)
        topMenus = tk.Frame(self)
        topMenus.pack(side=tk.TOP, fill=tk.X, expand=False)

        RCP = [
             "RCP 4.5",
             "RCP 8.5"
                ]
        GCM = [
            "CanESM2",
            "CCSM4",
            "CNRM-CM5",
            "CSIRO-Mk3-6-0",
            "GFDL-ESM2M",
            "HadGEM2-ES",
            "Inmcm4",
            "IPSL-CM5A-MR"
            "MIROCS"
                ]
        MDM = [
            "BCSD",
            "MACA",
                ]
        HMS = [
            "PRMS",
            "VIC P1",
            "VIC P2",
            "VIC P3",
                ]
        rcpVar = tk.StringVar(self.master)
        rcpVar.set(RCP[0])
        rcp = tk.OptionMenu(self.master, rcpVar, *RCP)
        rcp.pack(in_=topMenus, side=tk.LEFT)

        gcmVar = tk.StringVar(self.master)
        gcmVar.set(GCM[0])
        gcm = tk.OptionMenu(self.master, gcmVar, *GCM)
        gcm.pack(in_=topMenus, side=tk.LEFT)

        mdmVar = tk.StringVar(self.master)
        mdmVar.set(MDM[0])
        mdm = tk.OptionMenu(self.master, mdmVar, *MDM)
        mdm.pack(in_=topMenus, side=tk.LEFT)

        hmsVar = tk.StringVar(self.master)
        hmsVar.set(HMS[0])
        hms = tk.OptionMenu(self.master, hmsVar, *HMS)
        hms.pack(in_=topMenus, side=tk.LEFT)

    def client_exit(self):
        exit()


root = tk.Tk()
root.geometry("1024x576")
app = Window(root)
root.mainloop()
