"""
Location Search Module

Implements a location search

Author: Peter Looi 5/30/19
"""

from typing import List
import data_processing.file_io as file_io

"""Class definition for a Location"""
class Location:
    def __init__(self, abbreviation:str=None, name:str=None):
        self.abbreviation = abbreviation
        self.name = name
        self.valid = False
    """Setter and getter for the outlet abbreviation/code"""
    def set_abbreviation(self, abbreviation):
        self.abbreviation = abbreviation
    def get_abbreviation(self):
        return self.abbreviation
    """Setter and getter for the outlet's human readable name"""
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    """Setter and getter for the outlet validity (inclusion in the .NC file)"""
    def set_valid(self, v):
        self.valid = v
    def get_valid(self):
        return self.valid
    """String representation of the outlet"""
    def __repr__(self):
        return self.abbreviation + " : " + self.name # + " : valid? " + str(self.is_valid())
    def __str__(self):
        return repr(self)

"""Class used to represent a CSV file"""
class CSV:
    def __init__(self, file_name):
        self.grid = read_csv(file_name)
    def __getitem__(self, i):
        return self.grid[i]
    def __len__(self):
        return len(self.grid)
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]
    def __str__(self):
        ret = ""
        for line in self:
            ret += str(line)
            ret += "\n"
        return ret

def search_locations(search_string: str) -> List[Location]:
    """
    This is the only function you need to worry about

    Input a string to search for. For example "Willamette"

    Returns a list of Locations that match that search string
    """
    locations = get_locations()

    # Return all locations on empty string
    search_string = search_string.strip()
    search_string = search_string.split(" ")
    if len(search_string) == 0:
        ret = []
        for location in locations:
            ret.append(location)
        return ret

    # Do actual search
    ret = []
    for location in locations:
        add_the_location = True
        for search_keyword in search_string:
            if (search_keyword.lower() in location.get_abbreviation().lower()
                or search_keyword.lower() in location.get_name().lower()):
                # Then location can still be added
                pass
            else:
                # Then this search keyword doesn't match. This location cannot be added
                add_the_location = False
                break
        if add_the_location:
            ret.append(location)

    tag_locations(ret)

    return ret

def tag_locations(locations: List[Location]):
    """Sets the validity of the locations"""
    try:
        x = file_io.fileIO.allData.outlets
    except:
        #allData is None
        return
    for outlet_abbreviation in file_io.fileIO.allData.outlets:
        for location in locations:
            if location.abbreviation == get_string(outlet_abbreviation):
                location.set_valid(True)

def get_string(ob):
    """Parse out locations from list ASCII encoded strings"""
    ob = repr(ob)
    ob = ob[ob.find("b")+2:]
    return ob[0:ob.find("'")]

def read_csv(csv_name: str) -> CSV:
    """Read a CSV file from a given filename"""
    f = open(csv_name)
    csv = []
    for line in f:
        csv.append(line.split(";"))
    return csv

def get_locations() -> List[Location]:
    """Get a list of the locations from a CSV file"""
    c = CSV("streamflow_locations.csv")
    locations = []
    for line in c:
        if len(line) >= 2:
            locations.append(Location(line[0], line[1]))
    return locations

"""Main function used to test this module"""
def main():
    p = lambda a: list(map(print, a))
    while True:
        p(search_locations(input("search:")))

if __name__ == "__main__": main()
