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

def add_projection(location: str, gcm: str, mdm: str, rcp: str, hms: str, color: str, mx: bool):
    data = fileIO.allData.sel(outlets=location, parameters=hms, downscale_method=mdm, gcm=gcm, rcp=rcp)
    annual_values = []
    for i in range(2100 - 1950):
        year = str(1950 + i)
        if mx:
            val = np.max(data.sel(time=year))
        if not mx:
            val = np.mean(data.sel(time=year))
        annual_values.append(val)
    new_projection = Projection(rcp, gcm, mdm, hms, color, annual_values, mx, location)
    active_projections.append(new_projection)

def create_figure() -> Figure:
    figure = Figure(figsize=(8, 5), dpi=100)

    newPlot = figure.add_subplot(1, 1, 1)
    newPlot.title.set_text('Annual Maximum or Mean Streamflow')
    newPlot.set_ylabel('Streamflow (cms)')
    newPlot.set_xlabel('Time (years 1950-2100)')

    for projection in active_projections:
        if not (projection.get_visibility()):
            continue
        newPlot.plot([1950+i for i in range(150)], projection.data, projection.get_color())

    return figure
