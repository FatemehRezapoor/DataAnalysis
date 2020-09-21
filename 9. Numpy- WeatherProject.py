# July 2020
# OBJECCTIVE: 1. Load NOAA station and temp date from text files, 2. Integrate, smooth anf plot data, 3. Compute daily records

import numpy as np
import matplotlib.pyplot as plt
import seaborn

# 1. RETRIEVE DATA FROM WEBSITE
import urllib.request
"""
Text file has been saved in the drive. To speed up the process I comment out the file.

mtext=urllib.request.urlretrieve('ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt','stations.txt')

"""
print(open('stations.txt','r').readlines()[:10])

# 2. GATHER DATA FRROM THE FILE WHICH HAS GSN KEYWORD: IF it does, we take the line and split the line and save in another folder

stations = {}
for line in open('stations.txt','r'):
    if 'GSN' in line:
        fields=line.split()
        #print(fields)
        stations[fields[0]]=' '.join(fields[4:]) # Use the first index as a key and 4 to the rest elements as values of the dictionaey
print(len(stations))
#print(stations)
#print((stations.items())) # A view object that displays a list of a given dictionary’s (key, value) tuple pair.

# 3. SELECT SPECIAL KEYS/VALUES IN THE DICTIONARY

def findstation(s):
    found={code:name for code,name in stations.items() if s in name}
    print('Your Station is:', found)

findstation('LIHUE')
findstation('SAN DIEGO')
findstation('MINNEAPOLIS')
findstation('IRKUTSK')

# 4. SAVE THESE IN A LIST
datastations = ['USW00022536','USW00023188','USW00014922','RSM00030710']
#print(datastations)

# 5. LET'S CHECK THE TEMEPRATURE DATA
print(open('USW00022536.dly','r').readlines()[:10])
# The instruction to read the data is summerized in the text file

# 6.
