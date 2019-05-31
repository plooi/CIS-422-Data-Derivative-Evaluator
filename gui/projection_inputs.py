'''
Projections Inputs
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter.constants import TOP, LEFT, RIGHT
from tkinter import Frame, StringVar, OptionMenu, Button
import plot
from gui.main_window import GUI

# Test constants
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
    "IPSL-CM5A-MR",
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
MAX = [
    "MAX",
    "MED",
    "MIN"
        ]


class ProjectionInputs(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.main_window = root

        topMenus = Frame(self)
        topMenus.pack(side=TOP, fill='x', expand=False)

        self.rcpVar = StringVar(self)
        self.rcpVar.set(RCP[0])
        rcp = OptionMenu(self, self.rcpVar, *RCP)
        rcp.pack(side=LEFT)

        self.gcmVar = StringVar(self)
        self.gcmVar.set(GCM[0])
        gcm = OptionMenu(self, self.gcmVar, *GCM)
        gcm.pack(side=LEFT)

        self.mdmVar = StringVar(self)
        self.mdmVar.set(MDM[0])
        mdm = OptionMenu(self, self.mdmVar, *MDM)
        mdm.pack(side=LEFT)

        self.hmsVar = StringVar(self)
        self.hmsVar.set(HMS[0])
        hms = OptionMenu(self, self.hmsVar, *HMS)
        hms.pack(side=LEFT)

        self.maxVar = StringVar(self)
        self.maxVar.set(MAX[0])
        Max = OptionMenu(self, self.maxVar, *MAX)
        Max.pack(side=LEFT)

        PlotButton = Button(self, text="Plot", command=self.add)
        PlotButton.pack(side=RIGHT)

    def add(self):
        # def plot_button(gcm, mdm, rcp, hms, max):
        f = plot.plot_button(
            self.gcmVar.get(),
            self.mdmVar.get(),
            self.rcpVar.get(),
            self.hmsVar.get(),
            self.maxVar.get()
        )

        pDisp = self.main_window.getComponent(GUI.plotDisplay)
        pDisp.plot(f)
