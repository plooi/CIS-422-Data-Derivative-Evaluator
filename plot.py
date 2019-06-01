import numpy as np
import xarray as xr
import matplotlib
matplotlib.use('PS')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from Projection import *
from file_io import fileIO


'''
A function which plots the maximum or mean daily streamflow values for a
given projection.

data_array: an xarray dataarray object with streamflow values for a certain projection
max: a Boolean value. True: plot the maximum streamflow, False: plot the mean streamflow.
'''


def plot_timeseries(projections):

    figure = Figure(figsize=(8,5), dpi=100)
    if projection.max:
        figure.title('Annual Maximum Daily Streamflow')
    else:
        figure.title('Annual Mean Daily Streamflow')
    for projection in projections:
        # label = projection.rcp + "_" + projection.gcm + "_" + projection.mdm + "_" + projection.hms
        newPlot = figure.add_subplot(1, 1, 1)

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

def add_projection(gcm: str, mdm: str, rcp: str, hms: str, color: str, mx: bool):
    data = fileIO.allData.sel(parameters=hms, downscale_method=mdm, gcm=gcm, rcp=rcp)
    new_projection = Projection(rcp, gcm, mdm, hms, color, data, mx)
    active_projections.append(new_projection)

def create_figure() -> Figure:
    figure = Figure(figsize=(8, 5), dpi=100)

    newPlot = figure.add_subplot(1, 1, 1)
    newPlot.set_ylabel('CFS')
    newPlot.set_xlabel('Year')

    for projection in active_projections:
        if not (projection.get_visibility()):
            continue
        # label = projection.rcp + "_" + projection.gcm + "_" + projection.mdm + "_" + projection.hms
        values = []
        for i in range(2100 - 1950):
            year = str(1950 + i)
            if projection.max:
                val = np.max(projection.data.sel(time=year))
            if not projection.max:
                val = np.mean(projection.data.sel(time=year))
            values.append(val)

        newPlot.plot([1950+i for i in range(150)], values, projection.get_color())

    return figure
