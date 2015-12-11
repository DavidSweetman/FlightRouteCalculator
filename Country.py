__author__ = 'David'
from CurrencyDict import *
# Class to create Country Objects. Takes in a name and a Currency. Has method to take in the currency rate values
# from the currency dictionary


class Country:
    cDict = CurrencyDict()                                                       # Make a Currency Dictionary
    name = ""
    currency = ""
    toEuro = 0
    fromEuro = 0

    def __init__(self, name, currency):                                          # Init Method takes name, currency
        self.name = name                                                         # Sets the name read in as the name
        self.currency = currency                                                 # Sets Currency passed in as Currency

    def rateTo(self):                                                            # Returns the rate to €
        self.toEuro= self.cDict.getCurrencyRateToEuro(self.currency)             # by getting it from corresponding line
        return self.toEuro                                                       # in the currency dictionary

    def rateFrom(self):                                                          # Returns the rate from €
        self.fromEuro = self.cDict.getCurrencyRateFromEuro(self.currency)        # by getting it from corresponding line
        return self.fromEuro                                                     # in the currency dictionary


def main():                                                                      # Test Main

    myCountry = Country("England","gbp")
    print(myCountry.rateTo())
    print(myCountry.rateFrom())






if __name__ == "__main__":
        main()
