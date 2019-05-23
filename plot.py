import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


'''
A function which plots the maximum or mean daily streamflow values for a 
given projection.

data_array: an xarray dataarray object with streamflow values for a certain projection
max: a Boolean value. True: plot the maximum streamflow, False: plot the mean streamflow.
'''
def plot_timeseries(data_array, max):

	gcm = data_array.gcm.values.astype(str)
	parameter = data_array.parameters.values.astype(str)
	site = data_array.outlets.values.astype(str)

	# FIXME: currently can't concatenate the projection parameters for 
	# a label of the displayed plot. Need this functionality to differentiate 
	# between different displayed timeseries. 

	# label = site + "_" + gcm + "_" + parameter

	plt.figure(figsize=(8,5))

	values = []
	for i in range(2100 - 1950):
	    year = str(1950 + i)
	    if max:
	    	val = np.max(data_array.sel(time=year))
	    if not max:
	    	val = np.mean(data_array.sel(time=year))
	    values.append(val)

	plt.ylabel('cfs')
	plt.xlabel('year')
	plt.plot([1950+i for i in range(150)], values, color='blue')
	plt.show()
