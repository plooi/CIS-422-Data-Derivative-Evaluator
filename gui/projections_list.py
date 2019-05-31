'''
Projections List
Class definition

Author:
Brian Truong
'''

from tkinter.constants import RIGHT, END
from tkinter import Frame, Scrollbar, Canvas

class ProjectionsList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        self.yScroll = Scrollbar(self)
        self.yScroll.grid(column = 1, row = 0, sticky = 'ns')

        self.view = Canvas(self)
        self.view.config(relief = 'flat', width = 64, bd = 2)

        self.scrollView.grid(column = 0, row = 0, sticky = 'nsew')

        self.yScroll.config(command = self.view.yview)

        self.list = Frame(self)

        self.view.create_window(0, 0, window = self.list, anchor = 'nw')
        self.view.config(yscrollcommand = self.yScroll.set,
                         scrollregion = (0, 0, 100, 100))

        self.yScroll.lift(self.scrollwindow)
        self.list.bind('<Configure>', self._configure)

    def _configure(self, event):
        # update the scrollbars to match the size of the inner frame
        size = (self.list.winfo_reqwidth(), self.list.winfo_reqheight())
        self.view.config(scrollregion='0 0 %s %s' % size)