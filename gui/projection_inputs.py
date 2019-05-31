'''
Projections Inputs
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter.constants import TOP, LEFT, RIGHT
from tkinter import Frame, StringVar, OptionMenu, Button

from constants import GUI
import gui_bootstrap as gb
import plot

# Test constants
RCP = [
    "RCP45",
    "RCP85"
]
GCM = [
    "HadGEM2-CC",
    "HadGEW2-ES",
    "CanESM2",
    "CNRM-CM5",
    "CSIRO-Mk3-6-0",
    "GFDL-ESM2M",
    "inmcm4",
    "MIROC5"
    "IPSL-CM5A-MR",
    "CCSM4"
]
MDM = [
    "bcsd",
    "maca",
]
HMS = [
    "PRMS",
    "calib_inverse",
    "ORNL",
    "NCAR"
]
MAX = [
    "MAX",
    "MEAN",
        ]


class ProjectionInputs(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

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
        MaxBool = (self.maxVar.get() == 'MAX')

        f = plot.add_projection(
            self.gcmVar.get(),
            self.mdmVar.get(),
            self.rcpVar.get(),
            self.hmsVar.get(),
            MaxBool
        )

        pDisp = gb.main_window.getComponent(GUI.plotDisplay)
        pDisp.update()

        pList = gb.main_window.getComponent(GUI.projectionsList)
        pList.update()
