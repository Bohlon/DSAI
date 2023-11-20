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
print(f'Minimum without libs: {minimum}')      # expected 12

for i in werte:
    if (i > maximum):
        maximum = i
print(f'Maximum without libs: {maximum}')     # expected 91

class tmp():

    def max(list):
        maxi = 0
        for i in list:
            if (i > maxi):
                maxi= i
        print(f'Max: {maxi}')
        return maxi

    def min(list):
        mini = 1000
        for i in list:
            if (i < mini):
             mini = i
        print(f'Min: {mini}')
        return mini
    
    def floor(list):
        y = {}
        cnt = 0
        for i in list:
            y[cnt]=math.floor(i)
            cnt+=1
        print(f'Floor: {y}')
        return y
    
    def ceil(list):
        y = {}
        cnt = 0
        for i in list:
            y[cnt]=math.ceil(i)
            cnt+=1
        print(f'Ceil: {y}')
        return y

    def mode(list):
        y={}
        for i in list:
            if not i in y:
                y[i]=1
            else:
                y[i]+=1
        print(f'Mode: {[g for g,l in y.items() if l==max(y.values())]}')
        return [g for g,l in y.items() if l==max(y.values())]

    def mean(list):
        y = 0
        erg = 0
        for i in list:
            y+=i
        erg = y/len(list)
        print(f'Mean: {erg}')
        return erg

    def median(list):
        half = len(list) // 2
        list.sort()
        if not len(list) % 2:
            return (list[half - 1] + list[half]) / 2.0
        print(f'Median: {list[half]}')
        return list[half]

    def range(list):
        erg = max(list)-min(list)
        print(f'Range: {erg}')
        return erg

    def standard_derivation(list):
        mean = sum(list) / len(list)
        var = sum((l-mean)**2 for l in list) / len(list)
        st_dev = math.sqrt(var)
        print(f'Standart Derivation: {st_dev}')
        return st_dev

    def variance(list):
        n = len(list)
        mean = sum(list) / n
        deviations = [(x - mean) ** 2 for x in list]
        variance = sum(deviations) / n
        print(f'Variance: {variance}')
        return variance

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
