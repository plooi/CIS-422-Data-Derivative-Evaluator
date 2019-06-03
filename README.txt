Hydroclimate Change Data Visualizer README



Description: Hydroclimate Change Data Visualizer is a software tool for plotting flood-risk projection data in the Pacific Northwest. Projections are categorized by 4 projection parameters.

Authors: Edward Cho, Ben Lain, Peter Looi, Kylie Quan, Laura Queen, Brian Truong

Software created for CIS422 Programming Assignment 2

Program installation and setup
    1. Install Python
        Go to https://www.python.org/downloads/
        Install the latest version of python
    2. Download the HydroclimateChangeDataVisualizer.zip file. Unzip the file, and then move it to the desired location.
    3. Navigate to the HydroclimateChangeDataVisualizer 
    4. Install prerequisite libraries
        Execute "pip install matplotlib"
        Execute "pip install xarray"
        Execute "pip install netCDF4"
    5. Execute "python main.py" to launch the software
    
Directories
    "Hydroclimate-Change-Data-Visualizer" directory - contains data files as well as the executable main.py file. Data files include streamflow_locations.csv, which provides the software with information about each outlet location, as well as .nc files, which contain projection data.
        "data_processing" directory - contains Python files responsible for back-end data processing.
        "gui" directory - contains Python files responsible for the user interface
        