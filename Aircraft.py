__author__ = 'David'
from aircraftDict import *
# Class to create Aircraft objects. Take in the plane type.
class Aircraft:

    fuel = 0

    __fuelCheck = False
    MIN_FUEL = 0
    flightNumber = ""
    __flightClearance = False
    myAircraftDict = AircraftDict()

    def __init__(self, planeType='747'):
        self.planeType = planeType

    def fuelCheck(self):
        if self.fuel < self.MIN_FUEL:
            print("Fuel Check Failed: Current fuel below level:", self.fuel," less than ", self.MIN_FUEL)
            self.__fuelCheck = False
        else:
            print("Fuel Check Complete:", self.fuel)
            self.__fuelCheck = True

    def takeOff(self):
        if self.__fuelCheck == True:
            print("Cleared for Takeoff! Fasten your seat-belt!")
        else:
            print("Take off Failed: Please complete pre-flight check first")
            print(self.fuelCheck())

    def printStatus(self):
        print("Current fuel:", self.fuel)

    def addFuel(self, volume):
        unusedFuel = 0

        if volume < 0:
            print("No syphoning fuel")
        elif self.fuel + volume <= self.getRange():
            self.fuel = self.fuel + volume
        elif self.fuel + volume > self.getRange():
            self.fuel = self.getRange()
            unusedFuel = volume - self.fuel
        return unusedFuel

    def setFlightNumber(self, aFlightNumber):
        self.flightNumber = aFlightNumber

    def preFlightCheck(self):
        if self.__fuelCheck == True and self.__flightClearance == True:
            print("Take Off Approved")

        else:
             print("Preflight checked failed")

    def fly(self, fuelused):
        self.fuel -= fuelused

    def getRange(self):
        range = self.myAircraftDict.getRange(self.planeType)
        self.MIN_FUEL = range*0.1
        return range





def main():

    myPlane = Aircraft("747")
    range = myPlane.getRange()
    print(range)

if __name__ == "__main__":
        main()
