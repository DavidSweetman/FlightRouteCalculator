__author__ = 'David'
import os, csv
from Currency import Currency

# Class to create a Dictionary that stores Currency information.
# Reads in from file and sets key as the currency three letter code and has the values as a list.
# The list contains the code, the conversion rate to euro and the conversion rate from euro


class CurrencyDict:
    airport_fn = "currencyrates.csv"                                              # Set default file name
    currencyDict = {}                                                             # Empty Dictionary to add to

    def __init__(self, fileCSV = airport_fn):                                     # Init Method
        self.currencyDict = self.buildCurrencyDict(fileCSV)                       # Calls the build method

    def buildCurrencyDict(self, filename):                                        # Build Method

        with open(os.path.join(filename), "rt", encoding="utf8") as f:            # Opens file to read text data
            reader = csv.reader(f)
            for row in reader:

                self.currencyDict[row[1]] = Currency(row[1], row[2], row[3])      # Value is Currency object
        return self.currencyDict

    def getCurrencyRateToEuro(self, currencyCode):                                # Method to get the rate to euro
        return self.currencyDict[currencyCode.upper()].rateTo                     # for a currency with certain code

    def getCurrencyRateFromEuro(self,currencyCode):                               # Method to get the rate from euro
        return self.currencyDict[currencyCode.upper()].rateFrom                   # for a currency with a certain code


def main():
        MyDict = CurrencyDict()                                                   # Test
        answer = MyDict.getCurrencyRateFromEuro("gbp")
        answer2 = MyDict.getCurrencyRateToEuro("gbp")
        print(answer, answer2)

if __name__ == "__main__":
        main()
