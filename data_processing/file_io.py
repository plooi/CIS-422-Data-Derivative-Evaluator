'''
File IO
Class definition

Author:
Brian Truong
'''

import xarray as xr
import gui.bootstrap as gb
from gui.constants import GUI

class FileIO:
    def __init__(self):
        self.allData = None

    def loadNC(self, file: str):
        '''
        Loads the given .nc file,
        sets the required parameters as lists
        '''
        self.allData = xr.open_dataarray(file)

        rcp = self.allData.rcp.values
        gcm = self.allData.gcm.values
        mdm = self.allData.downscale_method.values
        hms = self.allData.parameters.values

        pInputs = gb.main_window.getComponent(GUI.projectionInputs)
        pInputs.create(rcp, gcm, mdm, hms)

        oSelection = gb.main_window.getComponent(GUI.outletSelection)
        oSelection.refresh()

fileIO = FileIO()
