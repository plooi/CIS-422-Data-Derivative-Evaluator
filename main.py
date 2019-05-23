import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

all_data = None
active_projections = []

def plot_button(gcm, mdm, rcp, hms, max):

	data = all_data.sel(parameters = hms, downscale_method = mdm, gcm = gcm, rcp = rcp)
	Projection new_projection = Projection(rcp, gcm, mdm, hms, data)
	active_projections.append(new_projection)

	for proj in active_projections:
		plot_timeseries(proj.data, max)

def main():
	global all_data = xr.open_dataarray("FILEPATH")
	#run GUI