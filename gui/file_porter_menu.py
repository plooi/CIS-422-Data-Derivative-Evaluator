'''
File Porter Menu
Class definition

Component that allows user to choose data files

Author:
Ben Lain
Brian Truong
'''

from tkinter import Frame, Button, filedialog, messagebox, StringVar, Label
from tkinter.constants import LEFT

from data_processing.file_io import fileIO
from gui.constants import OS_HOME_DIR, FILE_INPUTS

class FilePorterMenu(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        # Create the button
        Button(self, text='Choose .NC', command=self.getNC).pack(side=LEFT)

        # Create a display of the chosen file
        self.file = StringVar(self)
        self.file.set('No file loaded')
        Label(self, textvariable=self.file).pack(side=LEFT, padx=(16, 0))

    def getNC(self):
        '''Callback to get the file location of the .NC file to use'''
        try:
            file = filedialog.askopenfilename(
                initialdir=OS_HOME_DIR, title='Select the data file', filetypes=FILE_INPUTS)
            if not file in ['', ()]:
                fileIO.loadNC(file)
                self.file.set('File loaded: ' + file)
        except Exception as e:
            messagebox.showerror('File Load Error', str(e))