import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv


rows = []
with open('lifeExpectancyData.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        rows.append(row)

Years = []
for r in rows:
    if(len(r) > 1):  
        if(r[0] == "Country Name"):
            for y in r[4:]:
                Years.append(y)

Data = []
CountryCodes = []
val = ""
while(val != "Q"):
    val = input("Enter country code (or 'Q' to continue): ")
    if(val != "Q"):
        currentData = []
        for r in rows:
            if(len(r) > 1 and r[1] == val):  
                lastY = 0
                for y in r[4:]:
                    if(not y):
                        currentData.append(float(lastY))
                    else:
                        currentData.append(float(y))
                        lastY = y
        Data.append(currentData)
        CountryCodes.append(val)

        
for i in range(len(Data)):
    plt.plot(Years, Data[i], label=CountryCodes[i])


ax = plt.gca()
plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='right')
plt.setp(ax.get_yticklabels(), rotation=30, horizontalalignment='right')
plt.grid(b=None, which='major', axis='both')
ax.set_ylabel("Life Expectancy at Birth")
ax.set_xlabel("Years")


# function to show the plot
plt.legend()
plt.show()
