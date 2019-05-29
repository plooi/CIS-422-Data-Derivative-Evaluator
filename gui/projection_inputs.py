'''
Projections Inputs
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter.constants import TOP, LEFT
from tkinter import Frame, StringVar, OptionMenu

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

class ProjectionInputs(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        topMenus = Frame(self)
        topMenus.pack(side=TOP, fill='x', expand=False)

        rcpVar = StringVar(self)
        rcpVar.set(RCP[0])
        rcp = OptionMenu(self, rcpVar, *RCP)
        rcp.pack(side=LEFT)

        gcmVar = StringVar(self)
        gcmVar.set(GCM[0])
        gcm = OptionMenu(self, gcmVar, *GCM)
        gcm.pack(side=LEFT)

        mdmVar = StringVar(self)
        mdmVar.set(MDM[0])
        mdm = OptionMenu(self, mdmVar, *MDM)
        mdm.pack(side=LEFT)

        hmsVar = StringVar(self)
        hmsVar.set(HMS[0])
        hms = OptionMenu(self, hmsVar, *HMS)
        hms.pack(side=LEFT)