'''
File Porter Menu
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter import Menu, filedialog, messagebox

from file_io import fileIO
import gui_bootstrap as gb
from constants import OS_HOME_DIR, FILE_INPUTS

class FilePorterMenu(Menu):
    def __init__(self, root):
        Menu.__init__(self, root)

        self.add_command(label='Import .NC', command=self.getNC)

    def getNC(self):
        try:
            file = filedialog.askopenfilename(
                initialdir=OS_HOME_DIR, title='Select the data file', filetypes=FILE_INPUTS)
            if file != '':
                fileIO.loadNC(file)
                gb.main_window.setActiveNC(file)
        except:
            messagebox.showerror('Error', 'Cannot load file!')