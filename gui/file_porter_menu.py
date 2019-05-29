'''
File Porter Menu
Class definition

Author:
Ben Lain
Brian Truong
'''

from tkinter import Menu

class FilePorterMenu(Menu):
    def __init__(self, root):
        Menu.__init__(self, root)

        file = Menu(self)
        file.add_command(label="Exit", command=exit)
        file.add_command(label="Import")
        file.add_command(label="Export")

        self.add_cascade(label="File", menu=file)