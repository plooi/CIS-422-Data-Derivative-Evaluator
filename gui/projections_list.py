'''
Projections List
Class definitions

Component thta displays a list of created projections,
allowing for visibility toggling and removal

Scrolling implementation derived from:
https://stackoverflow.com/questions/16188420/tkinter-scrollbar-for-frame

Author:
Brian Truong
'''

from tkinter.constants import RIGHT, END
from tkinter import Frame, Scrollbar, Canvas, Label, Button, Checkbutton, IntVar

from data_processing.Projection import Projection
import data_processing.plot as plot

from gui.constants import GUI, FONT_SMALL
import gui.bootstrap as gb

class ProjectionsList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.rowconfigure(0, weight=1)

        # Scrollbar
        self.yScroll = Scrollbar(self)
        self.yScroll.grid(row=0, column = 1, sticky = 'ns')

        # The viewbox for the scrolling content
        self.view = Canvas(self)
        self.view.config(relief = 'flat', width = 160, bd = 2)
        self.view.grid(row=0, column = 0, sticky = 'nsew')

        # Bind scrolling to viewbox
        self.yScroll.config(command = self.view.yview)
        self.view.config(yscrollcommand = self.yScroll.set, scrollregion = (0, 0, 100, 100))

        # The list of items
        self.list = Frame(self)
        self.view.create_window(0, 0, window = self.list, anchor = 'nw')

        # Render scrollbar above the scrolling items
        self.yScroll.lift(self.list)

        # Bind dynamic events
        self.list.bind('<Configure>', self._configure)
        self.list.bind('<Enter>', self._wheel_bind)
        self.list.bind('<Leave>', self._wheel_unbind)

    def update(self):
        '''Updates the contents of the list to match the active projections'''

        for child in self.list.winfo_children():
            child.destroy()
        for p in plot.active_projections:
            PListItem(self.list, p).pack(pady=(0, 8), fill='x')

    def _configure(self, event):
        '''Callback to reconfigure the scroll box properties'''

        # Update the scrollbars to match the size of the inner frame
        size = (self.list.winfo_reqwidth(), self.list.winfo_reqheight())
        self.view.config(scrollregion='0 0 %s %s' % size)

        # Update the canvas's width to fit the inner frame
        if self.list.winfo_reqwidth() != self.view.winfo_width():
            self.view.config(width = self.list.winfo_reqwidth())

    def _wheel_bind(self, event):
        '''Bind scrolling to the mouse wheel'''
        self.view.bind_all("<MouseWheel>", self._wheel)

    def _wheel_unbind(self, event):
        '''Unbind scrolling from the mouse wheel'''
        self.view.unbind_all("<MouseWheel>") 

    def _wheel(self, event):
        '''From a mouse wheel event, scroll'''
        self.view.yview_scroll(int(-1*(event.delta/120)), "units")

'''Class definition for the items listed by the Projections List component'''
class PListItem(Frame):
    def __init__(self, root, projection: Projection):
        Frame.__init__(self, root)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.proj = projection
        self.config(
            highlightbackground=self.proj.get_color(),
            highlightcolor=self.proj.get_color(),
            highlightthickness=2,
            bd=0
        )

        # Label that specifies the location
        Label(self,
            text=self.proj.get_location()
        ).grid(row=0, column=0, sticky='w')
        
        # Checkbox that toggles visibility
        self.visibility = IntVar(self)
        self.visibility.set(1)
        Checkbutton(self, 
            variable=self.visibility, command=self._toggle
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
            text='✕', command=self._remove
        ).grid(row=0, column=2, rowspan=2, sticky='ne', padx=(5, 0))

    def _remove(self):
        '''Callback to remove an projection from the list'''
        plot.remove_projection(self.proj)

    def _toggle(self):
        '''Callback to toggle the visibility of a projection'''
        self.proj.set_visibility(self.visibility.get())

        pDisp = gb.main_window.getComponent(GUI.plotDisplay)
        pDisp.update()
