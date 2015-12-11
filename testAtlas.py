__author__ = 'David'
from AirportAtlas import *
from ItineraryBuilder import *
from Itinerary import *


myAirportAtlas = AirportAtlas()

print(myAirportAtlas.getDistBetween('dub','jfk'))

myItineraryList = ItineraryBuilder(myAirportAtlas)

myItineraryList.orderRoutes()

print(myItineraryList.itineraryList)
