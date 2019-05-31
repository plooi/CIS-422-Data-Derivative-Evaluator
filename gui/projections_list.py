'''
Projections List
Class definition

Author:
Brian Truong
'''

from tkinter.constants import RIGHT, END
from tkinter import Frame, Listbox

class ProjectionsList(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        locationlist = Listbox(self)
        locationlist.grid(sticky='ns')
        locationlist.insert(END, "Test location 1")
        locationlist.insert(END, "Test location 2")

        # # creating a scrollbars
        # self.xscrlbr = Scrollbar(self, orient = 'horizontal')
        # self.xscrlbr.grid(column = 0, row = 1, sticky = 'ew', columnspan = 2)
        # self.yscrlbr = Scrollbar(self)
        # self.yscrlbr.grid(column = 1, row = 0, sticky = 'ns')
        # # creating a canvas
        # self.canv = Canvas(self)
        # self.canv.config(relief = 'flat', width = canv_w, bd = 2)
        # # placing a canvas into frame
        # self.canv.grid(column = 0, row = 0, sticky = 'nsew')
        # # accociating scrollbar comands to canvas scroling
        # self.xscrlbr.config(command = self.canv.xview)
        # self.yscrlbr.config(command = self.canv.yview)

        # # creating a frame to inserto to canvas
        # self.scrollwindow = Frame(self)

        # self.canv.create_window(0, 0, window = self.scrollwindow, anchor = 'nw')

        # self.canv.config(xscrollcommand = self.xscrlbr.set,
        #                  yscrollcommand = self.yscrlbr.set,
        #                  scrollregion = (0, 0, 100, 100))

        # self.yscrlbr.lift(self.scrollwindow)
        # self.xscrlbr.lift(self.scrollwindow)
        # self.scrollwindow.bind('<Configure>', self._configure_window)