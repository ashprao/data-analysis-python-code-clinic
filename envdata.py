#!/usr/bin/env python3

# Implements the Lake Pend Oreille data analysis challenge as used in LinkedIn
# Learning code clinics
#
# This is the authors implementation which differs in the implementation and
# adds additional data that is analysed, such as the most frequent reading
# and its frequency.

import sys
import time

start = time.time()


class WeatherReadingDict:
    """A class that holds weather readings and their respective number of occurences"""

    # Dictionaries to store weather readings and their associated occurence counts
    _valueDict = dict()

    def addValue(self, val):
        # Get air temperature from column 3 (index 2)
        if val in self._valueDict:
            self._valueDict[val] = self._valueDict[val] + 1
        else:
            self._valueDict[val] = 1

    # getKeys returns a list of keys in the dictionary

    def getAllKeys(self):
        # Get all keys included ther occurenc count as lists
        resultList = []
        for k, v in self._valueDict.items():
            for _ in range(v):
                resultList.append(k)
        return resultList

    # average returns the average of all the keys in the dictionary taking into
    # account their count of occurences

    def average(self):
        sum = 0.0
        count = 0
        for k, v in self._valueDict.items():
            sum += k * v
            count += v
        return sum / float(count)

    # median returns the median of the keys in the dictionary taking into
    # account their count of occurences

    def median(self):
        # Get sorted list of keys which correspond to weather readings from the dictionary
        sortedList = sorted(self.getAllKeys())

        mid = int(len(sortedList) / 2)
        if len(sortedList) % 2 == 0:
            # Even number of values in list. Return the avg of the middle two values
            return (sortedList[mid-1] + sortedList[mid]) / 2
        else:
            return sortedList[mid]

    # getLowHigh returns the lowest and highest reading from a dictionary

    def getLowHigh(self):
        sortedList = sorted(self._valueDict.keys())
        return sortedList[0], sortedList.pop()

    # getMostFrequent returns the value with the highest occurence

    def getMostFrequent(self):
        # Create a count dictionary of all the counts as keys associated with a list of readings
        countDict = dict()
        for k, v in self._valueDict.items():
            # Get air temperature from column 3 (index 2)
            if v in countDict:
                countDict[v].append(k)
            else:
                countDict[v] = [k]

        # Get counts as list and return highest count and associated list of readings
        high = sorted(countDict.keys()).pop()
        return countDict[high], high


# Dictionaries to store air temperature, barometric pressure and wind speed
# readings and their associated occurence counts
airTempDict, barPressureDict, windSpeedDict = WeatherReadingDict(), WeatherReadingDict(), WeatherReadingDict()

if len(sys.argv) > 1:
    # Command line contains file name parameter
    try:
        with open(sys.argv[1]) as dataFile:  # Safely close at the end of block
            # Skip the header line
            dataFile.readline()

            # Process the data lines
            count = 0
            for line in dataFile:
                count += 1
                words = line.rsplit()

                # Get air temperature from column 3 (index 2)
                airTempDict.addValue(float(words[2]))

                # Get barometric pressure from column 4 (index 3)
                barPressureDict.addValue(float(words[3]))

                # Get wind speed from column 9 (index 8)
                windSpeedDict.addValue(float(words[8]))

            print("Total readings: ", count)

            airLowHigh, barLowHigh, windLowHigh = airTempDict.getLowHigh(
            ), barPressureDict.getLowHigh(), windSpeedDict.getLowHigh()
            airFreq, barFreq, windFreq = airTempDict.getMostFrequent(
            ), barPressureDict.getMostFrequent(), windSpeedDict.getMostFrequent()

            print('Air temperature: Average {0:.2f}, Median {1:.2f}, Low {2:.2f}, High {3:.2f}, Most frequent {4}, Frequency {5}'
                  .format(airTempDict.average(), airTempDict.median(), airLowHigh[0], airLowHigh[1], airFreq[0], airFreq[1]))
            print('Barometric pressure: Average {0:.2f}, Median {1:.2f}, Low {2:.2f}, High {3:.2f}, Most frequent {4}, Frequency {5}'
                  .format(barPressureDict.average(), barPressureDict.median(), barLowHigh[0], barLowHigh[1], barFreq[0], barFreq[1]))
            print('Wind speed: Average {0:.2f}, Median {1:.2f}, Low {2:.2f}, High {3:.2f}, Most frequent {4}, Frequency {5}'
                  .format(windSpeedDict.average(), windSpeedDict.median(), windLowHigh[0], windLowHigh[1], windFreq[0], windFreq[1]))
    except FileNotFoundError:
        print(sys.argv[1], " does not exist")
else:
    print("Pass a data file name as command line input")

end = time.time()
print()
print("Total time: {0:.2f}".format(end - start))
