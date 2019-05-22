import numpy as np
import pandas as pd
import xarray as xr
import matplotlib.pyplot as plt

def plot_max_timeseries(data_array):

	gcm = data.gcm.values.astype(str)
	parameter = data.parameters.values.astype(str)
	site = data.outlets.values.astype(str)

	#label = site + "_" + gcm + "_" + parameter

	plt.figure(figsize=(8,5))

	maxes = []
	for i in range(2100 - 1950):
	    year = str(1950 + i)
	    mx = np.max(data.sel(time=year))
	    maxes.append(mx)

	plt.ylabel('cfs')
	plt.xlabel('year')
	plt.plot([1950+i for i in range(150)], maxes, color='blue')
	plt.show()


def plot_mean_timeseries(data_array)
	gcm = data.gcm.values.astype(str)
	parameter = data.parameters.values.astype(str)
	site = data.outlets.values.astype(str)

	#label = site + "_" + gcm + "_" + parameter

	plt.figure(figsize=(8,5))

	means = []
	for i in range(2100 - 1950):
	    year = str(1950 + i)
	    mn = np.mean(data.sel(time=year))
	    means.append(mn)

	plt.ylabel('cfs')
	plt.xlabel('year')
	plt.plot([1950+i for i in range(150)], means, color='blue')
	plt.show()
