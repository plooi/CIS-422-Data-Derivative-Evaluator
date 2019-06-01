'''
File Porter Menu
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter import Frame, Button, filedialog, messagebox

from file_io import fileIO
import gui_bootstrap as gb
from constants import OS_HOME_DIR, FILE_INPUTS

class FilePorterMenu(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        Button(self, text='Import .NC', command=self.getNC).pack()

    def getNC(self):
        try:
            file = filedialog.askopenfilename(
                initialdir=OS_HOME_DIR, title='Select the data file', filetypes=FILE_INPUTS)
            if file != '':
                fileIO.loadNC(file)
                gb.main_window.setActiveNC(file)
        except:
            messagebox.showerror('Error', 'Cannot load file!')