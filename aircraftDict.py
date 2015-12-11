__author__ = 'David'
import os,csv

# Class to create a dictionary of airplanes with the plane type as the keys and the range of that type as the values


class AircraftDict:
                                                                                                                        
    aircraftDict = {}                                                                    # Empty dict
                                                                                                                        
    aircraft_fn = "aircraft.csv"                                                         # Default Filename
                                                                                                                        
    def __init__(self, fileCSV = aircraft_fn):
        self.aircraftDict = self.buildDict(fileCSV)                                      # Call build method
                                                                                                                        
    def buildDict(self,filename):                                                        # Build Method
        self.aircraftDict = {}                                                           # Empty Dictionary
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            reader = csv.reader(f)                                                                                      
            for row in reader:
                if row[2] == "metric":                                                   # If metric leave in KM
                    self.aircraftDict[row[0]] = float(row[4])
                else:                                                                    # If imperial convert to KM
                    self.aircraftDict[row[0]] = float(row[4])*1.60934

        return self.aircraftDict

    def getRange(self, code):                                                            # for a certain plane type get
        try:                                                                             # corresponding range
            return self.aircraftDict[code]
        except KeyError:                                                                                                
            return None                                                                                                 