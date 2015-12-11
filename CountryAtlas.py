__author__ = 'David'

import os,csv
from Country import *
# Class to creat an atlas, a dictionary of all the Countries, which has country name as key
# and a Country object with country name and currency code creating the object.

class CountryAtlas:

    countryDict = {}

    country_fn = "countrycurrency.csv"                                                  # Default Filename

    def __init__(self, fileCSV = country_fn):
        self.countryDict = self.buildDict(fileCSV)                                      # Call build method

    def buildDict(self,filename):                                                       # Build Method
        self.countryDict = {}                                                           # Empty Dictionary
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:                                                          # For each line, make a dict
                self.countryDict[row[15].upper()] = Country(row[15].upper(),row[14].upper())  # with country name as key
        return self.countryDict                                                         # and a country object as val


    def getCountry(self,code):
        try :
            return self.countryDict[code.upper()]                                       # Return the country object for
        except KeyError:                                                                # For a certain country name
            return None