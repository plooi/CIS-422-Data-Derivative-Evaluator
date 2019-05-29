import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


'''
A function which plots the maximum or mean daily streamflow values for a 
given projection.

data_array: an xarray dataarray object with streamflow values for a certain projection
max: a Boolean value. True: plot the maximum streamflow, False: plot the mean streamflow.
'''
def plot_timeseries(projection):

	label = projection.rcp + "_" + projection.gcm + "_" + projection.mdm + "_" + projection.hms

	plt.figure(figsize=(8,5))

	values = []
	for i in range(2100 - 1950):
	    year = str(1950 + i)
	    if projection.max:
	    	val = np.max(projection.data.sel(time=year))
	    if not projection.max:
	    	val = np.mean(projection.data.sel(time=year))
	    values.append(val)

	plt.ylabel('cfs')
	plt.xlabel('year')
	plt.plot([1950+i for i in range(150)], values, color='blue')
	plt.show()
