'''
Projections Inputs
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter.constants import TOP, LEFT, RIGHT
from tkinter import Frame, StringVar, OptionMenu, Button, messagebox, Label

from constants import GUI
import gui_bootstrap as gb
import plot

# Test constants
MAX = [
    "MAX",
    "MEAN",
]

colors = [
    'Red',
    'Blue',
    'Green',
    'Yellow',
    'Orange',
    'Violet',
    'Black',
    'Brown',
    'Grey',
    'Turquoise'
]


class ProjectionInputs(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

    def create(self, rcp, gcm, mdm, hms):
        '''Creates the inputs, given the parameter lists'''
        for child in self.winfo_children():
            child.destroy()

        Label(self, text='Outlet: ').pack(side=LEFT)
        self.outVar = StringVar(self)
        self.outVar.set('None Selected')
        self.out = Label(self, textvariable=self.outVar).pack(side=LEFT)

        self.rcpVar = StringVar(self)
        self.rcpVar.set(rcp[0])
        rcp = OptionMenu(self, self.rcpVar, *rcp)
        rcp.pack(side=LEFT)

        self.gcmVar = StringVar(self)
        self.gcmVar.set(gcm[0])
        gcm = OptionMenu(self, self.gcmVar, *gcm)
        gcm.pack(side=LEFT)

        self.mdmVar = StringVar(self)
        self.mdmVar.set(mdm[0])
        mdm = OptionMenu(self, self.mdmVar, *mdm)
        mdm.pack(side=LEFT)

        self.hmsVar = StringVar(self)
        self.hmsVar.set(hms[0])
        hms = OptionMenu(self, self.hmsVar, *hms)
        hms.pack(side=LEFT)

        self.maxVar = StringVar(self)
        self.maxVar.set(MAX[0])
        Max = OptionMenu(self, self.maxVar, *MAX)
        Max.pack(side=LEFT)

        self.colorVar = StringVar(self)
        self.colorVar.set(colors[0])
        color = OptionMenu(self, self.colorVar, *colors)
        color.pack(side=LEFT)

        PlotButton = Button(self, text="Plot", command=self.add)
        PlotButton.pack(side=RIGHT)

    def setOutlet(self, outlet: str):
        '''Sets the outlet from which to create the projection'''
        self.outVar.set(outlet)

    def add(self):
        MaxBool = (self.maxVar.get() == 'MAX')
        try:
            f = plot.add_projection(
            self.outVar.get(),
            self.gcmVar.get(),
            self.mdmVar.get(),
            self.rcpVar.get(),
            self.hmsVar.get(),
            self.colorVar.get(),
            MaxBool
            )
        except:
            messagebox.showinfo("Error Message", "One of your location, RCP, GCM, MDM, or HMS selections was invalid")

        pDisp = gb.main_window.getComponent(GUI.plotDisplay)
        pDisp.update()

        pList = gb.main_window.getComponent(GUI.projectionsList)
        pList.update()
