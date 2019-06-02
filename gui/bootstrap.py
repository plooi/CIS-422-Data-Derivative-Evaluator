'''
GUI Bootstrapping

Provides the live instance of the main window,
and a method to instantiate the live instance

Author: Brian Truong
'''

main_window = None

def bootstrap():
    from gui.main_window import MainWindow

    global main_window
    main_window = MainWindow()
    main_window.mainloop()
