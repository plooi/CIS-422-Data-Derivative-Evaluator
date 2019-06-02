'''
This file contains application wide constants

Author:
Brian Truong
'''

import os

# Enum used to access GUI components
class GUI:
    outletSelection = 1
    filePorterMenu = 2
    projectionInputs = 3
    projectionsList = 4
    plotDisplay = 5

# Font constants
FONT = 'Sans Serif'
FONT_SMALL = (FONT, 8)
FONT_NORMAL = (FONT, 10)
FONT_BOLD = (FONT, 10, 'bold')

# OS specific information
OS_HOME_DIR = "%USERPROFILE%" if (os.name == "nt") else "~"

# File I/O stuff
FILE_INPUTS = [
    ('netCDF4 files', '*.nc')
]