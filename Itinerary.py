import itertools
from AirportAtlas import *
from Aircraft import *
from Country import *


class Itinerary:

    route = []
    permutationlist = []
    distancesDict = {}
    costDict = {}
    refuelCostDict = {}

    def __init__(self, myAirportList, myAircraft, atlas):
        self.route = [atlas.getAirport(myAirportList[0]), atlas.getAirport(myAirportList[1]),
                          atlas.getAirport(myAirportList[2]),atlas.getAirport(myAirportList[3]),
                            atlas.getAirport(myAirportList[4])]
        self.aircraft = Aircraft(myAircraft)

    def permutateRoute(self):
        permutations = list(itertools.permutations([self.route[1], self.route[2], self.route[3], self.route[4]]))

        for route in permutations:
            self.permutationlist.append(((self.route[0],) + route + (self.route[0],)))
        return self.permutationlist

    def getCosts(self, atlas):

        for route in self.permutationlist:
            totCost = 0
            for i in range(len(route)-1):

                rate = float(route[i+1].country.rateFrom())
                cost = atlas.getDistBetween(route[i].code, route[i+1].code)*rate
                totCost += cost
            self.costDict[route] = round(totCost,2)
        return self.costDict

    def getLowestCostRoute(self):
        return min(self.costDict, key=self.costDict.get)

    def getDistances(self, atlas):

        for route in self.permutationlist:
            totDistance = 0

            for i in range(len(route)-1):

                        dist = atlas.getDistBetween(route[i].code, route[i+1].code)
                        totDistance += dist


            self.distancesDict[route]=round(totDistance,2)
        return self.distancesDict

    def getLowestDistRoute(self):
            return min(self.distancesDict, key=self.distancesDict.get)

    def getRefuelCosts(self, atlas):

        for route in self.permutationlist:
            self.aircraft.addFuel(self.aircraft.MIN_FUEL)
            totCost = self.aircraft.MIN_FUEL
            for i in range(len(route)-1):
                if atlas.getDistBetween(route[i].code, route[i+1].code) <= self.aircraft.getRange():
                    if self.aircraft.fuel < (atlas.getDistBetween(route[i].code, route[i+1].code))*1.1:
                        rate = float(route[i].country.rateFrom())
                        cost = ((atlas.getDistBetween(route[i].code, route[i+1].code))*1.1-self.aircraft.fuel)*rate
                        totCost += cost
                        self.aircraft.addFuel(((atlas.getDistBetween(route[i].code, route[i+1].code))*1.1)-self.aircraft.fuel)
                        self.aircraft.fly(atlas.getDistBetween(route[i].code, route[i+1].code))
                    else:
                        self.aircraft.fly(atlas.getDistBetween(route[i].code, route[i+1].code))
                else:
                    totCost = 99999999999.99
            self.refuelCostDict[route] = round(totCost, 2)
        return self.refuelCostDict


    def getRefuelCostRoute(self):
        if self.refuelCostDict.get(min(self.refuelCostDict, key=self.refuelCostDict.get)) > 9999999999.99:
            return "ERROR"
        else:
            return min(self.refuelCostDict, key=self.refuelCostDict.get)






    def costMinCalculator(self):
        return self.costDict.get(min(self.costDict, key=self.costDict.get))

    def distMinCalculator(self):
        return self.distancesDict.get(min(self.distancesDict, key=self.distancesDict.get))

    def refuelMinCalculator(self):
        if self.refuelCostDict.get(min(self.refuelCostDict, key=self.refuelCostDict.get)) > 9999999999.99:
            return "Plane range too short for this route"
        else:
            return self.refuelCostDict.get(min(self.refuelCostDict, key=self.refuelCostDict.get))





def main():

        myAtlas = AirportAtlas()
        myList = ["DKB", "LHR", "SYD", "JFK", "AAL"]
        myAircraft = "MD11"
        myItin = Itinerary(myList,myAircraft,myAtlas)
        permus = myItin.permutateRoute()
        dists = myItin.getDistances(myAtlas)
        costs = myItin.getCosts(myAtlas)
        recosts = myItin.getRefuelCosts(myAtlas)

        print("The route with the shortest distance is: ", myItin.getLowestDistRoute())

        print("The route with the lowest cost is: ", myItin.getLowestCostRoute())
        print("The route with the lowest cost is: ", myItin.getRefuelCostRoute())





if __name__ == "__main__":
        main()


