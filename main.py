# import numpy as np
# import pandas as pd
import xarray as xr
import Projection
import plot
# import gui_bootstrap
from gui.main_window import MainWindow
# import matplotlib.pyplot as plt

# xarray dataarray object which holds all the streamflow data
all_data = None

# an array of the projections which the user wants displayed
active_projections = []

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


def plot_button(gcm, mdm, rcp, hms, max):
    data = all_data.sel(parameters=hms, downscale_method=mdm, gcm=gcm, rcp=rcp)
    new_projection = Projection(rcp, gcm, mdm, hms, data)
    active_projections.append(new_projection)

    for proj in active_projections:
        plot.plot_timeseries(proj.data, max)


'''
Main function which loads the NetCDF file with all the streamflow data and runs
the GUI program.
'''


def main():
    global all_data
    # all_data = xr.open_dataarray("TDA.nc")
    testProj = Projection.Projection("RCP 4.5", "CanESM2", "Bias-corrected spatial disaggregation", "Precipitation Runoff Modeling System", max=False, location="Somewhere")
    testProj += [1, 10]
    testProj += [2, 12]
    testProj += [3, 10]
    testProj += [4, 7]
    active_projections.append(testProj)
    w = MainWindow()
    w.mainloop()


main()
