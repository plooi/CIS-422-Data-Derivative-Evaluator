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

        self.add_command(label="Import CVF")
        self.add_command(label="Export PNG")
