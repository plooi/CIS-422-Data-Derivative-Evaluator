'''
Projection Plotting Module

Manages the active projections,
and creates representations of the plotted projections

Authors:
Laura Queen
Ben Lain
Brian Truong
'''

import numpy as np
import xarray as xr

import matplotlib
matplotlib.use('PS')

import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from data_processing.Projection import Projection
from data_processing.file_io import fileIO

import gui.bootstrap as gb
from gui.constants import GUI

'''The static list of active projections'''
active_projections = []

def add_projection(location: str, gcm: str, mdm: str, rcp: str, hms: str, color: str, mx: bool):
    '''
    Creates an active Projection with the maximum or mean daily streamflow values

    Parameters
    location -- the outlet location
    gcm   -- global climate model
    mdm   -- meteorological  downscaling method
    rcp   -- representative concentration pathway
    hms   -- hydrologic model setup
    color -- the color of the projection's representation
    mx    -- whether or not data values are the max or the mean
    '''
    # Properly encode the location key
    location = location.encode('ascii', 'ignore')

    # Get the data from the netCDF using the given parameters
    data = fileIO.allData.sel(outlets=location, parameters=hms, downscale_method=mdm, gcm=gcm, rcp=rcp)

    # Calculate the anual streamflow values
    annual_values = []
    for i in range(2100 - 1950):
        year = str(1950 + i)
        if mx:
            val = np.max(data.sel(time=year))
        if not mx:
            val = np.mean(data.sel(time=year))
        annual_values.append(val)

    # Add the projection to the list of active projections
    new_projection = Projection(rcp, gcm, mdm, hms, color, annual_values, mx, location)
    active_projections.append(new_projection)
    _updateGUI()

def remove_projection(p: Projection):
    '''Removes a projection from the active projections list'''
    active_projections.remove(p)
    _updateGUI()

def create_figure() -> Figure:
    '''Creates a Figure to be displayed'''
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

def _updateGUI():
    '''Update relevant GUI components'''
    pDisp = gb.main_window.getComponent(GUI.plotDisplay)
    pDisp.update()
    pList = gb.main_window.getComponent(GUI.projectionsList)
    pList.update()