'''
Projections Inputs
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter.constants import TOP, LEFT, RIGHT
from tkinter import Frame, StringVar, OptionMenu, Button, messagebox, Label

from gui.constants import GUI
import gui.bootstrap as gb
import data_processing.plot as plot

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
        self.outVar = StringVar(self)
        self.rcpVar = StringVar(self)
        self.gcmVar = StringVar(self)
        self.mdmVar = StringVar(self)
        self.hmsVar = StringVar(self)
        self.maxVar = StringVar(self)
        self.colorVar = StringVar(self)

    def create(self, rcp, gcm, mdm, hms):
        '''Creates the inputs, given the parameter lists'''
        for child in self.winfo_children():
            child.destroy()

        ### Selected outlet

        outFrame = Frame(self)
        outFrame.grid(row=0, column=0, sticky='w')
        Label(outFrame, text='Outlet: ').grid(row=0, column=0)

        self.outVar.set('None Selected')
        Label(outFrame, textvariable=self.outVar).grid(row=0, column=1)


        ### Dropdowns

        dropdowns = Frame(self)
        dropdowns.grid(row=1, column=0, sticky='w')

        self.rcpVar.set(rcp[0])
        rcp = OptionMenu(dropdowns, self.rcpVar, *rcp)
        rcp.grid(row=1, column=0)

        self.gcmVar.set(gcm[0])
        gcm = OptionMenu(dropdowns, self.gcmVar, *gcm)
        gcm.grid(row=1, column=1)

        self.mdmVar.set(mdm[0])
        mdm = OptionMenu(dropdowns, self.mdmVar, *mdm)
        mdm.grid(row=1, column=2)

        self.hmsVar.set(hms[0])
        hms = OptionMenu(dropdowns, self.hmsVar, *hms)
        hms.grid(row=1, column=3)

        self.maxVar.set(MAX[0])
        mx = OptionMenu(dropdowns, self.maxVar, *MAX)
        mx.grid(row=1, column=4)

        self.colorVar.set(colors[0])
        color = OptionMenu(dropdowns, self.colorVar, *colors)
        color.grid(row=1, column=5)

        ### Plot button

        pButton = Button(self, text="Plot", command=self.add)
        pButton.grid(row=1, column=1, sticky='e')

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
        except Exception as e:
            messagebox.showwarning(
                "Parameter Error",
                "One of your selections was invalid:\n" + str(e)
            )

        pDisp = gb.main_window.getComponent(GUI.plotDisplay)
        pDisp.update()

        pList = gb.main_window.getComponent(GUI.projectionsList)
        pList.update()
