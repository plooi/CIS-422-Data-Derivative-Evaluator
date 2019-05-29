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