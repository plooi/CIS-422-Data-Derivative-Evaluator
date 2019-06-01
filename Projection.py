import xarray as xr

"""
Peter Looi

Class for projection
"""

# an array of the projections which the user wants displayed
active_projections = []
all_data = xr.open_dataarray("TDA.nc")


def main():
    print("Creating a new projection object\n")
    p = Projection("RCP 4.5", "CanESM2", "Bias-corrected spatial disaggregation", "Precipitation Runoff Modeling System", max=False, location="Somewhere")

    print("Adding the point [1, 10]")
    p += [1, 10]

    print("Adding the point [2, 12]")
    p += [2,12]

    print("Adding the point [3, 10]")
    p += [3,10]

    print("Adding the point [4, 7]\n\n")
    p += [4,7]

    print("Data in the projection is")
    print(p.data_string())

    print("The string representation of the projection is")
    print(p)

    print("\n\nLooping through the projection and printing out each data point")
    for data in p:
        print(data)


    print("\n\nThe GCM is \"" + str(p.get_gcm()) + "\"")
    print("The second data point is", p[1])
    print("The number of data points is", len(p))

    print("\n\nUse matplotlib to plot the data (example) \n\n<Plot shown on screen>")
    import matplotlib.pyplot as plt
    plt.plot(p.x_values(), p.y_values(), 'ro')
    plt.axis([0,6,0,20])
    plt.show()



class Projection:
    def __init__(self, RCP = None, GCM = None, MDM = None, HMS = None, color = None, data = None, max=True, location=None, visibility=True):
        self.RCP = RCP
        self.GCM = GCM
        self.MDM = MDM
        self.HMS = HMS
        self.color = color
        self.max = max
        self.location = location
        self.visibility = visibility
        self.data = data
    """
    Getters and setters
    """
    def get_rcp(self):
        return self.RCP
    def get_gcm(self):
        return self.GCM
    def get_mdm(self):
        return self.MDM
    def get_hms(self):
        return self.HMS
    def get_color(self):
        return self.color
    def get_max(self):
        return self.max
    def get_location(self):
        return self.location
    def is_visible(self):
        return self.visibility
    def get_visibility(self):
        return self.visibility


    def set_rcp(self, RCP):
        self.RCP = RCP
    def set_gcm(self, GCM):
        self.GCM = GCM
    def set_MDM(self, MDM):
        self.MDM = MDM
    def set_HMS(self, HMS):
        self.HMS = HMS
    def set_color(self, color):
        self.color = color
    def set_max(self, m):
        self.max = m
    def set_location(self, location):
        self.location = location
    def set_visibility(self, visibility):
        self.visibility = visibility

    def __getitem__(self, i):
        if type(i) == type(1):
            return self.data[i]
        elif type(i) == type(""):
            if i.upper() == "RCP":
                return self.RCP
            elif i.upper() == "GCM":
                return self.GCM
            elif i.upper() == "MDM":
                return self.MDM
            elif i.upper() == "HMS":
                return self.HMS
            elif i.upper() == "color":
                return self.color
            else:
                raise Exception("Unrecognized property \"" + str(i) + '"')
        else:
            raise Exception("Invalid type for input to __getitem__" + str(type(i)))
    def __len__(self):
        return len(self.data)
    def __setitem__(self, i, x):
        if type(i) == type(1):
            self.data[i] = x
        elif type(i) == type(""):
            if i.upper() == "RCP":
                self.RCP = x
            elif i.upper() == "GCM":
                self.GCM = x
            elif i.upper() == "MDM":
                self.MDM = x
            elif i.upper() == "HMS":
                self.HMS = x
            elif i.upper() == "color":
                self.color = x
            else:
                raise Exception("Unrecognized property \"" + str(i) + '"')
        else:
            raise Exception("Invalid type for input to __setitem__" + str(type(i)))
    def __add__(self, other):
        self.data.append(other)
        return self
    """
    Removes this projection object from the active projections
    """
    def remove(self):
        active_projections.remove(self)
    def __iter__(self):
        for i in range(len(self.data)):
            yield self.data[i]
    def __str__(self):
        out = "_____\nProjection:\n"
        out += "RCP: " + str(self.RCP) + "\n"
        out += "GCM: " + str(self.GCM) + "\n"
        out += "MDM: " + str(self.MDM) + "\n"
        out += "HMS: " + str(self.HMS) + "\n"
        out += "Color: " + str(self.color) + "\n"
        out += "Length of data: " + str(len(self)) + "\n"
        out += "max: " + str(self.get_max()) + "\n"
        out += "location: " + str(self.get_location()) + "\n"
        out += "visibility: " + str(self.is_visible()) + "\n"
        out += "_____"
        return out
    def data_string(self, delimiter="\n"):
        out = ""
        for data in self:
            out += repr(data) + delimiter
        return out
    def x_values(self):
        x = []
        for data in self:
            x.append(data[0])
        return x
    def y_values(self):
        y = []
        for data in self:
            y.append(data[1])
        return y


if __name__ == "__main__": main()




