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

# getKeys returns all of the keys corresponding to weather readings from 
# a given dictionary taking into account the number of occurences for each reading
def getKeys(valueDict):
    # Get all keys included ther occurenc count as lists
    resultList = []
    for k, v in valueDict.items():
        for _ in range(v):
            resultList.append(k)
    return resultList

# average returns the average of all the keys in the dictionary taking into 
# account their count of occurences
def average(valueDict):
    sum = 0.0
    count = 0
    for k, v in valueDict.items():
        sum += k * v
        count += v
    return sum / float(count)

# median returns the median of the keys in the dictionary taking into 
# account their count of occurences
def median(valueDict):
    # Get sorted list of keys which correspond to weather readings from the dictionary
    sortedList = sorted(getKeys(valueDict))

    mid = int(len(sortedList) / 2)
    if len(sortedList) % 2 == 0:
        # Even number of values in list. Return the avg of the middle two values
        return (sortedList[mid-1] + sortedList[mid]) / 2
    else:
        return sortedList[mid]

# getHigh returns the highest reading from a dictionary
def getLowHigh(valueDict):
    sortedList = sorted(valueDict.keys())
    return sortedList[0], sortedList.pop()

# getMostFrequent returns the value with the highest occurence
def getMostFrequent(valueDict):
    # Create a count dictionary of all the counts as keys associated with a list of readings
    countDict = dict()
    for k, v in valueDict.items():
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
airTemDict, barPressureDict, windSpeedDict = dict(), dict(), dict()

if len(sys.argv) > 1:
    # Command line contains file name parameter
    try:
        with open(sys.argv[1]) as dataFile: # Safely close at the end of block
            # Skip the header line
            dataFile.readline()

            # Process the data lines
            count = 0
            for line in dataFile:
                count += 1
                words = line.rsplit()
                
                # Get air temperature from column 3 (index 2)
                if float(words[2]) in airTemDict:
                    airTemDict[float(words[2])] = airTemDict[float(words[2])] + 1
                else:
                    airTemDict[float(words[2])] = 1

                # Get barometric pressure from column 4 (index 3)
                if float(words[3]) in barPressureDict:
                    barPressureDict[float(words[3])] = barPressureDict[float(words[3])] + 1
                else:
                    barPressureDict[float(words[3])] = 1

                # Get wind speed from column 9 (index 8)
                if float(words[8]) in windSpeedDict:
                    windSpeedDict[float(words[8])] = windSpeedDict[float(words[8])] + 1
                else:
                    windSpeedDict[float(words[8])] = 1
            

            print("Total readings: ", count)

            airLowHigh, barLowHigh, windLowHigh = getLowHigh(airTemDict), getLowHigh(barPressureDict), getLowHigh(windSpeedDict)
            airFreq, barFreq, windFreq = getMostFrequent(airTemDict), getMostFrequent(barPressureDict), getMostFrequent(windSpeedDict)

            print('Air temperature: Average {0:.2f}, Median {1:.2f}, Low {2:.2f}, High {3:.2f}, Most frequent {4}, Frequency {5}'.format(average(airTemDict), median(airTemDict), airLowHigh[0], airLowHigh[1], airFreq[0], airFreq[1]))
            print('Barometric pressure: Average {0:.2f}, Median {1:.2f}, Low {2:.2f}, High {3:.2f}, Most frequent {4}, Frequency {5}'.format(average(barPressureDict), median(barPressureDict), barLowHigh[0], barLowHigh[1], barFreq[0], barFreq[1]))
            print('Wind speed: Average {0:.2f}, Median {1:.2f}, Low {2:.2f}, High {3:.2f}, Most frequent {4}, Frequency {5}'.format(average(windSpeedDict), median(windSpeedDict), windLowHigh[0], windLowHigh[1], windFreq[0], windFreq[1]))
    except FileNotFoundError:
        print(sys.argv[1], " does not exist")
else:
    print("Pass a data file name as command line input")

end = time.time()
print()
print("Total time: {0:.2f}".format(end - start))