"""
Author: Peter Looi
5/30/19
Locations.py: Implements a location search
"""





"""
This is the only function you need to worry about

Input a string to search for. For example "Willamette"

Returns a list of Locations that match that search string
"""
def search_locations(search_string):
    search_string = search_string.strip()
    search_string = search_string.split(" ")
    if len(search_string) == 0:
        ret = []
        for location in locations:
            ret.append(location)
        return ret
    """elif len(search_string) == 1:
        for location in locations:
            if location.get_abbreviation() == search_string[0]:
                return location
    """
    ret = []
    for location in locations:
        add_the_location = True
        for search_keyword in search_string:
            if search_keyword.lower() in location.get_abbreviation().lower() or search_keyword.lower() in location.get_name().lower():
                #then add the location can still be true
                pass
            else:
                #then this search keyword doesnt match. this location cannot be added
                add_the_location = False
                break
        if add_the_location:
            ret.append(location)
    return ret

"""
search_locations returns a list of Location objects
"""
class Location:
    def __init__(self, abbreviation=None, name=None):
        self.abbreviation = abbreviation
        self.name = name
    def set_abbreviation(self, abbreviation):
        self.abbreviation = abbreviation
    def get_abbreviation(self):
        return self.abbreviation
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __repr__(self):
        return self.abbreviation + " : " + self.name
    def __str__(self):
        return self.abbreviation + " : " + self.name











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

def read_csv(csv_name):
    f = open(csv_name)
    csv = []
    for line in f:
        csv.append(line.split(";"))
    return csv

def get_locations():
    c = CSV("streamflow_locations.csv")
    locations = []
    for line in c:
        if len(line) >= 2:
            locations.append(Location(line[0], line[1]))
    return locations
locations = get_locations()


                
def main():
    while True:
        p(search_locations(input("search:")))
def p(a):
    for item in a:
        print(item)

if __name__ == "__main__": main()
        
