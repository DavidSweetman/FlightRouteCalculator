import os, csv
from Airport import *
from Aircraft import *
from AirportAtlas import *
from Itinerary import *


class ItineraryBuilder:

    routes_fn = "testroutes.csv"

    def __init__(self, atlas=AirportAtlas(), fileCSV=routes_fn):
        self.itineraryList = self.buildItineraryList(fileCSV, atlas)

    def buildItineraryList(self,filename,atlas):
        itineraryList = []
        with open(os.path.join(filename), "rt", encoding="utf8") as f:
            reader = csv.reader(f)
            for row in reader:
                airportList = [row[0], row[1], row[2], row[3],row[4]]
                airplane = row[5]
                itinerary = Itinerary(airportList, airplane, atlas)
                itineraryList.append(itinerary)
            return itineraryList


    def writeBestRoutes(self, filename, myAtlas):
        bestroutes = {}
        myAtlas = AirportAtlas()                                                         # Create Atlas
        buildItin = ItineraryBuilder(myAtlas)                                            # Build Itineraries
        myItin = buildItin.itineraryList                                                 # List of Itineraries
        print(type(myItin))
        for i in range(len(myItin)):                                                     # Cycle through itineraries
             permus = myItin[i].permutateRoute()                                         # get all perms for route
             refuel = myItin[i].getRefuelCosts(myAtlas)
             bestroutes[myItin[i].getRefuelCostRoute()] = myItin[i].refuelMinCalculator()

        with open(filename, 'w') as f:
            w = csv.DictWriter(f, bestroutes.keys())
            w.writeheader()
            w.writerow(bestroutes)

    def __str__(self):
        return str(self.itineraryList)


def main():                                                                              # Test
        myAtlas = AirportAtlas()                                                         # Create Atlas
        buildItin = ItineraryBuilder(myAtlas)                                            # Build Itineraries

        # myItin = buildItin.itineraryList                                                 # List of Itineraries
        # print(type(myItin))
        # for i in range(len(myItin)):                                                     # Cycle through itineraries
        #     permus = myItin[i].permutateRoute()                                          # get all perms for route
        #     dists = myItin[i].getDistances(myAtlas)                                      # Get all the dists
        #     costs = myItin[i].getCosts(myAtlas)                                          # Get all the costs
        #     refuel = myItin[i].getRefuelCosts(myAtlas)
        #     print("Journey: ", i+1)
        #     print("The route with the shortest distance is: ", myItin[i].getLowestDistRoute())
        #     print("Distance:", myItin[i].distMinCalculator(),"km")                               # min value
        #     print("The route with the lowest cost is: ", myItin[i].getLowestCostRoute())
        #     print("Cost:", myItin[i].costMinCalculator(), "euro")                                # min value
        #     print("The route with the lowest cost with refueling is: ", myItin[i].getRefuelCostRoute())
        #     print("Cost:", myItin[i].refuelMinCalculator(), "euro")                                # min value
        #     print("---------------------------------------------------------")


        buildItin.writeBestRoutes("test1.csv",myAtlas)





if __name__ == "__main__":
        main()
