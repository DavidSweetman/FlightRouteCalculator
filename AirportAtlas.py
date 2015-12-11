__author__ = 'David'
import os,csv
from math import *
from Airport import Airport

class AirportAtlas:
    airport_fn = "airport.csv"

    def __init__(self, fileCSV = airport_fn):
        self.airportDict = self.buildAirportDict(fileCSV)

    def buildAirportDict(self,filename):
        airportDict = {}
        with open(os.path.join(filename), "rt", encoding = "utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                airportDict[row[4]] = Airport(row[1],row[2],row[3],row[4],row[6],row[7])
        return airportDict

    def getAirport(self,code):
        try :
            return self.airportDict[code.upper()]
        except KeyError:
            return None

    def getDist(self, lg1, lt1, lg2, lt2):
        lat1 = 90 - lt1
        lat2 = 90 - lt2
        long1rad = lg1 * 2 * (pi / 360)
        lat1rad = lat1 * 2 * (pi / 360)
        long2rad = lg2 * 2 * (pi / 360)
        lat2rad = lat2 * 2 * (pi / 360)
        r = 6371
        dist = acos((sin(lat1rad) * sin(lat2rad) * cos(long1rad - long2rad)) + (cos(lat1rad) * cos(lat2rad))) * r
        return dist

    def getDistBetween(self,code1,code2):

        airport1 = self.getAirport(code1)
        airport2 = self.getAirport(code2)

        distance = int(self.getDist(airport1.longitude,airport1.latitude,airport2.longitude,airport2.latitude))
        return distance



