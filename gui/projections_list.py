'''
Projections List
Class definitions

Author:
Brian Truong
'''

from tkinter.constants import RIGHT, END
from tkinter import Frame, Scrollbar, Canvas, Label, Button, Checkbutton, IntVar

from Projection import Projection, active_projections
from constants import GUI, FONT_SMALL

import gui_bootstrap as gb

# Class definition for the main Projections List component
# Scrolling implementation from: https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame
class ProjectionsList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.root = root
        self.rowconfigure(0, weight=1)

        self.yScroll = Scrollbar(self)
        self.yScroll.grid(row=0, column = 1, sticky = 'ns')

        self.view = Canvas(self)
        self.view.config(relief = 'flat', width = 160, bd = 2)

        self.view.grid(row=0, column = 0, sticky = 'nsew')

        self.yScroll.config(command = self.view.yview)

        self.list = Frame(self)

        self.view.create_window(0, 0, window = self.list, anchor = 'nw')
        self.view.config(yscrollcommand = self.yScroll.set, scrollregion = (0, 0, 100, 100))

        self.yScroll.lift(self.list)
        self.list.bind('<Configure>', self._configure)
        self.list.bind('<Enter>', self._wheel_bind)
        self.list.bind('<Leave>', self._wheel_unbind)

    def update(self):
        for child in self.list.winfo_children():
            child.destroy()
        for p in active_projections:
            PListItem(self.list, p).pack(pady=(0, 8))

    def _configure(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.list.winfo_reqwidth(), self.list.winfo_reqheight())
        self.view.config(scrollregion='0 0 %s %s' % size)

        # update the canvas's width to fit the inner frame
        if self.list.winfo_reqwidth() != self.view.winfo_width():
            self.view.config(width = self.list.winfo_reqwidth())

    def _wheel_bind(self, event):
        self.view.bind_all("<MouseWheel>", self._wheel)

    def _wheel_unbind(self, event):
        self.view.unbind_all("<MouseWheel>") 

    def _wheel(self, event):
        self.view.yview_scroll(int(-1*(event.delta/120)), "units")

# Class definition for the items listed by the Projections List component
class PListItem(Frame):
    def __init__(self, root, projection: Projection):
        Frame.__init__(self, root)

        self.proj = projection
        self.config(
            highlightbackground=self.proj.get_color(),
            highlightcolor=self.proj.get_color(),
            highlightthickness=2,
            bd=0
        )

        # Label that specifies the location
        # TODO Location not specified!
        Label(self,
            text=self.proj.get_location()
        ).grid(row=0, column=0, sticky='w')
        
        # Checkbox that toggles visibility
        self.visibility = IntVar(self)
        self.visibility.set(1)
        Checkbutton(self, 
            variable=self.visibility, command=self.toggle
        ).grid(row=0, column=1, sticky='w')

        # Describes the projection parameters
        self.params = Frame(self)
        rows = ['RCP', 'GCM', 'MDM', 'HMS']
        for i in range(len(rows)):
            Label(self.params, text=rows[i] + ':', font=FONT_SMALL
                ).grid(row=i, column=0, sticky='w')
            Label(self.params, text=self.proj[rows[i]], font=FONT_SMALL
                ).grid(row=i, column=1, sticky='w')
        # Special case for the MAX
        Label(self.params, text='MAX:', font=FONT_SMALL
            ).grid(row=len(rows), column=0, sticky='w')
        Label(self.params, text=str(self.proj.get_max()), font=FONT_SMALL
            ).grid(row=len(rows), column=1, sticky='w')
        self.params.grid(row=1, column=0, columnspan=2, sticky='w')

        # Button to remove the projection
        Button(self,
            text='✕', command=self.remove
        ).grid(row=0, column=2, rowspan=2, sticky='ne', padx=(5, 0))

    def remove(self):
        # TODO Remove function not funcitoning as expected
        self.proj.remove()

        pDisp = gb.main_window.getComponent(GUI.plotDisplay)
        pDisp.update()

        pList = gb.main_window.getComponent(GUI.projectionsList)
        pList.update()

        return

    def toggle(self):
        self.proj.set_visibility(self.visibility.get())

        pDisp = gb.main_window.getComponent(GUI.plotDisplay)
        pDisp.update()
