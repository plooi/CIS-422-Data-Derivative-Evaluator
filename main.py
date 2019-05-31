import numpy as np
# import pandas as pd
import xarray as xr
import Projection
from Projection import active_projections
from Projection import all_data
from matplotlib.figure import Figure
import plot
# import gui_bootstrap
from gui.main_window import MainWindow
# import matplotlib.pyplot as plt

# xarray dataarray object which holds all the streamflow data

# an array of the projections which the user wants displayed

'''
The function which runs after a user has selected their parameters and
wants to see the projection timeseries.

gcm, mdm, rcp, and hms
are all strings which represent the global climate model,
meterological downscaling method, representation concentration pathway,
and hydrologic model set-up respectively.

max is a boolean value indictating whether the user wants the annual
maximum daily streamflow value (True) or
the mean daily streamflow value (False) plotted.

'''



'''
Main function which loads the NetCDF file with all the streamflow data and runs
the GUI program.
'''


def main():
    w = MainWindow()
    w.mainloop()


main()
