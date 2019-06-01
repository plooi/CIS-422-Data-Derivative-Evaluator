'''
File IO
Class definition

Author:
Brian Truong
'''

import xarray as xr

class FileIO:
    def __init__(self):
        self.allData = None
        self.rcp = []
        self.gcm = []
        self.mdm = []
        self.hms = []

    # Loads a .nc file from a given location
    def loadNC(self, file: str):
        self.allData: xr.DataArray = xr.open_dataarray(file)

fileIO = FileIO()