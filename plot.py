import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from Projection import *



'''
A function which plots the maximum or mean daily streamflow values for a
given projection.

data_array: an xarray dataarray object with streamflow values for a certain projection
max: a Boolean value. True: plot the maximum streamflow, False: plot the mean streamflow.
'''


def plot_timeseries(projections):

    figure = Figure(figsize=(8,5), dpi=100)
    for projection in projections:
        # label = projection.rcp + "_" + projection.gcm + "_" + projection.mdm + "_" + projection.hms
        newPlot = figure.add_subplot(111)

        values = []
        for i in range(2100 - 1950):
            year = str(1950 + i)
            if projection.max:
                val = np.max(projection.data.sel(time=year))
            if not projection.max:
                val = np.mean(projection.data.sel(time=year))
            values.append(val)

        newPlot.set_ylabel('cfs')
        newPlot.set_xlabel('year')
        newPlot.plot([1950+i for i in range(150)], values, color='blue')
        newPlot.show()
    return figure

def plot_button(gcm, mdm, rcp, hms, mx):
    data = all_data.sel(parameters=hms, downscale_method=mdm, gcm=gcm, rcp=rcp)
    new_projection = Projection(rcp, gcm, mdm, hms, data, mx)
    active_projections.append(new_projection)


    figure = Figure(figsize=(8,5), dpi=100)
    for projection in active_projections:
        # label = projection.rcp + "_" + projection.gcm + "_" + projection.mdm + "_" + projection.hms
        newPlot = figure.add_subplot(111)

        values = []
        for i in range(2100 - 1950):
            year = str(1950 + i)
            if projection.max:
                val = np.max(projection.data.sel(time=year))
            if not projection.max:
                val = np.mean(projection.data.sel(time=year))
            values.append(val)

        newPlot.set_ylabel('cfs')
        newPlot.set_xlabel('year')
        newPlot.plot([1950+i for i in range(150)], values, color='blue')

    return figure


