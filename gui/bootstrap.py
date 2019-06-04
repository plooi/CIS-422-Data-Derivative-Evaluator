'''
GUI Bootstrapping

Provides the live instance of the main window,
and a method to instantiate the live instance

Author: Brian Truong
'''

main_window = None

def bootstrap():
    '''Launches the GUI'''
    global main_window

    if (main_window != None):
        return

    from gui.main_window import MainWindow
    main_window = MainWindow()
    main_window.mainloop()
