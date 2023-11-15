from matplotlib import pyplot as plt
import math
import numpy
import statistics

werte = [13.2,12.3,44.4,33.1,25.9,65.3,78.1,53.5,91.7,54.4,34.2,45.8,54.4,37.2,78.1,13.2]
minimum = 1000
maximum = 0

for i in werte:
    if (i < minimum):
        minimum = i
print(minimum)      # expected 12

for i in werte:
    if (i > maximum):
        maximum = i
print (maximum)     # expected 91

class tmp():

    def max(list):
        maxi = 0
        for i in list:
            if (i > maxi):
                maxi= i
        print (maxi)

    def min(list):
        mini = 1000
        for i in list:
            if (i < mini):
             mini = i
        print(mini)

    def floor(list):
        y = {}
        cnt = 0
        for i in list:
            y[cnt]=math.floor(i)
            cnt+=1
        print(y)

    def ceil(list):
        y = {}
        cnt = 0
        for i in list:
            y[cnt]=math.ceil(i)
            cnt+=1
        print(y)

    def mode(list):
        y={}
        for i in list:
            if not i in y:
                y[i]=1
            else:
                y[i]+=1
        print([g for g,l in y.items() if l==max(y.values())]) 

    def mean(list):
        y = 0
        erg = 0
        for i in list:
            y+=i
        erg = y/len(list)
        print(erg)

    def median(list):
        half = len(list) // 2
        list.sort()
        if not len(list) % 2:
            return (list[half - 1] + list[half]) / 2.0
        print(list[half]) 

    def range(list):
        erg = max(list)-min(list)
        print(erg)

    def standard_derivation(list):
        mean = sum(list) / len(list)
        var = sum((l-mean)**2 for l in list) / len(list)
        st_dev = math.sqrt(var)
        print(st_dev)

    def variance(list):
        n = len(list)
        mean = sum(list) / n
        deviations = [(x - mean) ** 2 for x in list]
        variance = sum(deviations) / n
        print(variance) 

tmp.max(werte)
tmp.min(werte)
tmp.floor(werte)
tmp.ceil(werte)
tmp.mode(werte)
tmp.mean(werte)
tmp.median(werte)
tmp.range(werte)
tmp.standard_derivation(werte)
tmp.variance(werte)
