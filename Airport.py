__author__ = 'David'
from CountryAtlas import *
import Country
class Airport:


    countryAtlas = CountryAtlas()

    def __init__(self, airportName, cityName, country, code, latitude, longitude):

        self.airportName = airportName
        self.cityName = cityName
        self.country = self.countryAtlas.getCountry(country.upper())
        self.code = code.upper()
        self.latitude = float(latitude)
        self.longitude = float(longitude)




    def __str__(self):
        return self.code

    def __repr__(self):
        return str(self)


def main():

   myAirport = Airport("Dublin", "Dublin", "IRELAND", "DUB", "53", "-6")
   print(myAirport.country.rateTo())
   print(myAirport.country.rateFrom())






if __name__ == "__main__":
        main()
